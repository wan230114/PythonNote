
# Install

参考： [Docker---Docker-compose部署安装confluence并进行数据迁移_--山海--的博客-CSDN博客_confluence docker](https://blog.csdn.net/AnNan1997/article/details/125497406)

参考： [Docker 安装 Confluence_hellowordx007的博客-CSDN博客_docker安装confluence](https://blog.csdn.net/u013984806/article/details/124562189)

## Docker 安装 Confluence

docker-compose.yaml 如下:


```bash

{
echo '
atlassian-confluence:
    image: cptactionhank/atlassian-confluence:7.9.3
    container_name: confluence
    network_mode: host
    volumes:
      - "/etc/timezone:/etc/timezone:ro"
      - "/etc/localtime:/etc/localtime:ro"
      - "./atlassian-confluence/server.xml:/opt/atlassian/confluence/conf/server.xml"
      - "./atlassian-confluence/lib/mysql-connector-java-8.0.22.jar:/opt/atlassian/confluence/confluence/WEB-INF/lib/mysql-connector-java-8.0.22.jar"
      - "./atlassian-confluence/atlassian-agent.jar:/opt/atlassian/confluence/atlassian-agent.jar"
    environment:
      CATALINA_OPTS: "-javaagent:/opt/atlassian/confluence/atlassian-agent.jar"
' > docker-compose.yaml
}
```
atlassian-agent.jar 可以从如下地址获取:
链接:https://pan.baidu.com/s/1JKgDtoTyXP8hHcooMiJgVQ 密码:0856

server.xml 内容如下，仅修改了 Context 的path值为 ‘/confluence’


# 教程2

```bash

{
cd /share-nfs/confluence/docker_data/confluence/
mkdir -p logs data
chmod 777 logs data

echo "
version: '3'
services:
  confluence:
    image: atlassian/confluence-server:7.18.3
    container_name: confluence
    ports:
      - '8090:8090'
      - '8091:8091'
    restart: always
    depends_on:
      - db
    volumes:
      - $PWD/logs:/opt/atlassian/confluence/logs
      - $PWD/confluence-data:/var/atlassian/confluence
    environment:
      - TZ='Asia/Shanghai'
  db:
    image: bitnami/postgresql
    container_name: confluence-db
    ports:
      - '5432:5432'
    restart: always
    environment:
      - POSTGRES_PASSWORD=123456 #数据库密码
      - TZ='Asia/Shanghai'
    volumes:
      - $PWD/pgsql-data:/var/lib/postgresql/data
" >docker-compose.yaml
}

docker-compose up -d
docker ps
```

```bash
docker exec -it -u root confluence-db bash
psql -U postgres
123456
\l
CREATE DATABASE confluence WITH OWNER postgres;
\l
```

```bash
scp my2:/opt/atlassian-confluence-7.18.3/bin/tomcat-configuration.jar ./
docker exec confluence java -version
docker exec confluence ls /opt/atlassian/confluence/bin/
docker cp  ./tomcat-configuration.jar  confluence:/opt/atlassian/confluence/bin/

docker restart confluence


docker exec -it confluence bash
# export JAVA_HOME=/opt/java/openjdk
# export PATH=/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH
# export APP_NAME=confluence
# export RUN_USER=confluence
# export RUN_GROUP=confluence
# export CONFLUENCE_HOME=/var/atlassian/application-data/confluence
# export CONFLUENCE_INSTALL_DIR=/opt/atlassian/confluence

export CATALINA_HOME=/opt/atlassian/confluence/
export JAVA_OPTS="-javaagent:/opt/atlassian/confluence/bin/tomcat-configuration.jar ${JAVA_OPTS}"

cd /opt/atlassian/confluence/
bin/setenv.sh
bin/stop-confluence.sh
bin/start-confluence.sh
```


---
接下来打开网页操作：

破解失败
```bash
docker cp confluence:/opt/atlassian/confluence/confluence/WEB-INF/lib/atlassian-extras-decoder-v2-3.4.6.jar ./atlassian-extras-2.4.jar
docker cp ./atlassian-extras-2.4.jar confluence:/opt/atlassian/confluence/confluence/WEB-INF/lib/atlassian-extras-decoder-v2-3.4.6.jar 
docker cp ./atlassian-extras-2.4.bak confluence:/opt/atlassian/confluence/confluence/WEB-INF/lib/atlassian-extras-decoder-v2-3.4.6.jar 
docker restart confluence
```


解决导入空间后无法登录的BUG
```bash
docker exec -it -u root confluence bash
# /opt/atlassian/confluence/bin
```


# 教程3

https://www.cnblogs.com/jhno1/p/14998309.html

```bash

```


# 教程4

```bash
{
cd /share-nfs/confluence/docker_data/confluence/
mkdir -p logs confluence-data pgsql-data
chmod 777 logs confluence-data pgsql-data

echo "version: '3.3'
services:
  confluence:
    image: cptactionhank/atlassian-confluence:7.2.0
    container_name: confluence
    ports:
      - '8090:8090'
      - '8091:8091'
    restart: always
    depends_on:
      - db
    volumes:
      - $PWD/logs:/opt/atlassian/confluence/logs
      - $PWD/confluence-data:/var/atlassian/confluence
  db:
    image: postgres:latest
    container_name: confluence-db
    ports:
      - '5432:5432'
    restart: always
    environment:
      - POSTGRES_PASSWORD=123456
    volumes:
      - $PWD/pgsql-data:/var/lib/postgresql/data
" >docker-compose.yaml
cat docker-compose.yaml
}

docker-compose up -d
docker ps
```

```bash
docker cp confluence:/opt/atlassian/confluence/confluence/WEB-INF/lib/atlassian-extras-decoder-v2-3.4.1.jar ./atlassian-extras-2.4.jar
docker cp ./atlassian-extras-2.4.jar confluence:/opt/atlassian/confluence/confluence/WEB-INF/lib/atlassian-extras-decoder-v2-3.4.1.jar 

docker-compose restart

```

