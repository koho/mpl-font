import os

from mpl_font import apply_font

FONT_NAME = 'WenQuanYi Micro Hei'

def set():
  apply_font(os.path.join(os.path.dirname(__file__), 'fonts', 'wqy'), FONT_NAME)
  
set()
