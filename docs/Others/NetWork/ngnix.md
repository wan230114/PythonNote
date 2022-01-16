
配置设置：

/etc/nginx/nginx.conf:

```bash
        location / {
            root /usr/share/nginx/html/PythonNote/;
            disable_symlinks on;
            #index  index.html index.htm;
            autoindex on;       #开启nginx目录浏览功能
            autoindex_exact_size off;   #文件大小从KB开始显示
                        #默认为on，显示出文件的确切大小，单位是bytes。
                         #改为off后，显示出文件的大概大小，单位是kB或者MB或者GB
            autoindex_localtime on;     #显示文件修改时间为服务器本地时间
            charset utf-8,gbk;          #显示中文
            #  limit_conn one 8;        #并发数
            #  limit_rate 100k;         #单个线程最大下载速度，单位KB/s
        }

```