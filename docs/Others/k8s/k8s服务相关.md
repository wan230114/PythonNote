```bash
# 检查Kubernetes集群的状态：
kubectl cluster-info

# 检查集群中的节点状态：
kubectl get nodes

# 检查正在运行的Pod的状态：
kubectl get pods -A

# 检查服务的状态：
kubectl get services -A

netstat -antpu | grep 6443

systemctl status --full kubelet

# systemctl restart kube-proxy
# systemctl restart kubelet
# systemctl restart docker

# systemctl stop kubelet
# systemctl start kubelet
# docker ps -a | sed 1d | grep " k8s_" | awk '{print $1}' | xargs docker stop
# systemctl stop docker
# docker container prune
# systemctl start docker
```

## Pod 清理大法

[K8s无法删除状态为terminating的pod解决方法_k8s terminating-CSDN博客](https://blog.csdn.net/lisongyue123/article/details/118966921)

清理 Pod

```bash

kubectl get pods --all-namespaces | grep -v -- -test- > /mfs1/tmpworkdir/tmp/allpods.txt
for ns in alignment callvariant cnvseqrbam mutation snv cnvbatch; do
    kubectl delete pod $(cat /mfs1/tmpworkdir/tmp/allpods.txt | grep -P "Error|Completed" | grep ^$ns | awk '{print $2}' | xargs) -n $ns;
    # kubectl delete pod $(cat /mfs1/tmpworkdir/tmp/allpods.txt | grep -P "Running" | grep ^$ns | awk '{print $2}' | xargs) -n $ns;
done

for node in hadoop01 hadoop02 hadoop03 hadoop05 hadoop06; do
    ssh $node docker container prune -f
done

for node in hadoop02 hadoop03 hadoop05; do
    ssh $node systemctl restart docker
done

```

```bash
# 查看pod信息
kubectl -n alignment describe pods/star-testwfrhz

```