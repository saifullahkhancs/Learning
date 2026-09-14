# ==============================================================================
# DEFINITIONS: Advanced Generator Methods
# ==============================================================================
#
# Standard generators produce data via `yield`. Advanced generator methods 
# allow two-way communication and lifecycle control after execution starts:
#
# 1. generator.send(value):
#    - Sends `value` back into the generator where it last paused on a `yield`.
#    - The `yield` expression evaluates to `value`.
#    - Advances execution to the next `yield` and returns its produced value.
#    - Note: The first call MUST be `send(None)` or `next(gen)` to "prime" it.
#
# 2. generator.throw(type, value=None, traceback=None):
#    - Raises an exception inside the generator at the point where it is paused.
#    - If handled inside the generator (try/except), execution continues.
#    - If unhandled, the exception propagates up to the caller.
#
# 3. generator.close():
#    - Raises a `GeneratorExit` exception at the pause point.
#    - Used to terminate the generator cleanly.
#    - After calling `.close()`, further `next()` calls raise `StopIteration`.
# ==============================================================================


def advanced_coroutine():
    """Demonstrates handling input via .send(), handling errors via .throw(),
    and clean teardown via .close().
    """
    total = 0
    print("[Generator] Started and waiting for initial value...")
    
    try:
        while True:
            # Execution pauses here. When send(val) is called, val is assigned to 'value'.
            value = yield total
            
            if value is not None:
                print(f"[Generator] Received value: {value}")
                total += value

    except CustomGeneratorError:
        print("[Generator] CustomGeneratorError caught inside generator! Resetting total to 0.")
        total = 0
        yield total  # Resume yielding after handling exception

    except GeneratorExit:
        print("[Generator] GeneratorExit caught. Performing cleanup before closing...")
        # Clean teardown operations go here (e.g., closing files/sockets)


class CustomGeneratorError(Exception):
    """Custom exception used to demonstrate .throw()."""
    pass


# ==============================================================================
# EXECUTION & DEMONSTRATION
# ==============================================================================
if __name__ == "__main__":
    gen = advanced_coroutine()

    # --------------------------------------------------------------------------
    # 1. Priming and using .send()
    # --------------------------------------------------------------------------
    print("=== 1. USING .send() ===")
    # Step A: Prime the generator (advance to first yield)
    current_total = next(gen)
    print(f"[Caller] Initial yielded total: {current_total}")

    # Step B: Send data into the generator
    current_total = gen.send(10)
    print(f"[Caller] Updated total after send(10): {current_total}")

    current_total = gen.send(25)
    print(f"[Caller] Updated total after send(25): {current_total}")

    # --------------------------------------------------------------------------
    # 2. Injecting an exception using .throw()
    # --------------------------------------------------------------------------
    print("\n=== 2. USING .throw() ===")
    current_total = gen.throw(CustomGeneratorError)
    print(f"[Caller] Total after throw(): {current_total}")

    # Send another value to verify generator continues running
    current_total = gen.send(5)
    print(f"[Caller] Total after send(5): {current_total}")

    # --------------------------------------------------------------------------
    # 3. Terminating execution using .close()
    # --------------------------------------------------------------------------
    print("\n=== 3. USING .close() ===")
    gen.close()

    # Verifying generator is terminated
    try:
        next(gen)
    except StopIteration:
        print("[Caller] Confirmed: Generator is closed and raises StopIteration on next().")