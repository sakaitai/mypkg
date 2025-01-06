import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class TimePublisher(Node):

    def __init__(self):
        super().__init__('time_publisher')
        self.publisher_ = self.create_publisher(String, 'elapsed_time', 10)
        self.start_time = time.time()
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1秒ごとにコールバック

        self.hourly_rate = 1300  # 時給

    def timer_callback(self):
        elapsed_time = time.time() - self.start_time
        total_seconds = int(elapsed_time)
        earned_money = (total_seconds / 3600) * self.hourly_rate  # 時給を秒単位で計算

        msg = String()
        msg.data = f'{total_seconds}秒 とんかつバイト: {int(earned_money)} 円'
        self.publisher_.publish(msg)
        self.get_logger().info(f'経過時間: {total_seconds}秒, とんかつバイトの収入: {int(earned_money)} 円')

def main(args=None):
    rclpy.init(args=args)
    node = TimePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

