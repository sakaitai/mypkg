import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(Int16, "countup", 10)
        self.create_timer(0.5, self.cb)
        self.n = 0


    def cb(self):
        rclpy.init()
        node = Listener()
        rclpy.spin(node)


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)

            
