from PIL import Image

#get file path
filepath = "images\dice4.png"
img = Image.open(filepath)

width = img.width
height = img.height


left = 6
top = height / 4
right = 174
bottom = 3 * height / 4
img1 = img.crop((left, top, right, bottom))
new_size = (200, 200)
img1 = img1.resize(new_size) 

print('The heigth of image is:', height)
print('The width of image is:', width)