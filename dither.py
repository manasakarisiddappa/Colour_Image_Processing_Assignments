import numpy as np
import matplotlib.pyplot as plt
import cv2

def dither(image):
	gr = [1,2,0,0,2,3,0,3,3,1]; rd = [0,1,2,1,3,3,1,0,3,0]; bl = [3,2,2,2,1,1,2,0,0,2,1,3]
	
	cim = np.zeros((image.shape[0]*4,image.shape[1]*4,3))
	for x,i in zip(range(image.shape[0]),range(0,cim.shape[0],4)):
		for y,j in zip(range(image.shape[1]),range(0,cim.shape[1],4)):
			for k in range(image.shape[2]):
				pix = image[x,y,k]
				if k == 0:
					dot = np.array([255,0,0])
					if pix >= 0 and pix <= 42:
						cim[i+bl[0],j+bl[1]] = dot 
					elif pix >= 43 and pix <= 85:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
					elif pix >= 86 and pix <= 128:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
						cim[i+bl[4],j+bl[5]] = dot
					elif pix >= 129 and pix <= 171:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
						cim[i+bl[4],j+bl[5]] = dot
						cim[i+bl[6],j+bl[7]] = dot
					elif pix >= 172 and pix <= 214:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
						cim[i+bl[4],j+bl[5]] = dot
						cim[i+bl[6],j+bl[7]] = dot
						cim[i+bl[8],j+bl[9]] = dot
					elif pix >= 215 and pix <= 255:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
						cim[i+bl[4],j+bl[5]] = dot
						cim[i+bl[6],j+bl[7]] = dot
						cim[i+bl[8],j+bl[9]] = dot
						cim[i+bl[10],j+bl[11]] = dot

				if k == 1:
					dot = [0,255,0]
					if pix >= 0 and pix <= 50:
						cim[i+gr[0],j+gr[1]] = dot
					elif pix >= 51 and pix <= 101:
						cim[i+gr[0],j+gr[1]] = dot
						cim[i+gr[2],j+gr[3]] = dot
					elif pix >= 102 and pix <= 152:
						cim[i+gr[0],j+gr[1]] = dot
						cim[i+gr[2],j+gr[3]] = dot
						cim[i+gr[4],j+gr[5]] = dot
					elif pix >= 153 and pix <= 203:
						cim[i+gr[0],j+gr[1]] = dot
						cim[i+gr[2],j+gr[3]] = dot
						cim[i+gr[4],j+gr[5]] = dot
						cim[i+gr[6],j+gr[7]] = dot
					elif pix >= 204 and pix <= 255:
						cim[i+gr[0],j+gr[1]] = dot
						cim[i+gr[2],j+gr[3]] = dot
						cim[i+gr[4],j+gr[5]] = dot
						cim[i+gr[6],j+gr[7]] = dot
						cim[i+gr[8],j+gr[9]] = dot

				if k == 2:
					dot = [0,0,255]
					if pix >= 0 and pix <= 50:
						cim[i+rd[0],j+rd[1]] = dot
					elif pix >= 51 and pix <= 101:
						cim[i+rd[0],j+rd[1]] = dot
						cim[i+rd[2],j+rd[3]] = dot
					elif pix >= 102 and pix <= 152:
						cim[i+rd[0],j+rd[1]] = dot
						cim[i+rd[2],j+rd[3]] = dot
						cim[i+rd[4],j+rd[5]] = dot
					elif pix >= 153 and pix <= 203:
						cim[i+rd[0],j+rd[1]] = dot
						cim[i+rd[2],j+rd[3]] = dot
						cim[i+rd[4],j+rd[5]] = dot
						cim[i+rd[6],j+rd[7]] = dot
					elif pix >= 204 and pix <= 255:
						cim[i+rd[0],j+rd[1]] = dot
						cim[i+rd[2],j+rd[3]] = dot
						cim[i+rd[4],j+rd[5]] = dot
						cim[i+rd[6],j+rd[7]] = dot
						cim[i+rd[8],j+rd[9]] = dot


	return np.asarray( cim, dtype="uint8" )

def cmydither(image):
	gr = [1,2,0,0,2,3,0,3,3,1]; rd = [0,1,2,1,3,3,1,0,3,0]; bl = [3,2,2,2,1,1,2,0,0,2,1,3]
	cim = np.zeros((image.shape[0]*4,image.shape[1]*4,3))
	cim.fill(255)
	for x,i in zip(range(image.shape[0]),range(0,cim.shape[0],4)):
		for y,j in zip(range(image.shape[1]),range(0,cim.shape[1],4)):
			for k in range(image.shape[2]):
				pix = 255 - image[x,y,k]
				if k == 0:
					dot = np.array([0,255,255])
					if pix >= 0 and pix <= 42:
						cim[i+bl[0],j+bl[1]] = dot 
					elif pix >= 43 and pix <= 85:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
					elif pix >= 86 and pix <= 128:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
						cim[i+bl[4],j+bl[5]] = dot
					elif pix >= 129 and pix <= 171:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
						cim[i+bl[4],j+bl[5]] = dot
						cim[i+bl[6],j+bl[7]] = dot
					elif pix >= 172 and pix <= 214:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
						cim[i+bl[4],j+bl[5]] = dot
						cim[i+bl[6],j+bl[7]] = dot
						cim[i+bl[8],j+bl[9]] = dot
					elif pix >= 215 and pix <= 255:
						cim[i+bl[0],j+bl[1]] = dot
						cim[i+bl[2],j+bl[3]] = dot
						cim[i+bl[4],j+bl[5]] = dot
						cim[i+bl[6],j+bl[7]] = dot
						cim[i+bl[8],j+bl[9]] = dot
						cim[i+bl[10],j+bl[11]] = dot

				if k == 1:
					dot = [255,0,255]
					if pix >= 0 and pix <= 50:
						cim[i+gr[0],j+gr[1]] = dot
					elif pix >= 51 and pix <= 101:
						cim[i+gr[0],j+gr[1]] = dot
						cim[i+gr[2],j+gr[3]] = dot
					elif pix >= 102 and pix <= 152:
						cim[i+gr[0],j+gr[1]] = dot
						cim[i+gr[2],j+gr[3]] = dot
						cim[i+gr[4],j+gr[5]] = dot
					elif pix >= 153 and pix <= 203:
						cim[i+gr[0],j+gr[1]] = dot
						cim[i+gr[2],j+gr[3]] = dot
						cim[i+gr[4],j+gr[5]] = dot
						cim[i+gr[6],j+gr[7]] = dot
					elif pix >= 204 and pix <= 255:
						cim[i+gr[0],j+gr[1]] = dot
						cim[i+gr[2],j+gr[3]] = dot
						cim[i+gr[4],j+gr[5]] = dot
						cim[i+gr[6],j+gr[7]] = dot
						cim[i+gr[8],j+gr[9]] = dot

				if k == 2:
					dot = [255,255,0]
					if pix >= 0 and pix <= 50:
						cim[i+rd[0],j+rd[1]] = dot
					elif pix >= 51 and pix <= 101:
						cim[i+rd[0],j+rd[1]] = dot
						cim[i+rd[2],j+rd[3]] = dot
					elif pix >= 102 and pix <= 152:
						cim[i+rd[0],j+rd[1]] = dot
						cim[i+rd[2],j+rd[3]] = dot
						cim[i+rd[4],j+rd[5]] = dot
					elif pix >= 153 and pix <= 203:
						cim[i+rd[0],j+rd[1]] = dot
						cim[i+rd[2],j+rd[3]] = dot
						cim[i+rd[4],j+rd[5]] = dot
						cim[i+rd[6],j+rd[7]] = dot
					elif pix >= 204 and pix <= 255:
						cim[i+rd[0],j+rd[1]] = dot
						cim[i+rd[2],j+rd[3]] = dot
						cim[i+rd[4],j+rd[5]] = dot
						cim[i+rd[6],j+rd[7]] = dot
						cim[i+rd[8],j+rd[9]] = dot


	return np.asarray( cim, dtype="uint8" )
				






im = cv2.imread('chamelion.jpg')
print(im.shape)
gr = dither(im)
resized = cv2.resize(gr, (im.shape[1],im.shape[0]), interpolation = cv2.INTER_AREA)
print(resized.shape)

nim = np.hstack((im,resized))
cv2.imshow('image',nim)
cv2.waitKey(0)

gr = cmydither(im)
print(gr.shape)
resized = cv2.resize(gr, (im.shape[1],im.shape[0]), interpolation = cv2.INTER_AREA)
print(resized.shape)
nim = np.hstack((im,resized))
cv2.imshow('image',nim)
cv2.waitKey(0)