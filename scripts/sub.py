#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16MultiArray

def callback(msg):
    res = msg.data[0] + msg.data[1]
    print(msg.data[0], "+", msg.data[1], "=", res)

def main():
  rospy.init_node('subscriber', anonymous=True)
  pub = rospy.Subscriber("/calculator", Int16MultiArray, callback, queue_size=1)
  rospy.spin()

if __name__ == '__main__':
    main()
