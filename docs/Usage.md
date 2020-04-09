### 开始
- 下载以及clone：  
    ```bash
    git clone https://github.com/wan230114/PythonNote.git
    ```

### 软件安装
- 安装vscode软件：  
  - https://code.visualstudio.com/
- 安装插件 **(推荐)**
  - Settings Sync，设置 sync.gist:
    ```
    9119aa6c385cce49769343cd90e5dc7d
    ```

- 插件包含内容：
  - markdown、Python及其相关插件
  - IPython for VSCode(发送当前选择行到ipython终端运行)
  - 常用自定义快捷键，markdown中：
    - `ctrl+g` 可以快速选择markdown中的代码块

- 打开PythonNote目录作为项目目录  
  - 文件 --> 打开文件夹  --> PythonNote
  - File --> Open Folder --> PythonNote


## 1.1. 本地运行Python脚本方法


## 1.2. 本地访问文档

先安装docsify-cli工具:
```shell
npm i docsify-cli -g
```

然后运行一个本地服务器，这样就可以在 http://localhost:3000 实时访问文档网页渲染效果。

```shell
docsify serve ./
```