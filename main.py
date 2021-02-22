import cv2
from functionalities import random_colorizer

img = cv2.imread('assets/MichaelSchumacher.jpg',1)
img_gray_scale = cv2.imread('assets/MichaelSchumacher.jpg',0)

print(img.shape)

img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
img_gray_scale = cv2.resize(img_gray_scale,(0,0),fx=0.5,fy=0.5)

out_folder = 'out_images'

cv2.imwrite('{}\schumi.jpg'.format(out_folder),img)
cv2.imwrite('{}\schumi2.jpg'.format(out_folder),img_gray_scale)

print(img.shape)

random_colorizer.init_function()

cv2.imshow('Image',img_gray_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()
