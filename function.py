import cv2 as cv
import numpy as np
from area_plot import room_plot

# Extra Parameters
# canvas of same size as roi frame
canvas_l = np.zeros((400, 400,3), dtype = np.uint8)
canvas_r = np.zeros((400, 400,3), dtype = np.uint8)
canvas_j = np.zeros((400, 800,3), dtype = np.uint8)

# Source and destination points for homography
dst_points = np.array([[0,0], [399,0], [399,399], [0,399]], dtype = 'float')
src_right = np.array([[0,50],[169,70],[355,355],[0,398]], dtype= 'float')
src_left = np.array([[235,62],[399,61],[399,399],[100,399]], dtype= 'float')

# create background subtractor object
bg_sub = cv.createBackgroundSubtractorKNN(history=1)

# Function to crop region of interest and give two cropped images.
def roi_frame(frame):
    """
    This function takes a frame and return to frames of the area of ROI.
    Input: frame/image
    Output: Two frame/images
    """

    left_frame = frame[20:200, 26:320]
    right_frame = frame[20:200, 325:627]

    # Resize the frame to 400, 400
    left_frame = cv.resize(left_frame, (400,400))
    right_frame = cv.resize(right_frame, (400,400))

    return left_frame, right_frame

# Function to give warped Perespective image.
def warped_frame(frame, frame_type):
    """
    This function takes an image and type of images and give warped frame using homography
    """
    if frame_type == "left":
        h, status = cv.findHomography(src_left, dst_points)
        frame_warped = cv.warpPerspective(frame, h, (400, 400))
    elif frame_type == "right":
        h, status = cv.findHomography(src_right, dst_points)
        frame_warped = cv.warpPerspective(frame, h, (400, 400))

    return frame_warped

# function to stack two frame to create 1 frame.
def join_frame(frame1, frame2):
    """
    This function will join two images on an empty canvas
    """

    canvas_j[0:400, 0:400] = frame1
    canvas_j[0:400, 400::] = frame2

    return canvas_j

# Function to display movements on area plot.
def movement_mapping(frame, plot= room_plot):

    frame_mask= bg_sub.apply(frame)
    # Get contours and center point of each contour
    contours, hierarchy = cv.findContours(frame_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        area = cv.contourArea(cnt)

        if area >= 1000:

            # Get center point of the contours.
            M = cv.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            cv.circle(plot, (cx,cy), 5, (0, 100, 255), -1)

    return plot
    
        

        
    
