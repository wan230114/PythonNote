
## 1. 开始

项目下载clone：  
```bash
git clone https://github.com/wan230114/PythonNote.git
```

---
## 2. 高效食用软件 vscode 基本配置

### 2.1. vscode 软件安装及配置

1. 下载及安装软件。
   - 打开vscode官网下载界面：https://code.visualstudio.com/Download
   - 下载并根据向导安装
2. 一键下载设置及安装插件。 准备从公网下载一套相对成型完善的设置。
   - 打开左边侧边栏的扩展商店（快捷键方法， win: `ctrl+shift+x` / mac: `command+shift+x`）
   - 搜索并安装插件： `Settings Sync`。亦可点击[插件地址](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync)完成安装。
   - 插件 `Settings Sync` 的使用：
     - 打开vscode命令面板  
       （点击 >设置 >命令面板。或使用快捷键 win: `ctrl+shift+p` / mac: `command+shift+p`）
     - 输入命令：`>sync advanced`，选中第一条命令，再选中`Sync 打开设置`
     - 输入以下 `Gist ID` 完成
      ```text
      9119aa6c385cce49769343cd90e5dc7d
      ```
     - 输入命令：`>sync Download Settings`，选中第一条命令完成下载。

      （该 `Gist ID` 的 DIY设置的相关介绍见下一小节）

---
### 2.2. vscode - Sync.gist ID 的内容简介

#### 2.2.1. 本套同步设置特点
- 丰富的实用插件
  - Markdown、Python及其相关插件，可以完成语法检测，格式化文本等操作
  - IPython for VSCode(发送当前选择行到ipython终端运行)
  - 其他暂不描述...
- 丰富的 VsCode 软件设置
  - 自定义的终端设置：
    - 鼠标融合，双击复制，右击粘贴。（复制的分隔符设置位于 `设置 --> 功能 --> 终端 --> 最后一项terminal.integrated.wordSeparators` ）
    - 在终端中打开目录或文件到编辑器。
  - ...
- 方便的 VsCode 快键键设置（基于Sublime text3习惯，此处着重介绍）

#### 2.2.2. 常用自定义快捷键

（以下快捷键以 mac 系统为准，windows 的部分快捷键设置可能未及时更新）


**Markdown：**

|     win      |        mac        | 生效条件  |                            说明                             |
|:------------:|:-----------------:|:---------:|:-----------------------------------------------------------:|
|   `ctrl+g`   |    `command+g`    | <b>  </b> |                 快速选择markdown中的代码块                  |
| `ctrl+enter` |   `ctrl+enter`    | <b>  </b> |           快速于IPython终端运行选中命令行或当前行           |
|  <b>  </b>   |     `ctrl+L`      | <b>  </b> |                   创建/取消 无序列表 `- `                   |
|  <b>  </b>   |     `ctrl+L`      | <b>  </b> |                   创建/取消 段落格式 `> `                   |
|  <b>  </b>   |  `ctrl+shift+c`   | <b>  </b> |         创建/取消 checkbox<br>(可单行多行) `- [ ] `         |
|  <b>  </b>   | `command+shift+c` | <b>  </b> | 创建/取消 checkbox<br>（仅单行，细节与上一条互补） `- [ ] ` |


**文本编辑器中：**

|    win    |         mac         | 生效条件  |         说明         |
|:---------:|:-------------------:|:---------:|:--------------------:|
| <b>  </b> |  `command+shift+d`  | <b>  </b> |    向下复制当前行    |
| <b>  </b> | `command+shift+↑/↓` | <b>  </b> |  快速向上/下移动行   |
| <b>  </b> |     `command+c`     | <b>  </b> |       复制(行)       |
| <b>  </b> |     `command+x`     | <b>  </b> |       剪切(行)       |
| <b>  </b> |     `command+v`     | <b>  </b> |         粘贴         |
| <b>  </b> |      <b>  </b>      | <b>  </b> | 返回上次光标所在位置 |
| <b>  </b> |      <b>  </b>      | <b>  </b> | 返回下次光标所在位置 |


**窗口管理：**

|      win       |        mac        |          生效条件          |           说明           |
|:--------------:|:-----------------:|:--------------------------:|:------------------------:|
|    `ctrl+w`    |    `command+w`    | 当光标聚焦于文本编辑窗口时 |         关闭窗口         |
|    `ctrl+w`    |    `command+w`    |     当光标聚焦于终端时     | 将光标聚焦于文本编辑窗口 |
|    `ctrl+e`    |    `command+e`    |     当光标聚焦于终端时     | 将光标聚焦于文本编辑窗口 |
|    `ctrl+e`    |    `command+e`    | 当光标聚焦于文本编辑窗口时 |   将光标聚焦于终端窗口   |
| `ctrl+shift+w` | `command+shift+w` |         <b>  </b>          |  关闭当前编辑组整个窗口  |
|      ...       |     <b>  </b>     |         <b>  </b>          |        <b>  </b>         |


**终端：**

|    win    |      mac       |      生效条件      |   说明   |
|:---------:|:--------------:|:------------------:|:--------:|
| <b>  </b> | `ctrl+shift+~` |     <b>  </b>      | 新建终端 |
| <b>  </b> |  `ctrl+table`  | 当光标聚焦于终端时 | 切换终端 |


**脚本执行：**

|    win    |   mac    | 生效条件  |   说明   |
|:---------:|:--------:|:---------:|:--------:|
| <b>  </b> | `ctrl+b` | <b>  </b> | 运行程序 |


## 3. npm服务器环境安装

将本项目的文件夹自动渲染为本地网页，便于开发，或本地查看渲染访问文档网页。

安装docsify-cli工具:
```shell
# npm安装网上教程一大把，不再赘述
npm i docsify-cli -g
```

## 4. vscode 食用方法

打开PythonNote目录作为项目目录  
- 文件 --> 打开文件夹  --> PythonNote
- File --> Open Folder --> PythonNote

然后运行一个本地服务器，这样就可以在 http://localhost:3000 实时访问文档网页渲染效果。(实时将项目中的文件更改同步更新到网页端)

```shell
cd PythonNote
docsify serve ./
```


# 专题

文件与终端的交互
- 怎么快速从终端中打开一个文件？
- 怎么从某一个文件快速进入当前文件文件夹的终端？

文件内容与终端的交互
- 怎样快速将文件内容复制到终端运行？
