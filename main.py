import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from function import roi_frame, warped_frame, join_frame, movement_mapping
from area_plot import room_plot

# create named window
winName = "Object Mapping"
cv.namedWindow(winName)

# create a cap object to read the video frame.
path = "/Users/gauravsingh/Desktop/AI ENGINEER/Multiple Camera stitching and object mapping/[FairMOT] Multiple Object Tracking and Mapping the coordinates to map with two different cameras.mp4"
cap = cv.VideoCapture(path)
if not cap.isOpened():
    print("Issue while accessing the video file.")


frame_count = 0 # Frame count
canvas_output = np.zeros((800, 800,3), dtype = np.uint8) # canvas to display output
fourcc = cv.VideoWriter_fourcc('M','J','P','G') # Save output object
out = cv.VideoWriter('output.avi', fourcc, 20.0, (800,800)) # Save output object

# Main loop.
while True:
    frame_count += 1
    plot = room_plot

    # Read frame video capture object.
    has_frame, frame = cap.read()
    if not has_frame:
        print("No frame to read.")
        break

    # Crop the frame area of camera 1 and camera 2.
    left_frame, right_frame = roi_frame(frame)

    # Warped perspective frame.
    left_warped = warped_frame(left_frame, "left")
    right_warped = warped_frame(right_frame, "right")
    
    # combine both warped frames
    frame_combine = join_frame(left_warped, right_warped)

    # Plot area of movement on room plot.
    room_map = movement_mapping(frame, plot)
    room_map = cv.resize(room_map, (800,400))

    # add input camera to canvas
    canvas_output[0:400,0:400] = left_frame
    canvas_output[0:400, 400:800] = right_frame
    canvas_output[400:800, 0:800] = room_map

    cv.putText(canvas_output, "Input: Camera 1", (100,50), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),2,cv.LINE_AA)
    cv.putText(canvas_output, "Input: Camera 1", (490,50), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),2,cv.LINE_AA)
    cv.putText(canvas_output, "Mapping - Multi Camera", (300,470), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),1,cv.LINE_AA)
   
    
    # Display frame.
    cv.imshow(winName,canvas_output)
    key = cv.waitKey(1)

    # Break the loop if user press 'q', 'Q' or esc key.
    if key == ord('q') or key == ord('Q') or key == 27:
        print("Video ended by user.")
        break
    # Save the frame.
    out.write(canvas_output)

cap.release()
cv.destroyAllWindows()
