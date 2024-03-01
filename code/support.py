import pygame
from os import walk
from os.path import join


def import_folder(path):
    surface_list = []

    for dir_name, __, img_files in walk(path):
        for img_name in img_files:
            full_path = join(dir_name, img_name)
            surface_list.append(pygame.image.load(full_path).convert_alpha())

    return surface_list


def import_folder_dict(path):
    surface_dict = {}

    for dir_name, __, img_files in walk(path):
        for img_name in img_files:
            full_path = join(dir_name, img_name)
            surface_dict[img_name.split('.')[0]] = pygame.image.load(
                full_path).convert_alpha()

    return surface_dict
