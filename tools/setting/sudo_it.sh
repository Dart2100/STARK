#!/bin/bash
exec 2> log/ErrInfo.log
#set -x

cp -a src/.container ~
cp -a src/rc.local /etc

vim ~/catkin_ws/src/car_ros/smartcar/container_config/config.ini

exit 0
