#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import json 
import os




from std_msgs.msg import String
from smbus import SMBus

addr = 0x8 # bus addressi
bus = SMBus(1) # indicates /dev/ic2-1i

#os.system('sudo sh -c "echo Jas2544!! | sudo -S python3 -c \'import smbus; bus = smbus.SMBus(1);\'"')



pose_dict = {"reverberant" : {"1":0, "2":0, "3":0 }, "absorptive" : {"1":160, "2":90, "3":90}} #Specific panel poses maintained as a dict of dicts : 'reverb Setting' -> {'panel':pose}
class panelBus(Node):

    def __init__(self):
        super().__init__("panelBus")
        self.subscription = self.create_subscription(String, 'panelTopic', self.listener_callback, 10)
        self.subscription
    def listener_callback(self, msg):
        global addr
        if msg.data == 'reverberant':
            self.get_logger().info(str(pose_dict["reverberant"]))
            jsonified = json.dumps(pose_dict["reverberant"])
            byteified = jsonified.encode('utf-8')
           # os.system('sudo sh -c "echo Jas2544!! | sudo -S python3 -c \'import smbus; bus = smbus.SMBus(1); bus.write_i2c_block_data({addr}, 0, list({byteified}))\'"')
#            os.system(f'sudo sh -c "echo Jas2544!! | sudo -S python3 -c \'import smbus; bus = smbus.SMBus(1); bus.write_i2c_block_data({addr}, 0, {repr(byteified)});\'"')


            bus.write_i2c_block_data(addr, 0, list(byteified))
            self.get_logger().info("bus write")
        if msg.data == 'absorptive':
            self.get_logger().info(str(pose_dict["absorptive"]))
            jsonified = json.dumps(pose_dict["absorptive"])
            byteified = jsonified.encode('utf-8')
            bus.write_i2c_block_data(addr, 0, list(byteified))
            self.get_logger().info("bus write")


        



def main():
    rclpy.init()
    node = panelBus()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
