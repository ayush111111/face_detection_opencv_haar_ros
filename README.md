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

-node_2 is used to display the Cropped image of face



![](https://github.com/ayush111111/face_detection_opencv_haar_ros/blob/master/Screenshot%20from%202020-03-28%2023-52-39.png)
-Trying to build a custom message that sends coordinates of detected face from node_1 to node_2 along with the Frame containing the face
In current version,the second node displays the cropped face from the frames that only contain the face and hence the actual image is not cropped and saved


1.1 )  Possible workarounds:

1.1.1 )
Subscribe to two different topics published by node_1 to node_2,one containing the Image and the other containing x,y,w,h.
Problems may arise while synchronizing the x,y.w.h(coordinates of detected face) and image data 
(possible solution :https://answers.ros.org/question/10223/how-to-synchronize-image-and-marker-display-between-two-ros-nodes/)

1.1.2 )
Instead of publishing to two different topic publish custom message to a single topic with image and coordinates
Problem arises while accessing Image data from custom message ( eg CvBridgeError: Unrecognized image encoding [] etc)
