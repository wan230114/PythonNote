
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