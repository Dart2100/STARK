#!/usr/bin/python
旧版本的包由于依赖过来而无法升级或删除，此时需要忽略掉原有依赖，升级/删除
例如 enum34的升级：
sudo pip install enum34 --ignore-installed enum34
