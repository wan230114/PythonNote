```bash
kubectl apply -f test-volumes.yaml -n snv
kubectl apply -f opengk-pvc.yaml -n snv
kubectl delete -f opengk-pvc.yaml -n snv

kubectl apply -f opengk-pvc.yaml -n argo
kubectl apply -f opengk-pvc.yaml -n argo

kubectl get PodPreset job-preset -n callvariant -o yaml
kubectl apply -f snv-podpreset.yaml -n snv

kubectl get PodPreset -n snv
kubectl get PodPreset -n snv -oyaml
kubectl get PodPreset -n annotation -oyaml

kubectl delete PodPreset job-preset -n snv
kubectl apply -f test-pre-set.yaml -n snv
kubectl apply -f backup-pre-set.yaml -n snv

kubectl edit configmap workflow-controller-configmap -n argo

kubectl get configmap workflow-controller-configmap -n argo -o yaml


# 如何用 kubectl 修改Argo的默认容器设置
kubectl get argoworkflow -n argo
kubectl edit argoworkflow my-workflow -n argo
```


```bash
# PodPreset
mkdir -p PodPreset--bak
for ns in alignment callvariant mutation annotation snv cnvbatch cnvseqrbam couplescreen family; do
    # ns=callvariant
    # kubectl get PodPreset -n $ns -oyaml > PodPreset--bak/$ns-bak-PodPreset.yaml
    # kubectl get PodPreset job-preset -n $ns -o yaml > PodPreset--bak/$ns-bak-PodPreset.yaml
    kubectl delete PodPreset job-preset -n $ns
    kubectl apply -f PodPreset--bak/PodPreset.yaml -n $ns
    # kubectl apply -f job-preset.yaml -n $ns
    # kubectl get PodPreset job-preset -n $ns -o yaml > PodPreset--bak/$ns-bak-PodPreset.yaml
done
```


```yaml
  volumes:
  - hostPath:
      path: /mfs1/opengk/opengk-tmp
      type: Directory
    name: tmp
  - hostPath:
      path: /mfs1/opengk/opengk-input
      type: Directory
    name: input
  - hostPath:
      path: /mfs1/opengk/opengk-output
      type: Directory
    name: output
  - hostPath:
      path: /mfs1/opengk/opengk-other
      type: Directory
    name: other
  - hostPath:
      path: /mfs1/opengk/opengk-logs
      type: Directory
    name: logs
  - hostPath:
      path: /mfs1/gene
      type: Directory
    name: ref
#   - name: logs
#     persistentVolumeClaim:
#       claimName: opengk-logs-pvc
#   - name: input 
#     persistentVolumeClaim:
#       claimName: opengk-input-pvc
#   - name: tmp
#     persistentVolumeClaim:
#       claimName: opengk-tmp-pvc
#   - name: output
#     persistentVolumeClaim:
#       claimName: opengk-output-pvc
#   - name: other
#     persistentVolumeClaim:
#       claimName: opengk-other-pvc
#   - name: ref
#     persistentVolumeClaim:
#       claimName: opengk-ref-pvc
```

Deployment修改：

```yaml
spec:
  template:
    spec:
      volumes:
        # - name: opengk-input
        #   persistentVolumeClaim:
        #     claimName: opengk-input-pvc
        # - name: opengk-output
        #   persistentVolumeClaim:
        #     claimName: opengk-output-pvc
        - name: opengk-input
          hostPath:
            path: /mfs1/opengk/opengk-input
            type: Directory
        - name: opengk-output
          hostPath:
            path: /mfs1/opengk/opengk-output
            type: Directory
        - name: opengk-tmp
          hostPath:
            path: /mfs1/opengk/opengk-tmp
            type: Directory
    name: tmp
      containers:
        - name: opengk-job
          volumeMounts:
            - name: opengk-input
              mountPath: /input
            - name: opengk-output
              mountPath: /output
            - name: opengk-tmp
              mountPath: /tmpa
```

