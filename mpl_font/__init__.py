import os

import matplotlib
import matplotlib.pyplot
from matplotlib import font_manager


def apply_font(path, name):
    if path != "":
        ttf_files = [ttf.fname for ttf in font_manager.fontManager.ttflist]
        for font in os.listdir(path):
            font_path = os.path.join(path, font)
            if font_path not in ttf_files:
                font_manager.fontManager.addfont(font_path)
    matplotlib.rcParams['font.family'] = ['sans-serif']
    matplotlib.rcParams['font.sans-serif'] = [name]


def set_font(name, font_dir):
    apply_font(os.path.join(os.path.dirname(__file__), 'fonts', font_dir), name)
