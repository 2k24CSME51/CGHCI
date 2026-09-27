# TODO 1: Multiply width, height, and bpp, then divide by 8.
def display_memory_bytes(width: int, height: int, bpp: int) -> int:
    """Return image memory in bytes."""
    return (width * height * bpp) // 8


# TODO 2: Remove the # symbols and run the given test.
expected_bytes = 1920 * 1080 * 24 // 8
assert display_memory_bytes(1920, 1080, 24) == expected_bytes
print("Problem 4 passed")