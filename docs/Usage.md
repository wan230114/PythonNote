## 1. 开始

下载以及clone：  
```bash
git clone https://github.com/wan230114/PythonNote.git
```

## 2. 高效软件配置
### 2.1. Markdown食用软件安装
安装vscode软件：  
- https://code.visualstudio.com/Download

安装插件，插件的一键同步设置 **(推荐)**：  
- 打开扩展，安装插件 `Settings Sync`

使用 `Settings Sync` 同步设置：
- 设置 sync.gist，进行同步下载，`sync.gist`：
  ```text
  9119aa6c385cce49769343cd90e5dc7d
  ```

---
**本gist内容常用简介**

本套同步设置特点：
- 丰富的实用插件
- 丰富的设置，及快键键设置

常用插件：
- Markdown、Python及其相关插件
- IPython for VSCode(发送当前选择行到ipython终端运行)
- ...

自定义的终端设置：
- 鼠标融合，双击复制，右击粘贴。（复制的分隔符设置位于 `设置 --> 功能 --> 终端 --> 最后一项terminal.integrated.wordSeparators` ）
- 在终端中打开目录或文件到编辑器。

常用自定义快捷键：
| win          | mac             | 说明                           |
|--------------|-----------------|--------------------------------|
| Markdown：   |                 |                                |
| `ctrl+g`     | `command+g`     | 可以快速选择markdown中的代码块 |
| `ctrl+enter` | `command+enter` | 快速运行选中命令行或当前行     |
| `ctrl+L`     | `ctrl+L`        | 设置列表                       |
| 窗口管理：   |                 |                                |
| `ctrl+w`     | `command+W`     | 关闭窗口                       |
| ...          |                 |                                |
| 终端：       |                 |                                |
|              |                 | 新建终端                       |
|              |                 | 切换终端                       |
| 文本编辑： |                 |                                |
|              |                 | 返回上次所在位置               |
|              |                 | 返回下次所在位置               |

## npm服务器环境安装
使用其本地访问文档。安装docsify-cli工具:
```shell
npm i docsify-cli -g
```

## 3. 食用方法

打开PythonNote目录作为项目目录  
- 文件 --> 打开文件夹  --> PythonNote
- File --> Open Folder --> PythonNote


然后运行一个本地服务器，这样就可以在 http://localhost:3000 实时访问文档网页渲染效果。(实时将项目中的文件更改同步更新到网页端)

```shell
docsify serve ./
```


# 补充
怎么快速从终端中打开一个文件？
怎么从某一个文件快速进入当前文件目录终端？