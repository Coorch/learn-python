# 图像和办公文档处理
用程序来处理图像和办公文档经常出现在实际开发中，Python的标准库中虽然没有直接支持这些操作的模块，但我们可以通过Python生态圈中的第三方模块来完成这些操作。

## 20190713
### 操作图像
#### 计算机图像相关知识
1. 颜色。红绿蓝为色光三原色，通常将一个颜色表示为一个RGB值或RGBA值（其中A表示Alpha通道，决定了透过这个图像的像素，也就是透明度）。

|  名称  |RGBA值|名称|RGBA值|
| :------: | :------: |  :------: | :------: |
|White|(255,255,255,255)|Red|(255,0,0,255)|
|Green|(0,255,0,255)|Blue|(0,0,255,255)|
|Gray|(128,128,128,255)|Yellow|(255,255,0,255)|
|Black|(0,0,0,255)|Purple|(128,0,128,255)|

2. 像素。对于一个由数字序列表示的图像来说，最小的单位就是图像上单一颜色的小方格，这些小方块都有一个明确的位置和被分配的色彩数值，而这些小方格的颜色和位置决定了该图像最终呈现出来的样子，它们是不可分割的单位，我们通常称之为像素（pixel）。每一个图像都包含了一定量的像素，这些像素决定图像在屏幕上所呈现的大小

#### 用Pillow操作图像
Pillow是由著名的Python图像处理库PIL发展出来的一个分支，通过Pillow可以实现图像压缩和图像处理等各种操作。
安装命令如下
```Python
pip install pillow
```
Pillow中最为重要的是Image类，读取和处理图像都要通过这个类来完成。
```Python
from PIL import Image

image = Image.open(filename)
print(image.format, image.size, image.mode)
image.show()
```

1. 剪裁图像
```Python
image = Image.open(filename)
rect = 80, 20, 310, 360
image.crop(rect).show()
```
2. 生成缩略图
- iamge.thumbnail(size)
 
### 处理Excel电子表格
- openpyxl

### 处理Word文档
- python-docx