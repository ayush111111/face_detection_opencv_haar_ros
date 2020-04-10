#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from face_detect.msg import rectan

def image_callback(img):

        bridge= CvBridge()

        cv_image = bridge.imgmsg_to_cv2(img, "bgr8")
   
	gray=cv2.cvtColor(cv_image,cv2.COLOR_BGR2GRAY)

	faces=face_cascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=4)

        for (x,y,w,h) in faces:
            rec = rectan()
            rec.x=x
            rec.y=y
            rec.w=w
            rec.h=h

            pub2.publish(rec)
            '''cv_image = cv2.rectangle(cv_image,(x,y),(x+w,y+h),(255,0,0),2)
            roi_color = cv_image[y:y+h, x:x+w]'''
                  
        if len(faces) > 0 :
            ros_image = bridge.cv2_to_imgmsg(cv_image, "bgr8")  
          
            pub.publish(ros_image)
                  

if __name__ == '__main__':
    try :
         rospy.init_node('node_1')

         rospy.loginfo("node_1 started")
                 
         face_cascade = cv2.CascadeClassifier("/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml") 

         sub = rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
      
         pub=rospy.Publisher("/faces", Image, queue_size=10) 
         pub2=rospy.Publisher("/rectangle", rectan)

         rospy.spin()

    except rospy.ROSInterruptException :
         pass
