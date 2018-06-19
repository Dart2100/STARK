#!/bin/bash
exec 2> /tmp/container.log
exec 1>&2
set -x
nohup python /home/yunle/catkin_ws/src/car_ros/smartcar/src/monitor.py & 
