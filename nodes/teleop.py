#!/usr/bin/env python

import rospy
import tty
import select
import sys
import termios
from geometry_msgs.msg import Twist, Vector3

rospy.init_node('teleop')

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

tout = Twist()
l0 = Vector3(0.0, 0.0, 0.0)
a0 = Vector3(0.0, 0.0, 0.0)

tout.linear = l0
tout.angular = a0

print tout


def getKey():
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

settings = termios.tcgetattr(sys.stdin)
key = None

if __name__=="__main__":
	while not rospy.is_shutdown():
		key = getKey()
		print key
		if key == 'u':
			l0 = Vector3(0.5, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, 1.0)
		elif key == 'i':
			l0 = Vector3(0.5, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, 0.0)
		elif key == 'o':
			l0 = Vector3(0.5, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, -1.0)
		elif key == 'j':
			l0 = Vector3(0.0, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, 1.0)
		elif key == 'k':
			l0 = Vector3(0.0, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, 0.0)
		elif key == 'l':
			l0 = Vector3(0.0, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, -1.0)
		elif key == 'm':
			l0 = Vector3(-0.5, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, 1.0)
		elif key == ',':
			l0 = Vector3(-0.5, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, 0.0)
		elif key == '.':
			l0 = Vector3(-0.5, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, -1.0)
		else:
			l0 = Vector3(0.0, 0.0, 0.0)
			a0 = Vector3(0.0, 0.0, 0.0)
			if key == '\x03':
				break

		tout.linear = l0
		tout.angular = a0

		print tout

		pub.publish(tout);