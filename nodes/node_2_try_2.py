#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from face_detect.msg import rectan

class listener :
	def __init__(self) :

		self.sub = rospy.Subscriber("/faces", Image, self.image_callback,queue_size = 10)
		self.sub2 = rospy.Subscriber("/rectangle", rectan, self.rect_callback)
		self.bridge = CvBridge()	
		rospy.loginfo("node_2 started")	
		self.cv_image = None
		

				 
  	
	def rect_callback(self,rectangle):

		self.x = int(rectangle.x)
		self.y = int(rectangle.y)
		self.w = int(rectangle.w)
		self.h = int(rectangle.h)




	def image_callback(self,data):
	
		self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8") 


		rec_image = cv2.rectangle(self.cv_image,(self.x,self.y),(self.x+self.w,self.y+self.h),(255,0,0),2)
		
		roi_color = rec_image[self.y:self.y+self.h, self.x:self.x+self.w]

		cv2.imshow('window_3', roi_color)		 		
        	if cv2.waitKey(1) & 0xFF == ord('q') :
         		cv2.destroyAllWindows()
		
		


if __name__ == '__main__':
    try :
         rospy.init_node('node_2')

         listener_inst = listener()

         rospy.spin()

    except rospy.ROSInterruptException :
         pass














