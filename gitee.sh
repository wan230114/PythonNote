# https://gitee.com/wan230114/mytools.git
echo "***********"
echo ">拉取中..."
sh Get_gitee.sh

echo
echo "***********"
echo ">上传中..."
read -p "Input this commit: " val echo $val
git add -A
git commit -a -m "`date "+%F  %H:%M:%S"` $val"
git push -u origin master        # 上传仓库到码云
