#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import GetModelState
from std_msgs.msg import String

def main():
    pub = rospy.Publisher('getstatenodetalker', String, queue_size=10)
    rospy.init_node('getstatenode', anonymous=True)
    rate = rospy.Rate(5)
    state_msg = ModelState()
    state_msg.model_name = 'suv'

    rospy.wait_for_service('/gazebo/get_model_state')
    try:
        i = 0
        while not rospy.is_shutdown():
            get_state = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            gets = get_state("suv",'')
            print("X: " , gets.pose.position.x)
            print("Y: " , gets.pose.position.y)
            pub.publish(str(gets.pose.position.x))
            rate.sleep()
            i=i+1

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
