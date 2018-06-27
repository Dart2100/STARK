* 运行：
----
#本目录下运行 sudo ./sudo_it.sh

* 修改：
----
host=192.168.1.147
port=9555
vin=1+2+14  --> 保持与gateway/config.ini中的vin一致
>>	    第一位为仿真和实际的区分位，仿真为S（大写），实车为0/1
>>	    中间两位为宣城/杭州区分位，宣城00，杭州01
>>	    最后14位为车辆区分位

* 检验
----
可通过运行 ~/.container下的start_container.sh来检验是否设置成功
	----tail -f /tmp/container.log 没有报错信息
	----否则根据错误信息进行修复（通常为缺少alluxio等模块，pip一下即可）
