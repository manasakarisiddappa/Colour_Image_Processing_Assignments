import numpy as np
import cv2



def gray(image):
	mask = np.array([[0,1],[1,2]])
	ngr = np.zeros((image.shape[0],image.shape[1]))
	x = mask.shape[0]
	y = mask.shape[1]
	for i in range(0,image.shape[0]-2,x):
		for j in range(0,image.shape[1]-2,y):

			temp = image[i:i+x,j:j+y]
			for m in range(x):
				for n in range(y):
					ngr[i+m,j+n] = temp[m,n,mask[m][n]]
	
	return  np.asarray( ngr, dtype="uint8" )


def demosaic(gr):
	cim = np.zeros((gr.shape[0],gr.shape[1],3))
	mask = np.array([[0,1],[1,2]])
	x = mask.shape[0]
	y = mask.shape[1]
	for i in range(gr.shape[0]-x):
		for j in range(gr.shape[1]-y):
			twobytwo = gr[i:i+x,j:j+y]

			for k in range(0,3):
				tt = np.argwhere(mask == k).flatten()
				a = []
				for m in range(0,tt.shape[0]-2+1,2):
					p = tt[m]
					q = tt[m+1]
					a.append(twobytwo[p,q])

				cim[i,j,k] = np.sum(a)/(tt.shape[0]/2)
			mask = np.roll(mask,1,axis = 1)
		mask = np.roll(mask,1,axis = 0)

	return np.asarray( cim, dtype="uint8" )



im = cv2.imread('chamelion.jpg')
cv2.imshow('image',im)
cv2.waitKey(0)
gr = gray(im)
print(gr.shape)
cv2.imshow('image',gr)
cv2.waitKey(0)
cim = demosaic(gr)
cv2.imshow('image',cim)
cv2.waitKey(0)