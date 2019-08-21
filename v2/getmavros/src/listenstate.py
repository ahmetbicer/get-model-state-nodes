#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import TwistStamped
from PySide2 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()

#Widgets
label = QtWidgets.QLabel("X: ")
label1 = QtWidgets.QLabel("")

label2 = QtWidgets.QLabel("Y: ")
label3 = QtWidgets.QLabel("")

label4 = QtWidgets.QLabel("Z: ")
label5 = QtWidgets.QLabel("")

#Layout
layout = QtWidgets.QHBoxLayout()
layout.addWidget(label)
layout.addWidget(label1)
layout2 = QtWidgets.QHBoxLayout()
layout2.addWidget(label2)
layout2.addWidget(label3)
layout3 = QtWidgets.QHBoxLayout()
layout3.addWidget(label4)
layout3.addWidget(label5)
main_layout = QtWidgets.QVBoxLayout()
main_layout.addLayout(layout)
main_layout.addLayout(layout2)
main_layout.addLayout(layout3)
window.setLayout(main_layout)


def get_vel(message):
    print message.twist.linear
    label1.setText(str(message.twist.linear.x))
    label3.setText(str(message.twist.linear.y))
    label5.setText(str(message.twist.linear.z))
    #rospy.loginfo("Current Z Coordinate %s", message)

#Listener Node
def listener():
    rospy.init_node('listenravmos', anonymous=True)

    rospy.Subscriber("/mavros/local_position/velocity_body", TwistStamped, get_vel)



    window.show()
    app.exec_()
    rospy.spin()

if __name__ == '__main__':
    listener()
