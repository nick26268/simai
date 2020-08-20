#更改圖片大小為600x600

from PIL import Image

img = Image.open("bg.jpg")

resize_img = img.resize((600,600))

resize_img.save("bg.jpg")
