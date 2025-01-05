import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class TimePublisher(Node):

    def __init__(self):
        super().__init__('time_publisher')
        self.publisher_ = self.create_publisher(String, 'elapsed_time', 10)
        self.start_time = time.time()
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        elapsed_time = time.time() - self.start_time
        hours, remainder = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        msg = String()
        msg.data = f'{int(hours)}時間{int(minutes)}分{int(seconds)}秒経過'
        self.publisher_.publish(msg)
        self.get_logger().info('経過時間をパブリッシュしました。')

def main(args=None):
    rclpy.init(args=args)
    node = TimePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        
