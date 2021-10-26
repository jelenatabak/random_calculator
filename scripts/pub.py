#!/usr/bin/env python3

import rospy
from random import randint
from std_msgs.msg import Int16MultiArray

def main():
  rospy.init_node('publisher', anonymous=True)
  pub = rospy.Publisher("/calculator", Int16MultiArray, queue_size=1)
  msg = Int16MultiArray()
  msg.data.append(0)
  msg.data.append(0)
  rate = 10

  while not rospy.is_shutdown():
      x = randint(0,100)
      y = randint(0,100)
      msg.data[0] = x
      msg.data[1] = y
      pub.publish(msg)
      print("How much is", x, "+", y, "?")
      rate.sleep()


if __name__ == '__main__':
    main()
