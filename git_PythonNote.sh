#!/usr/bin/bash

tools_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

cd $tools_path
#git clone https://gitee.com/wan230114/PythonNote.git &>>log

while true; do 
  sleep 1; 
  logs=`git pull &>/dev/stdout`
  if [ "$logs" == "Already up-to-date." ]; 
  then
    sleep 0;
  else
    echo >>../log
    date "+%F %H:%M:%S" &>>../log
    echo $logs &>>../log
  fi
done

