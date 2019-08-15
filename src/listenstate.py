#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def chatter_callback(message):

    rospy.loginfo("Current X Coordinate %s", message.data)

def listener():

    rospy.init_node('listengetstatenode', anonymous=True)
    rospy.Subscriber("getstatenodetalker", String, chatter_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
