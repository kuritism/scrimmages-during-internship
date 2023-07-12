import pygame, numpy


def greyscale(surface: pygame.Surface):
    arr = pygame.surfarray.array3d(surface)
    # calulates the avg of the "rgb" values, this reduces the dim by 1
    mean_arr = numpy.mean(arr, axis=2)
    # restores the dimension from 2 to 3
    mean_arr3d = mean_arr[..., numpy.newaxis]
    # repeat the avg value obtained before over the axis 2
    new_arr = numpy.repeat(mean_arr3d[:, :, :], 3, axis=2)
    # return the new surface
    return pygame.surfarray.make_surface(new_arr)
