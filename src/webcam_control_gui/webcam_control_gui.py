#!/usr/bin/env python3
from ast import arg
from time import sleep
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
        cv2.imshow("Press CTLR+P for buttons", cv2.resize(cv2_img, theimgsize))
        # cv2.waitKey(20)
        # print("drawen..")

def changeGoal(*args):
    pub.publish(args[1])

def gui():
    cv2.namedWindow("Press CTLR+P for buttons", cv2.WINDOW_AUTOSIZE)
    cv2.createButton("Close",closetheapp,None,cv2.QT_PUSH_BUTTON,0)
    cv2.createButton("Home",changeGoal,"Home",cv2.QT_PUSH_BUTTON,0)
    cv2.createButton("Bottle",changeGoal,"Bottle",cv2.QT_PUSH_BUTTON,0)
    cv2.createButton("Ball",changeGoal,"Ball",cv2.QT_PUSH_BUTTON,0)
    cv2.createButton("Cube",changeGoal,"Cube",cv2.QT_PUSH_BUTTON,0)
    cv2.imshow("Press CTLR+P for buttons", cv2.resize(cv2_img, theimgsize))
    cv2.waitKey()

def ros():
    rospy.init_node('theGuiNode')
    image_topic = "/webcam/image_raw"
    rospy.Subscriber(image_topic, Image, image_callback)
    rospy.on_shutdown(onshutdown)
    global pub
    global statusPub
    pub = rospy.Publisher('/the_gui/goal', String, queue_size=10)
    statusPub =  rospy.Publisher('/the_gui/status', String, queue_size=10)
    sleep(0.1)
    statusPub.publish("Ready")

def onshutdown():
    global pub
    statusPub.publish("Closing")
    print("onshutdown triggered...")
    cv2.destroyAllWindows()
    os._exit(0)

def closetheapp(*args):
    print("closetheapp pressed...")
    rospy.signal_shutdown("manual exit using button")
    onshutdown()

if __name__ == '__main__':
    t1=Thread(target=gui)
    t1.start() 
    ros()
    
    
    
    