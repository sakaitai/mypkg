#!/bin/bash
# SPDX-FileCopyrightText: 2024 TAISEI SAKAI
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/ros2_ws/install/setup.bash  # ROS 2ワークスペースの環境設定

# タイムアウト10秒でtalkerノードを実行し、ログを/tmp/mypkg.logに保存
timeout 10 ros2 run mypkg talker > /tmp/mypkg.log

# ログファイルから特定の経過時間メッセージが含まれているかをgrepでチェック
grep '時間' /tmp/mypkg.log
grep '分' /tmp/mypkg.log
grep '秒' /tmp/mypkg.log

