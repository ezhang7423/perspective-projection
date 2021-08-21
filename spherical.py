import math
import numpy as np


def spherical_to_image(phi, theta, focal_length):
    """spherical to (x, y, z) on image plane

    :param phi: [description]
    :type phi: [type]
    :param theta: [description]
    :type theta: [type]
    :param focal_length: [description]
    :type focal_length: [type]
    :return: [description]
    :rtype: [type]
    """
    x = math.tan(math.pi / 2 - phi)
    return focal_length * np.asarray([x, math.tan(theta) / math.sin(phi), -1])


def cartesian_to_image(x, y, z, focal_length):
    return (
        -1
        * np.asarray(
            [
                [focal_length / z, 0, 0, 0],
                [0, focal_length / z, 0, 0],
                [0, 0, 1 / z, 0],
            ]
        )
        @ np.asarray([x, y, z, 1])
    )


def cartesian_to_spherical(x, y, z):
    """return (phi, theta) (disregard r)

    :param x: [description]
    :type x: [type]
    :param y: [description]
    :type y: [type]
    :param z: [description]
    :type z: [type]
    """
    assert z <= -1
    proj_length = math.sqrt(x ** 2 + z ** 2)
    # print(math.atan(y / proj_length))
    return (
        math.acos(x / proj_length),
        math.atan(y / proj_length),
    )
