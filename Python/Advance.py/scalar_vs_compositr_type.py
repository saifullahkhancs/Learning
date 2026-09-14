# ==============================================================================
# DEFINITIONS: Scalar vs Composite in Deep Copy vs Shallow Copy
# ==============================================================================
#
# 1. SCALAR TYPES (int, float, str, bool, tuple*):
#    - Are immutable and atomic values.
#    - Copying behavior: Neither shallow nor deep copies duplicate scalar objects 
#      in memory. Python reuses the existing object reference because scalar 
#      values cannot be mutated in-place.
#    *Note: Tuples are composite structures, but if a tuple contains ONLY 
#     scalars, copy operations return the same tuple reference as an optimization.
#
# 2. COMPOSITE TYPES (list, dict, set, custom objects):
#    - Containers holding references to other objects.
#    - SHALLOW COPY (`copy.copy()`): Creates a NEW outer container, but copies 
#      REFERENCES to the inner elements. Modifying nested mutable items affects 
#      both original and copy.
#    - DEEP COPY (`copy.deepcopy()`): Creates a NEW outer container AND 
#      recursively creates NEW copies of all inner composite elements. 
#      Modifications are entirely isolated.
# ==============================================================================

import copy

# ------------------------------------------------------------------------------
# 1. SCALAR BEHAVIOR (References Are Reused)
# ------------------------------------------------------------------------------
def demonstrate_scalar_copy():
    print("=== 1. SCALAR TYPES & IMMUTABLE BEHAVIOR ===")
    a = 1000
    b = copy.copy(a)
    c = copy.deepcopy(a)

    print(f"Original value 'a': {a} (Memory ID: {id(a)})")
    print(f"Shallow copy 'b':  {b} (Memory ID: {id(b)})")
    print(f"Deep copy    'c':  {c} (Memory ID: {id(c)})")
    print(f"Are all IDs identical? {id(a) == id(b) == id(c)}")


# ------------------------------------------------------------------------------
# 2. COMPOSITE BEHAVIOR (Shallow vs Deep Copy)
# ------------------------------------------------------------------------------
def demonstrate_composite_copy():
    print("\n=== 2. COMPOSITE TYPES (Nested Containers) ===")

    # Original nested structure containing scalar items and nested composite items
    original = [[1, 2], [3, 4]]

    shallow_arr = copy.copy(original)
    deep_arr = copy.deepcopy(original)

    print(f"Original: {original} | Outer ID: {id(original)} | Inner [0] ID: {id(original[0])}")
    print(f"Shallow:  {shallow_arr} | Outer ID: {id(shallow_arr)} | Inner [0] ID: {id(shallow_arr[0])}")
    print(f"Deep:     {deep_arr} | Outer ID: {id(deep_arr)} | Inner [0] ID: {id(deep_arr[0])}")

    print("\n--- Modifying nested composite element: original[0][0] = 999 ---")
    original[0][0] = 999

    print(f"Original:    {original}")
    print(f"Shallow Copy (AFFECTED because inner reference shared): {shallow_arr}")
    print(f"Deep Copy    (ISOLATED because inner element duplicated): {deep_arr}")


# ==============================================================================
# EXECUTION
# ==============================================================================
if __name__ == "__main__":
    demonstrate_scalar_copy()
    demonstrate_composite_copy()