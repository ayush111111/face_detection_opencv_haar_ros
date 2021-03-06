#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

from face_detect.msg import rectan






def image_callback(image_msg):
	bridge= CvBridge()
        
        ros_img = image_msg

        cv_image = bridge.imgmsg_to_cv2(ros_img, "bgr8")        
              
        cv2.imshow('window_2', cv_image)

        if cv2.waitKey(1) & 0xFF == ord('q') :
         cv2.destroyAllWindows()
	
'''
def rect_callback(msg):

	x = msg.x
	y = msg.y
	w = msg.w
	h = msg.h

	cv_image = cv2.rectangle(cv_image,(x,y),(x+w,y+h),(255,0,0),2)
	
 	cv2.imshow('window_3', cv_image)
	


'''



if __name__ == '__main__':
    try :
         rospy.init_node('node_2')
         rospy.loginfo("node_2 started")
                 
         face_cascade = cv2.CascadeClassifier("/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml") 

         sub = rospy.Subscriber("/faces", Image, image_callback)
	 '''sub2 = rospy.Subscriber("/rectangle", rectan, rect_callback)'''	          
         rospy.spin()

    except rospy.ROSInterruptException :
         pass
