import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# create a black canvas of size 800, 400, 3
canvas = np.ones((400, 800, 3), dtype = np.uint8)
canvas[:,:,:] = (202,228,246)

x = 40
for i in range(0, 20):
    cv.line(canvas, (x,0),(x,400), (0,0,0),1)
    x+= 40
y = 40
for i in range(0, 10):
    cv.line(canvas, (0,y),(800,y), (0,0,0),1)
    y += 40

cv.rectangle(canvas, (350,175), (450,225), (61, 121, 160),-1)
cv.rectangle(canvas, (120,100), (680, 150), (61, 121, 160),-1)
cv.rectangle(canvas, (120,150), (175, 250), (61, 121, 160),-1)
cv.rectangle(canvas, (120,250), (680,300), (61, 121, 160),-1)
cv.rectangle(canvas, (615,150), (680,250), (61, 121, 160),-1)
cv.rectangle(canvas, (40,25), (760,65), (61, 121, 160),-1)
cv.rectangle(canvas, (40,340), (760,380), (61, 121, 160),-1)
cv.rectangle(canvas, (40,60), (100,345), (61, 121, 160),-1)
cv.rectangle(canvas, (700,60), (760,345), (61, 121, 160),-1)
cv.rectangle(canvas, (120,280), (180,399), (69,69,69),-1)
cv.rectangle(canvas, (180,325), (200,395), (102,75,75),-1)
cv.rectangle(canvas, (400,0), (680,15), (102,75,75),-1)
cv.rectangle(canvas, (780,45), (799,360), (102,75,75),-1)

canvas = cv.resize(canvas, (600,200))
room_plot = canvas


