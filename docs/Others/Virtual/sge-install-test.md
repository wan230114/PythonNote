
---
## 1. docker实现（centos）【已过时】

https://github.com/stevekm/docker-centos6-sge

```bash
git clone https://github.com/stevekm/docker-centos6-sge.git
cd docker-centos6-sge
docker build -t stevekm/docker-centos6-sge .

docker run --rm -t -i stevekm/docker-centos6-sge
```


---
## 2. docker实现（ubuntu）【测试报错】

```bash
git clone https://github.com/gawbul/docker-sge.git
cd docker-sge
docker build -t gawbul/docker-sge .
```


---
## 3. k8s【有点麻烦，不想用】

```bash
git clone https://github.com/wtakase/docker-sge.git
```


