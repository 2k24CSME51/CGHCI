import numpy as np

def adjust_brightness_contrast(image: np.ndarray, alpha: float, beta: float) -> np.ndarray:
    """Apply O = alpha * I + beta and clip the result to [0, 255]."""
    image_float = image.astype(np.float32)
    adjusted = alpha * image_float + beta
    return np.clip(adjusted, 0, 255).astype(np.uint8)

sample_image = np.array([[100, 150], [200, 50]], dtype=np.uint8)
sample_output = adjust_brightness_contrast(sample_image, alpha=1.5, beta=-20)
expected_output = np.array([[130, 205], [255, 55]], dtype=np.uint8)
np.testing.assert_array_equal(sample_output, expected_output)
print(sample_output)

# Extra test: a large positive beta must clip at 255.
extra = adjust_brightness_contrast(np.array([[240]], dtype=np.uint8), alpha=1.0, beta=30)
assert extra[0, 0] == 255
print("Sample 2 passed.")