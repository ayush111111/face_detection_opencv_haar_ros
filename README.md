# face_detection_opencv_haar_ros


Task​ : Facial Detection using Haar Cascade
Create 2 ROS nodes, the first one should extract the webcam feed by creating an
Image Subscriber. Use facial detection on the subscribed feed by implementing Haar
Cascades using OpenCV. The frames with detected faces should be published to the
second ROS node, which crops the bounding box (detected face) from the Image
subscribed.

-usb_cam used to get data from webcam to node_1

-cv_bridge converts Image to needed form and this image is converted to b&w as classifier takes gray input 

-If the current frame has a face,it is published to node_2

-node_2 is used to display the Cropped image


![](https://github.com/ayush111111/face_detection_opencv_haar_ros/blob/master/Screenshot%20from%202020-03-28%2023-52-39.png)
