import unittest

import matplotlib
import matplotlib.pyplot as plt


def simple_plot():
    plt.plot([1, 2], [3, 4])
    plt.title("标题测试-abc-123", fontsize=20)
    plt.show()


class TestFonts(unittest.TestCase):

    def test_noto(self):
        import mpl_font.noto
        simple_plot()

    def test_wqy(self):
        import mpl_font.wqy
        simple_plot()

    def test_msyh(self):
        import mpl_font.msyh
        simple_plot()

    def test_set(self):
        import mpl_font.noto
        matplotlib.rcParams['font.sans-serif'] = ['Fangsong']
        simple_plot()
        mpl_font.noto.set()
        simple_plot()
