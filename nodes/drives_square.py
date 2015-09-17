#!/usr/bin/env python
"Autonomously move Neato through a 1m by 1m square"

import rospy

from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry

rospy.init_node('drives_square')

#def process_odom(msg):
#	xdis = 


pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
#sub = rospy.Subscriber("/odom", Odometry, process_odom)

twist = Twist()
l0 = Vector3(0.0, 0.0, 0.0)
a0 = Vector3(0.0, 0.0, 0.0)
twist.linear = l0
twist.angular = a0

tl= 3.66 #time to 1 meter
ta= 1.7 #time to rotate 90 degrees
itime = rospy.get_time()

while not rospy.is_shutdown():
	seconds = rospy.get_time() - itime
	if seconds > 0 and seconds < tl:
		l0 = Vector3(0.5, 0.0, 0.0)
		a0 = Vector3(0.0, 0.0, 0.0)
	elif seconds > tl and seconds < tl+ta:
		l0 = Vector3(0.0, 0.0, 0.0)
		a0 = Vector3(0.0, 0.0, -1.0)
	elif seconds > tl+ta and seconds < 2*tl + ta:
		l0 = Vector3(0.5, 0.0, 0.0)
		a0 = Vector3(0.0, 0.0, 0.0)
	elif seconds > 2*tl + ta and seconds < 2*tl + 2*ta:
		l0 = Vector3(0.0, 0.0, 0.0)
		a0 = Vector3(0.0, 0.0, -1.0)
	elif seconds > 2*tl+ 2*ta and seconds < 3*tl + 2*ta:
		l0 = Vector3(0.5, 0.0, 0.0)
		a0 = Vector3(0.0, 0.0, 0.0)
	elif seconds > 3*tl + 2*ta and seconds < 3*tl + 3*ta:
		l0 = Vector3(0.0, 0.0, 0.0)
		a0 = Vector3(0.0, 0.0, -1.0)
	elif seconds > 3*tl+ 3*ta and seconds < 4*tl + 3*ta:
		l0 = Vector3(0.5, 0.0, 0.0)
		a0 = Vector3(0.0, 0.0, 0.0)	
	elif seconds > 4*tl + 3*ta and seconds < 4*tl + 4*ta:
		l0 = Vector3(0.0, 0.0, 0.0)
		a0 = Vector3(0.0, 0.0, -1.0)
	elif seconds > 4*tl + 4*ta:
		l0 = Vector3(0.0, 0.0, 0.0)
		a0 = Vector3(0.0, 0.0, 0.0)

	twist.linear = l0
	twist.angular = a0

	print seconds

	pub.publish(twist);
		


