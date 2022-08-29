
## 执行前后对比

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Workflow                  # new type of k8s spec
metadata:
  generateName: test    # name of the workflow spec
spec:
  entrypoint: whalesay          # invoke the whalesay template
  templates:
    - name: whalesay              # name of the template
      container:
        image: docker/whalesay
        command: [ cowsay ]
        args: [ "hello world" ]
        resources: # limit the resources
          limits:
            memory: 32Mi
            cpu: 100m
```


```yaml
kind: Pod
apiVersion: v1
metadata:
  name: hello-world-testzbxh6
  namespace: argo
  selfLink: /api/v1/namespaces/argo/pods/hello-world-testzbxh6
  uid: dd8c8a32-0723-489f-b23d-6e4d0ca01ab9
  resourceVersion: '76865726'
  creationTimestamp: '2022-06-14T07:51:18Z'
  labels:
    workflows.argoproj.io/completed: 'true'
    workflows.argoproj.io/workflow: hello-world-testzbxh6
  annotations:
    workflows.argoproj.io/execution: '{"deadline":"2022-06-16T07:51:18Z"}'
    workflows.argoproj.io/node-name: hello-world-testzbxh6
    workflows.argoproj.io/outputs: '{"exitCode":"0"}'
    workflows.argoproj.io/template: >-
      {"name":"whalesay","arguments":{},"inputs":{},"outputs":{},"metadata":{},"container":{"name":"","image":"docker/whalesay","command":["cowsay"],"args":["hello
      world"],"resources":{"limits":{"cpu":"100m","memory":"32Mi"}}}}
  ownerReferences:
    - apiVersion: argoproj.io/v1alpha1
      kind: Workflow
      name: hello-world-testzbxh6
      uid: dac69695-31d6-4ac4-b0dd-76d502b29315
      controller: true
      blockOwnerDeletion: true
spec:
  volumes:
    - name: podmetadata
      downwardAPI:
        items:
          - path: annotations
            fieldRef:
              apiVersion: v1
              fieldPath: metadata.annotations
        defaultMode: 420
    - name: docker-sock
      hostPath:
        path: /var/run/docker.sock
        type: Socket
    - name: default-token-p6vd7
      secret:
        secretName: default-token-p6vd7
        defaultMode: 420
  containers:
    - name: wait
      image: 'docker.reg.me:6698/public/argoexec:v2.8.2'
      command:
        - argoexec
        - wait
      env:
        - name: ARGO_POD_NAME
          valueFrom:
            fieldRef:
              apiVersion: v1
              fieldPath: metadata.name
      resources: {}
      volumeMounts:
        - name: podmetadata
          mountPath: /argo/podmetadata
        - name: docker-sock
          readOnly: true
          mountPath: /var/run/docker.sock
        - name: default-token-p6vd7
          readOnly: true
          mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      imagePullPolicy: IfNotPresent
    - name: main
      image: docker/whalesay
      command:
        - cowsay
      args:
        - hello world
      resources:
        limits:
          cpu: 100m
          memory: 32Mi
        requests:
          cpu: 100m
          memory: 32Mi
      volumeMounts:
        - name: default-token-p6vd7
          readOnly: true
          mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      terminationMessagePath: /dev/termination-log
      terminationMessagePolicy: File
      imagePullPolicy: Always
  restartPolicy: Never
  terminationGracePeriodSeconds: 30
  activeDeadlineSeconds: 172799
  dnsPolicy: ClusterFirst
  serviceAccountName: default
  serviceAccount: default
  nodeName: hadoop05
  securityContext: {}
  schedulerName: default-scheduler
  tolerations:
    - key: node.kubernetes.io/not-ready
      operator: Exists
      effect: NoExecute
      tolerationSeconds: 300
    - key: node.kubernetes.io/unreachable
      operator: Exists
      effect: NoExecute
      tolerationSeconds: 300
  priority: 0
  enableServiceLinks: true
status:
  phase: Succeeded
  conditions:
    - type: Initialized
      status: 'True'
      lastProbeTime: null
      lastTransitionTime: '2022-06-14T07:51:18Z'
      reason: PodCompleted
    - type: Ready
      status: 'False'
      lastProbeTime: null
      lastTransitionTime: '2022-06-14T07:51:31Z'
      reason: PodCompleted
    - type: ContainersReady
      status: 'False'
      lastProbeTime: null
      lastTransitionTime: '2022-06-14T07:51:31Z'
      reason: PodCompleted
    - type: PodScheduled
      status: 'True'
      lastProbeTime: null
      lastTransitionTime: '2022-06-14T07:51:18Z'
  hostIP: 192.168.1.24
  podIP: 10.244.6.180
  podIPs:
    - ip: 10.244.6.180
  startTime: '2022-06-14T07:51:18Z'
  containerStatuses:
    - name: main
      state:
        terminated:
          exitCode: 0
          reason: Completed
          startedAt: '2022-06-14T07:51:29Z'
          finishedAt: '2022-06-14T07:51:29Z'
          containerID: >-
            docker://2c90584cb4805c3539f34d7d0cb5ac65eae4d0753abe1e9537f99b17cfec8766
      lastState: {}
      ready: false
      restartCount: 0
      image: 'docker/whalesay:latest'
      imageID: >-
        docker-pullable://docker/whalesay@sha256:178598e51a26abbc958b8a2e48825c90bc22e641de3d31e18aaf55f3258ba93b
      containerID: >-
        docker://2c90584cb4805c3539f34d7d0cb5ac65eae4d0753abe1e9537f99b17cfec8766
      started: false
    - name: wait
      state:
        terminated:
          exitCode: 0
          reason: Completed
          startedAt: '2022-06-14T07:51:20Z'
          finishedAt: '2022-06-14T07:51:30Z'
          containerID: >-
            docker://613b3c2fab384e01723368b20cd6f80166cdc33376d663edee7e0c7fa6bb20db
      lastState: {}
      ready: false
      restartCount: 0
      image: 'docker.reg.me:6698/public/argoexec:v2.8.2'
      imageID: >-
        docker-pullable://docker.reg.me:6698/public/argoexec@sha256:daff7b83755e99f5429dae5843f3786d3dbfbe9cb4b2c40de5b2b741184ca0aa
      containerID: >-
        docker://613b3c2fab384e01723368b20cd6f80166cdc33376d663edee7e0c7fa6bb20db
      started: false
  qosClass: Burstable

```