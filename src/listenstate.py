#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
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

#Get Functions
def get_x(message):
    label1.setText(message.data)
    rospy.loginfo("Current X Coordinate %s", message.data)

def get_y(message):
    label3.setText(message.data)
    rospy.loginfo("Current Y Coordinate %s", message.data)

def get_z(message):
    label5.setText(message.data)
    rospy.loginfo("Current Z Coordinate %s", message.data)

#Listener Node
def listener():
    rospy.init_node('listengetstatenode', anonymous=True)

    rospy.Subscriber("getter_x", String, get_x)
    rospy.Subscriber("getter_y", String, get_y)
    rospy.Subscriber("getter_z", String, get_z)

    window.show()
    app.exec_()
    rospy.spin()

if __name__ == '__main__':
    listener()
