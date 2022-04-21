# Mpl-Font

A CJK font selector for matplotlib to display CJK characters in an easy way.

## Supported Fonts
- Noto Sans CJK SC
- WenQuanYi Micro Hei
- Microsoft YaHei

## Install
```shell script
pip install mpl-font
```

## Usage
Just import the font you want to use, such as
```python
import mpl_font.noto # For Noto Sans CJK SC
import mpl_font.wqy # For WenQuanYi Micro Hei
import mpl_font.msyh # For Microsoft YaHei
```
Then matplotlib should be able to display CJK characters.

If the font is already imported but overwritten by others, you need to explicitly call the `set` method of the font:

```python
mpl_font.noto.set()
```
