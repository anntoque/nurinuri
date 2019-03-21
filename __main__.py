from os import path
import numpy as np
from cv2 import imread, floodFill, imshow, imwrite, waitKey, destroyAllWindows
from PIL.ImageColor import getrgb

# 画像読み込み
pic = imread(path.join(path.dirname(__file__), 'nurinuri.png'), flags=9)
flooded = pic.copy()

# 数値を読み込む番号で

# 枠の座標を読み込む

# ヒートマップの色指定

# 画像の枠内に色を塗る
floodFill(flooded, None, (300,300), newVal=(255, 0, 0))
floodFill(flooded, None, (100,100), newVal=(255, 255, 0))

# 画像を保存
imwrite('test.png', flooded)
