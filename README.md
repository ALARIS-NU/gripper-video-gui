# Workspace to have a GUI with buttons and cam stream
## dependancies
* ~~libuvc_camera `sudo apt-get install ros-melodic-libuvc-camera`~~
* https://github.com/ros-drivers/video_stream_opencv

## How to run?
1. Publish camera by starting publisher node
* * `roslaunch fucking_webcam webcam.launch`
2. Run GUI
* * `rosrun webcam_control_gui webcam_control_gui.py`

## Limitations
> There is a problem with dependacies, so if you are using Ubuntu, there is a chance that due to copyright stuff the icons won't appear.
> Also there is a unknown problem with buttons that make them appear on separate window (press CTRL+P for button window)
Both of this problems are result of using ROS + Python + OpenCV. But alternative software may result in longer development time.

## How to use
* start the node
* open menu (CTRL+P)
* press needed buttons

## Screenshot
![Alt text](ss1.png?raw=true "Screenshot 1")

## Nodes
```Bash 
➜  ~ rostopic list
/rosout
/rosout_agg
/the_gui/goal
/webcam/camera_info
/webcam/image_raw
/webcam/image_raw/compressed
/webcam/image_raw/compressed/parameter_descriptions
/webcam/image_raw/compressed/parameter_updates
/webcam/image_raw/compressedDepth
/webcam/image_raw/compressedDepth/parameter_descriptions
/webcam/image_raw/compressedDepth/parameter_updates
/webcam/image_raw/theora
/webcam/image_raw/theora/parameter_descriptions
/webcam/image_raw/theora/parameter_updates
/webcam/webcam_image_view/output
/webcam/webcam_image_view/parameter_descriptions
/webcam/webcam_image_view/parameter_updates
/webcam/webcam_stream/parameter_descriptions
/webcam/webcam_stream/parameter_updates
```

## todo
* CLI args for sub/pub topics
* CLI args for img size

## references
* ~~https://msadowski.github.io/ros-web-tutorial-pt2-cameras/~~
* * ~~why the fuck this thing is shitty?~~
* ~~https://minhld.wordpress.com/2017/06/05/connect-usb-webcam-with-ros/~~
* * ~~this one is even shittier~~
* * ~~what the hell is `"file:///$(find your_camera_package)/config/your_camera.yaml"`~~
* https://github.com/ros-drivers/video_stream_opencv
* * this one is actually good