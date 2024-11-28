import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %s" % msg.data)



def main():
    sub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)
            
