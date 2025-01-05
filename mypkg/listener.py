import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TimeListener(Node):

    def __init__(self):
        super().__init__('time_listener')
        self.subscription = self.create_subscription(
            String,
            'elapsed_time',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'受信: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = TimeListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
            
