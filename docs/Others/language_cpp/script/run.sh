time for i in `seq 1 200` ; do echo "Hello, world!" ; done &>log

echo ----- 多次执行
g++ hello.cpp -o hello
time for i in `seq 1 200` ; do ./hello ; done &>log1
time for i in `seq 1 200` ; do ./hello.sh ; done &>log2
time for i in `seq 1 200` ; do ./hello.py ; done &>log3

echo ----- 一次编译，循环去执行
g++ hello2.cpp -o hello2
time ./hello2  &>log1.1
time ./hello2.sh  &>log2.1
time ./hello2.py &>log3.1

wc -l log*
rm log*
