"""Helpers for loading modules from file paths with spaces and top-level side effects."""

import importlib.util
import io
import sys
import types
from contextlib import contextmanager
from unittest.mock import patch


@contextmanager
def suppress_stdout_and_input(input_value="0"):
    """Suppress stdout and mock input() during module loading."""
    with patch("sys.stdout", new_callable=io.StringIO):
        with patch("builtins.input", return_value=input_value):
            yield


def load_module_from_path(filepath, module_name=None, input_value="0"):
    """Load a Python module from an arbitrary file path, suppressing side effects.

    Handles directory names with spaces and top-level print/input calls.
    Returns the module namespace.
    """
    if module_name is None:
        module_name = filepath.rsplit("/", 1)[-1].replace(".py", "").replace(" ", "_")

    spec = importlib.util.spec_from_file_location(module_name, filepath)
    module = importlib.util.module_from_spec(spec)

    with suppress_stdout_and_input(input_value):
        try:
            spec.loader.exec_module(module)
        except Exception:
            pass

    return module


def load_classes_from_source(filepath, class_names, input_value="0"):
    """Load specific classes/functions from source, extracting only valid code.

    Useful for files with syntax errors in non-class portions.
    Returns a dict of {name: object}.
    """
    import ast
    import textwrap

    with open(filepath, "r") as f:
        source = f.read()

    results = {}
    namespace = {}

    # Try to parse the whole file first
    try:
        tree = ast.parse(source)
        # Extract class and function definitions
        extracted_lines = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.ClassDef, ast.FunctionDef)):
                if node.name in class_names:
                    segment = ast.get_source_segment(source, node)
                    if segment:
                        extracted_lines.append(segment)
        if extracted_lines:
            code = "\n\n".join(extracted_lines)
            exec(code, namespace)
            for name in class_names:
                if name in namespace:
                    results[name] = namespace[name]
            return results
    except SyntaxError:
        pass

    # Fallback: extract top-level class/function blocks by scanning lines.
    # Inner defs (methods) are kept as part of the enclosing class block.
    lines = source.split("\n")
    current_block = []
    current_name = None
    block_indent = None

    def _save_block():
        if current_name and current_name in class_names and current_block:
            block_code = "\n".join(current_block)
            try:
                exec(block_code, namespace)
                if current_name in namespace:
                    results[current_name] = namespace[current_name]
            except Exception:
                pass

    for line in lines:
        stripped = line.lstrip()
        line_indent = len(line) - len(stripped)

        is_class_or_def = stripped.startswith("class ") or stripped.startswith("def ")

        if is_class_or_def:
            if block_indent is not None and line_indent > block_indent:
                # Inner def/class (e.g. a method) — part of current block
                current_block.append(line)
                continue

            # Top-level class/def: save previous block first
            _save_block()

            if stripped.startswith("class "):
                name = stripped.split("class ")[1].split("(")[0].split(":")[0].strip()
            else:
                name = stripped.split("def ")[1].split("(")[0].strip()
            current_name = name
            current_block = [line]
            block_indent = line_indent
        elif current_name is not None and block_indent is not None:
            if line.strip() == "" or line.strip().startswith("#"):
                current_block.append(line)
            elif line_indent > block_indent:
                current_block.append(line)
            else:
                _save_block()
                current_block = []
                current_name = None
                block_indent = None

    _save_block()
    return results
