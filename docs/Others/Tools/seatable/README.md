# seatable

启动：
```bash
cd /opt/seatable/
docker-compose start
docker exec -d seatable /shared/seatable/scripts/seatable.sh start

# 可手动新增账户
docker exec -it seatable /shared/seatable/scripts/seatable.sh superuser
# 执行上述命令后， 点击进入用户组： http://jun-seatable.com/group-invite/c5db628e/
```


配置：
```bash
docker-compose start
docker-compose stop

nohup docker-compose up &>log &
# docker-compose up

docker exec -it seatable /shared/seatable/scripts/seatable.sh start

docker exec -it seatable /shared/seatable/scripts/seatable.sh superuser

docker exec -d seatable /shared/seatable/scripts/seatable.sh restart

```

https://seatable.github.io/seatable-scripts-cn/python/


[在线协同表格SeaTable（安装篇） | 老苏的blog](https://laosu.ml/2021/03/29/%E5%9C%A8%E7%BA%BF%E5%8D%8F%E5%90%8C%E8%A1%A8%E6%A0%BCSeaTable%EF%BC%88%E5%AE%89%E8%A3%85%E7%AF%87%EF%BC%89/)


## python

```bash
cd /opt
wget https://github.com/seatable/seatable-admin-docs/releases/download/seatable-python-runner-2.0.2/seatable-python-runner-2.0.2.zip
unzip seatable-python-runner-2.0.2.zip
rm seatable-python-runner-2.0.2.zip

```