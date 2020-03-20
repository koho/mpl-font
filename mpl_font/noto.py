import os

from mpl_font import apply_font

FONT_NAME = 'Noto Sans CJK SC'

def set():
  apply_font(os.path.join(os.path.dirname(__file__), 'fonts', 'noto'), FONT_NAME)

set()
