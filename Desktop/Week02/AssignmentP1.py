import numpy as np
def rgb_to_grayscale(r: int, g: int, b: int) -> int:
    """Convert one RGB pixel to a rounded grayscale luminosity value."""
    luminosity = 0.299 * r + 0.587 * g + 0.114 * b
    return int(round(luminosity))

sample_result = rgb_to_grayscale(180, 120, 60)
print("Sample result:", sample_result)
assert sample_result == 131

# Extra test: equal channels should remain unchanged.
assert rgb_to_grayscale(80, 80, 80) == 80
print("Sample 1 passed.")