import os
import shutil

import matplotlib
import matplotlib.pyplot


def apply_font(path, name):
    target_font_path = os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf')
    target_font_list = os.listdir(target_font_path)
    rebuild = False
    for font in os.listdir(path):
        if font not in target_font_list:
            shutil.copy(os.path.join(path, font), os.path.join(target_font_path, font))
            rebuild = True
    matplotlib.rcParams['font.family'] = ['sans-serif']
    matplotlib.rcParams['font.sans-serif'] = [name]
    if rebuild:
        matplotlib.font_manager._rebuild()
