import numpy as np # linear algebra
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import math

class image:
    
    def __init__(self, img):
        input_type = type(img).__name__
        if input_type == "str":
            self.img = cv2.imread(img)
        elif input_type == "ndarray":
            self.img = img
        else:
            raise TypeError("invalid constructor, must be string path or cv2 image")
        self.height, self.width, self.channels = self.img.shape
        
    def display(self):
        # this plotting function expects BGR instead of RGB... 
        tmp = np.copy(self.img)
        tmp[:,:,0] = self.img[:,:,2]
        tmp[:,:,2] = self.img[:,:,0]
        plt.imshow(tmp)
        
    def show(self):
        cv2.imshow('image',self.img)

    def size(self):
        return self.height, self.width
    
    def minvalue(self):
        return self.img.mean(axis=2).amin()
    
    def maxvalue(self):
        return self.img.mean(axis=2).amax()
    
    def meanvalue(self):
        return self.img.mean()

    def blacknwhite(self):
        mean = self.meanvalue()
        result = np.zeros((self.height, self.width, 3), np.uint8)
        result[self.img >= mean] = 255
        return image(result)
    
    def pixelvalue(self, px): #Missing criteria
        return np.mean(px)
   
    def resize_nn(self, ratio):
        width, height = math.floor(self.width*ratio), math.floor(self.height*ratio)
        scale = 1/ratio
        result = np.zeros((height, width, 3), np.uint8)
        for i in range(height):
            for j in range(width):
                result[i,j] = self.img[int(round(i*scale)),int(round(j*scale))]
        return image(result)
    
    def resize_pixelreplication(self, ratio):
        width, height = math.floor(self.width*ratio), math.floor(self.height*ratio)
        scale = 1/ratio
        result = np.zeros((height, width, 3), np.uint8)
        for i in range(height):
            for j in range(width):
                result[i,j] = self.img[math.floor(i*scale),math.floor(j*scale)]
        return image(result)
        
    def resize_bl(self, ratio):
        width, height = math.floor(self.width*ratio), math.floor(self.height*ratio)
        scale = 1/ratio
        result = np.zeros((height, width, 3), np.uint8)
        for i in range(height):
            for j in range(width):
                x, y = j*scale, i*scale
                
                x1 = math.floor(x)
                x2 = math.ceil(x)
                y1 = math.floor(y)
                y2 = math.ceil(y)
                
                if x2 >= self.width:
                    x2 = self.width - 1
                if y2 >= self.height:
                    y2 = self.height - 1
                    
                dx1 = x - x1
                dx2 = x2 - x
                dy1 = y - y1
                dy2 = y2 - y
 
                if y1 == y2:
                    Ix1 = self.img[y1, x1]
                    Ix2 = self.img[y2, x2]
                else:
                    Ix1 = dy2 * self.img[y1, x1] + dy1 * self.img[y2, x1]
                    Ix2 = dy2 * self.img[y1, x2] + dy1 * self.img[y2, x2]
                
                if x1 == x2:
                    result[i,j] = np.around(Ix1, 0)
                else:
                    result[i,j] = np.around(dx1 * Ix2 + dx2 * Ix1, 0)
                
        return image(result)

    def resize_bc(self, ratio):
        width, height = math.floor(self.width*ratio), math.floor(self.height*ratio)
        scale = 1/ratio
        result = np.zeros((height, width, 3), np.uint8)
        C = np.zeros((4, 3), np.int)
        tmp = np.zeros(3, int)
        for i in range(height):
            for j in range(width):
                # coordinates in original image
                x, y = j*scale, i*scale
                x_int, y_int = math.floor(x), math.floor(y)
                dx, dy = x - x_int, y - y_int
                # interpolate each row
                for n in range(4):
                    tmp_y = y_int - 1 + n
                    a0 = self.getPixel(x_int,tmp_y)
                    d0 = self.getPixel(x_int - 1,tmp_y)
                    d2 = self.getPixel(x_int + 1,tmp_y)
                    d3 = self.getPixel(x_int + 2,tmp_y)
                    a1 = d0*(-0.5) + d2*(0.5)
                    a2 = d0 + a0*(-2.5) + d2*(2.0) + d3*(-0.5)
                    a3 = d0*(-0.5) + a0*(1.5) + d2*(-1.5) + d3*(0.5)
                    C[n] = a0 + a1*dx + a2*dx*dx + a3*dx*dx*dx
                # interpolate vertically
                a0 = C[1]
                d0 = C[0]
                d2 = C[2]
                d3 = C[3]
                a1 = d0*(-0.5) + d2*(0.5)
                a2 = d0 + a0*(-2.5) + d2*(2.0) + d3*(-0.5)
                a3 = d0*(-0.5) + a0*(1.5) + d2*(-1.5) + d3*(0.5)
                tmp = a0 + a1*dy + a2*dy*dy + a3*dy*dy*dy
                for n in range(3):
                    if tmp[n] < 0:
                        tmp[n] = 0
                    elif tmp[n] > 255:
                        tmp[n] = 255
                result[i, j] = tmp
                
        return image(result)  
    
    def getPixel(self, x, y):
        if (x < self.width) and (y < self.height):
            return self.img[y,x]
        else:
            return np.zeros(3, np.uint8)
        
    def grayScale(self, levels = 256):
        if levels > 256:
            levels = 256
        elif levels < 2:
            levels = 2
        c = 256/(levels-1)
        result = np.zeros((self.height, self.width, 3), np.uint8)
        for i in range(self.height):
            for j in range(self.width):
                value = self.pixelvalue(self.img[i,j])
                value = int(value/c)*int(c)
                result[i,j] = [value, value, value]
        return image(result)
    
    def interpolate(self, ratio, function = "bc"):
        if function == "nn":
            return img.resize_nn(ratio).resize_nn(1/ratio)
        elif function == "bl":
            return img.resize_bl(ratio).resize_bl(1/ratio)
        else:
            return img.resize_bc(ratio).resize_bc(1/ratio)
        
    def negative(self):
        result = np.zeros((self.height, self.width, 3), np.uint8)
        result = 255 - self.img
        return image(result)
    
    def save(self, name):
        cv2.imwrite(name,self.img)
        
    def hist(self):
        plt.hist(self.img.ravel(),256,[0,256])
        plt.show()   
        
    def adjust(self, x1, y1, x2, y2):
        result = np.zeros((self.height, self.width, 3), np.uint8)
        select = self.img.mean(axis=2) <= x1
        a = y1/x1
        result[select] = np.round(self.img[select] * a)
        select = np.logical_and(self.img.mean(axis=2) > x1, self.img.mean(axis=2) <= x2)
        a = (y2-y1)/(x2-x1)
        b = (y1-(x1 * a))
        result[select] = np.round((self.img[select] * a) + b)
        select = self.img.mean(axis=2) > x2
        a = (255-y2)/(255-x2)
        b = (y2-(x2 * a))
        result[select] = np.round((self.img[select] * a) + b)
        return image(result)
