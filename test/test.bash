#!/bin/bash
# SPDX-FileCopyrightText: 2024 TAISEI SAKAI
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/ros2_ws/install/setup.bash  # ROS 2ワークスペースの環境設定

# タイムアウトでtalkerノードを実行し、ログを/tmp/mypkg.logに保存
timeout 10 ros2 run mypkg talker > /tmp/mypkg.log &  # バックグラウンドで実行

# 少し待ってからログを確認（1秒ごとに更新されるので）
sleep 2

# ログファイルから特定のメッセージが含まれているかをgrepでチェック
cat /tmp/mypkg.log | grep -e '秒 とんかつバイト: ' -e '円'

# プロセスを終了する
kill %1

