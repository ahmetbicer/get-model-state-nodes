#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import GetModelState
from std_msgs.msg import String

def main():
    pub_x = rospy.Publisher('getter_x', String, queue_size=18)
    pub_y = rospy.Publisher('getter_y', String, queue_size=18)
    pub_z = rospy.Publisher('getter_z', String, queue_size=18)

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
            pub_x.publish(str(gets.pose.position.x))
            pub_y.publish(str(gets.pose.position.y))
            pub_z.publish(str(gets.pose.position.z))
            rate.sleep()
            i=i+1

    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
