#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Taisei Sakai
# SPDX-License-Identifier: BSD-3-Clause


import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class ElapsedTimePublisher(Node):

    def __init__(self):
        super().__init__('elapsed_time_publisher')
        self.publisher_ = self.create_publisher(String, 'elapsed_time', 10)
        self.start_time = time.time()
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1秒ごとにコールバック

        self.hourly_rate = 1300  # 時給
        self.warning_threshold = 60 * 60 * 8  # 8時間を警告閾値とする
        self.get_logger().info('ElapsedTimePublisher node has started.')  # ノード起動確認

    def timer_callback(self):
        # 経過時間と収入を計算
        elapsed_time = time.time() - self.start_time
        total_seconds = int(elapsed_time)
        earned_money = (total_seconds / 3600) * self.hourly_rate  # 時給を秒単位で計算

        # 警告メッセージの生成
        warning_message = ""
        if total_seconds > self.warning_threshold:
            warning_message = "※注意: 8時間を超えました！休憩を取ってください。"

        # トピックに送信するメッセージ
        msg = String()
        msg.data = (
            f'経過時間: {total_seconds}秒\n'
            f'累計収入: {int(earned_money)}円\n'
            f'{warning_message}'
        )
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = ElapsedTimePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

