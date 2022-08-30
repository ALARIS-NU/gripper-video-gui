#!/usr/bin/env python3
from ast import arg
import rospy
import os
from sensor_msgs.msg import Image
from std_msgs.msg import String
import cv2
from cv_bridge import CvBridge
from threading import *
import multiprocessing

# Instantiate CvBridge
bridge = CvBridge()
novideoimgpath = '/home/parallels/camGUI/src/webcam_control_gui/video-not-working.PNG'
cv2_img = cv2.imread(novideoimgpath, 0)
theimgsize = (320, 180)

def image_callback(msg):
    # print("Received an image!")
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        # print("converted...")
    except:
        print("CvBridgeError")
    else:
        # print("drawcall...")
        cv2.imshow("Display", cv2.resize(cv2_img, theimgsize))
        # cv2.waitKey(20)
        # print("drawen..")

def changeGoal(*args):
    global current_goal
    current_goal = args[1]

def gui():
    cv2.namedWindow("Display", cv2.WINDOW_AUTOSIZE)
    cv2.createButton("Close",closetheapp,None,cv2.QT_PUSH_BUTTON,0)
    cv2.createButton("Home",changeGoal,"Home",cv2.QT_PUSH_BUTTON,0)
    cv2.createButton("Bottle",changeGoal,"Bottle",cv2.QT_PUSH_BUTTON,0)
    cv2.createButton("Ball",changeGoal,"Ball",cv2.QT_PUSH_BUTTON,0)
    cv2.createButton("Cube",changeGoal,"Cube",cv2.QT_PUSH_BUTTON,0)
    cv2.imshow("Display", cv2.resize(cv2_img, theimgsize))
    cv2.waitKey()

def ros():
    rospy.init_node('theGuiNode')
    image_topic = "/webcam/image_raw"
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.on_shutdown(onshutdown)

    pub = rospy.Publisher('/the_gui/goal', String, queue_size=10)
    rate = rospy.Rate(60)
    while not rospy.is_shutdown():
        global current_goal
        pub.publish(current_goal)
        rate.sleep()
    

def onshutdown():
    print("onshutdown triggered...")
    cv2.destroyAllWindows()
    os._exit(0)

def closetheapp(*args):
    print("closetheapp pressed...")
    rospy.signal_shutdown("manual exit using button")
    onshutdown()

if __name__ == '__main__':
    global current_goal
    current_goal = "Ready"
    t1=Thread(target=gui)
    t1.start() 
    ros()
    
    
    
    