import numpy as np
import cv2


def floyddiffuse(image):
	cim = image.copy()
	tmp = 0
	for i in range(0,cim.shape[0]-1):
		for j in range(0,cim.shape[1]):
			if cim[i,j] <= 127:
				tmp = cim[i,j] - 0
				cim[i,j] = 0
			if cim[i,j] > 127:
				tmp = cim[i,j] - 255
				cim[i,j] = 255

			if j == 0:
				cim[i,j+1] = np.clip(cim[i,j+1]+tmp*(7/16),0,255)
				cim[i+1,j+1] = np.clip(cim[i+1,j+1]+tmp*(1/16),0,255)
				cim[i+1,j] = np.clip(cim[i+1,j]+tmp*(5/16),0,255)

			elif j == cim.shape[1]-1:
				cim[i+1,j] = np.clip(cim[i+1,j]+tmp*(5/16),0,255)
				cim[i+1,j-1] = np.clip(cim[i+1,j-1]+tmp*(3/16),0,255)
			
			else:
				cim[i,j+1] = np.clip(cim[i,j+1]+tmp*(7/16),0,255,)
				cim[i+1,j+1] = np.clip(cim[i+1,j+1]+tmp*(1/16),0,255)
				cim[i+1,j] = np.clip(cim[i+1,j]+tmp*(5/16),0,255)
				cim[i+1,j-1] = np.clip(cim[i+1,j-1]+tmp*(3/16),0,255)

	return cim


def owndiffuse(image):
	cim = image.copy()
	tmp = 0
	for i in range(0,cim.shape[0]-1):
		for j in range(0,cim.shape[1]):
			if cim[i,j] <= 127:
				tmp = cim[i,j] - 0
				cim[i,j] = 0
			if cim[i,j] > 127:
				tmp = cim[i,j] - 255 
				cim[i,j] = 255

			if j == 0:
				cim[i,j+1] = np.clip(cim[i,j+1]+tmp*(7/29),0,255)
				cim[i+1,j+1] = np.clip(cim[i+1,j+1]+tmp*(4/29),0,255)
				cim[i+1,j] = np.clip(cim[i+1,j]+tmp*(9/29),0,255)

			elif j == cim.shape[1]-1:
				cim[i+1,j] = np.clip(cim[i+1,j]+tmp*(9/29),0,255)
				cim[i+1,j-1] = np.clip(cim[i+1,j-1]+tmp*(9/29),0,255)

			else:
				cim[i,j+1] = np.clip(cim[i,j+1]+tmp*(7/29),0,255)
				cim[i+1,j+1] = np.clip(cim[i+1,j+1]+tmp*(4/29),0,255)
				cim[i+1,j] = np.clip(cim[i+1,j]+tmp*(9/29),0,255)
				cim[i+1,j-1] = np.clip(cim[i+1,j-1]+tmp*(9/29),0,255)

	return cim

im = cv2.imread('ed-eg.png')
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
print(im.shape)
cv2.imshow('image',im)
cv2.waitKey(0)

gr = floyddiffuse(im)
print(gr.shape)
cv2.imshow('image',gr)
cv2.waitKey(0)

gr = owndiffuse(im)
print(gr.shape)
cv2.imshow('image',gr)
cv2.waitKey(0)