import os
import shutil

import matplotlib
import matplotlib.pyplot

FONT_NAME = 'Noto Sans CJK SC'
target_font_path = os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf')
origin_font_path = os.path.join(os.path.pardir, 'fonts', 'noto')
target_font_list = os.listdir(target_font_path)
rebuild = False
for font in os.listdir(origin_font_path):
    if font not in target_font_list:
        shutil.copy(os.path.join(origin_font_path, font), os.path.join(target_font_path, font))
        rebuild = True

matplotlib.rcParams['font.family'] = ['sans-serif']
matplotlib.rcParams['font.sans-serif'] = [FONT_NAME]
if rebuild:
    matplotlib.font_manager._rebuild()