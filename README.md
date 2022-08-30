# Workspace to have a GUI with buttons and cam stream
## dependancies
* ~~libuvc_camera `sudo apt-get install ros-melodic-libuvc-camera`~~
* https://github.com/ros-drivers/video_stream_opencv

## Nodes
```Bash 
➜  ~ rostopic list
/rosout
/rosout_agg
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

## references
* ~~https://msadowski.github.io/ros-web-tutorial-pt2-cameras/~~
* * ~~why the fuck this thing is shitty?~~
* ~~https://minhld.wordpress.com/2017/06/05/connect-usb-webcam-with-ros/~~
* * ~~this one is even shittier~~
* * ~~what the hell is `"file:///$(find your_camera_package)/config/your_camera.yaml"`~~
* https://github.com/ros-drivers/video_stream_opencv
* * this one is actually good