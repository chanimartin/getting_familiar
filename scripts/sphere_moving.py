#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point, Vector3, Pose
from std_msgs.msg import ColorRGBA


rospy.init_node('sphere_moving')
pub = rospy.Publisher("/sph_marker", Marker, queue_size = 10)

r = rospy.Rate(10)
while not rospy.is_shutdown():
	marker_message = Marker()
	marker_message.header.frame_id = "base_link"
	marker_message.header.stamp = rospy.Time.now()
	marker_message.ns = "sphere_moving"
	marker_message.id = 0
	marker_message.type = Marker.SPHERE
	marker_message.action = Marker.ADD
	marker_message.pose.position.x = 1
	marker_message.pose.position.y = 0
	marker_message.pose.position.z = 0
	marker_message.pose.orientation.x = 0.0
	marker_message.pose.orientation.y = 0.0
	marker_message.pose.orientation.z = 0.0
	marker_message.pose.orientation.w = 1.0
	marker_message.scale.x = 0.2
	marker_message.scale.y = 0.2
	marker_message.scale.z = 0.2
	marker_message.color.a = 1.0 
	marker_message.color.r = 1.0
	marker_message.color.g = 0.0
	marker_message.color.b = 1.0

	pub.publish(marker_message)
	r.sleep()
