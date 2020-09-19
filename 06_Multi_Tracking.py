#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import Libraries
import cv2
import sys
from random import randint


# Tracker Types
tracker_types = ['BOOSTING',
                'MIL',
                'KCF',
                'TLD',
                'MEADIANFLOW',
                'GOTURN',
                'MOSSE',
                'CSRT']

# Define trackers by name
def tracker_name(tracker_types):

    # Create trackers by name with if statement
    if tracker_types == tracker_types[0]:
        tracker = cv2.TrackerBoosting_create()
    elif tracker_types == tracker_types[1]:
        tracker = cv2.TrackerMIL_create()
    elif tracker_types == tracker_types[2]:
        tracker = cv2.TrackerKFC_create()
    elif tracker_types == tracker_types[3]:
        tracker = cv2.TrackerTLD_create()
    elif tracker_types == tracker_types[4]:
        tracker = cv2.TrackerMedianFlow_create()
    elif tracker_types == tracker_types[5]:
        tracker = cv2.TrackerGOTURN_create()
    elif tracker_types == tracker_types[6]:
        tracker = cv2.TrackerMOSSE_create()
    elif tracker_types == tracker_types[7]:
        tracker = cv2.TrackerCSRT_create()
                                           

    # else statement
    else:
        tracker = None
        print('No tracker found')
        print('Choose from these trackers: ')
        for tr in tracker_types:
            print(tr)
    
    # return
    return tracker

if __name__ == '__main__':
    print("Default tracking algorithm MOSSE \n"
         "Available algorithms are: \n")
    for tr in tracker_types:
        print(tr)
    
        
#    trackerType = 'MOSSE'
    trackerType = 'MOSSE'

    # Create a video capture
    cap = cv2.VideoCapture('Video/Vehicles.mp4')
    
    # Read first frame
    success, frame = cap.read()
    
    # Quit if failure
    if not success:
        print('Cannot read the vedio')
    
    # Select boxes and colors
    rects = []
    colors = []

    # While loop
    while True:
        
    
        # draw rectangles, select ROI, open new window
        rect_box = cv2.selectROI('MultiTracker',frame)
        rects.append(rect_box)
        colors.append((rabdint(64,255), rabdint(64,255), rabdint(64,255)))
        print('Press q to stop selecting boxes and start multitracking')
        print('Press any key to select another box')
        
        
        
        #close window
        if cv2.waitKey(0) & 0xFF == 113:
            break
        
    # print message
    print(f'Selected boxes {rects}')
    
    
    # Create multitracker
    multitracker = cv2.MultiTracker_create()
    
    
    # Initialize multitracker
    for rect_box in rects:
        multitracker.add(tracker_name(tracker_types),
                        frame,
                        rect_box)
    
    #Video and Tracker
    # while loop
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        # update location objects
        success, boxes = multitracker.update(frame)
        
        # draw the objectes tracked
        for i, nwebox in enumerate(boxes):
            pts1 = (int(newbox[0]),
                   int(newboxe[1]))
            pts2 = (int(newbox[0] + newbox[2]),
                   int(newbox[1] + newbox[3]))
            cv2.rectangle(frame,
                         pts1,
                         pts2,
                         colors[i],
                         2,
                         1)
            
            
        # display frame
        cv2.imshow('MultiTracker', frame)
    
        # Close the frame
        if cv2.waitKey(20) & 0xFF == 27:
            break
    
# Release and Destroy
cap.release()
cv2.destroyAllWindowa()


# In[ ]:




