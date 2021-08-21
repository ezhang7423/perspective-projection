from spherical import *
from numpy import allclose

MAX_BOUND = int(1e2)
MIN_BOUND = -MAX_BOUND


def test_hypothesis():
    print(
        f"Testing all values from ({MIN_BOUND} to {MAX_BOUND}, {MIN_BOUND} to {MAX_BOUND}, -1 to 10)"
    )
    focal_length = 1
    for z in range(-1, -11, -1):
        print("Depth at", z)
        for x in range(MIN_BOUND, MAX_BOUND):
            for y in range(MIN_BOUND, MAX_BOUND):

                point = [x, y, z]

                c2i = cartesian_to_image(*point, focal_length)

                s2i = spherical_to_image(*cartesian_to_spherical(*point), focal_length)
                assert allclose(c2i, s2i)

    print("Successfully passed")


    
if __name__ == "__main__":
    test_hypothesis()
