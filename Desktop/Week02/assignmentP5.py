import numpy as np


# TODO 1: Write the two kernels, multiply them with the block, and add the results to get gx and gy.
def sobel_response(block: np.ndarray) -> tuple[float, float, float]:
    """Return gx, gy, and edge strength."""
    # Sobel kernels for horizontal (gx) and vertical (gy) gradients
    K_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)

    K_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

    # Element-wise multiply and sum to get gradients
    gx = float(np.sum(block * K_x))
    gy = float(np.sum(block * K_y))

    # Calculate magnitude / edge strength
    strength = float(np.sqrt(gx**2 + gy**2))

    return gx, gy, strength


problem_5_input = np.array(
    [[20, 20, 200], [20, 20, 200], [20, 20, 200]], dtype=np.float32
)

# TODO 2: Remove the # symbols and run the given test.
gx, gy, strength = sobel_response(problem_5_input)
assert gx == 720.0 and gy == 0.0
print("Problem 5 passed")