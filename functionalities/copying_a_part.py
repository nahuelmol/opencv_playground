import cv2

def init_function():
	img = cv2.imread('assets/MichaelSchumacher.jpg',-1)
	
	tag = img[0:300,500:800]
	img[420:720,980:1280] = tag

	img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
	
	cv2.imshow('Image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()