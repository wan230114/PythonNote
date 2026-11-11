
# 调试笔记

python:

```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [{
        "name": "Python: 当前文件",
        "type": "python",
        "request": "launch",
        "program": "main.py",
        "console": "integratedTerminal",
        "justMyCode": true,
        "args": [
            "generate",
            "--samplesFile",
            "test/sample.list",
            "--output",
            "test/out/frequency2000.txt",
            "--samplesOutput",
            "test/out/frequency2000-samples.txt",
            "--startWith",
            "Index",
            "--sampleBits"
        ]
    }]
}
```

go:

```json
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Package",
            "type": "go",
            "request": "launch",
            "mode": "auto",
            "program": "main.go",
            "args": [
                "-ldflags='-s -w'",
                "-installsuffix", "cgo", 
                "-o", "scheduler"
            ],
            "env": {
                "GOOS": "linux",
                "GOARCH": "amd64",
                "HARBOR_REGISTRY": "docker.reg.me:6698",
                "ETCD_ENDPOINTS": "192.168.1.20:2379",
                "KUBE_CONFIG": "/home/chenjun/gitlab/opengk-go/opengk-scheduler/opengk-go-cfg/kubelet.conf",
                "CONFIG": "/home/chenjun/gitlab/opengk-go/opengk-scheduler/config/config-fat.yaml",
                "GOPROXY": "https://proxy.golang.com.cn,direct"
            }
        }
    ]
}

```



## windows10 排错指南

windows10下Bad owner or permissions on .ssh/config的解决办法

2020-06-12阅读 4.7K0

方法很简单，亲测有效。

1. 进入如下路径C:\Users\用户名\.ssh，你会看到有config这个文件
2. 右击config,属性→安全→高级→禁止继承→删除所有继承(忘了全称了，大概这个意思)→确定

如果系统是英文：

Properties -> Security -> Advanced -> Disable Inheritance -> Remove all inherited permissions from this object

参考Bad owner or permissions on C:\Users\USER/.ssh/config

