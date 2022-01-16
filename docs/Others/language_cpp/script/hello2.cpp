// #include <iostream>
// using namespace std;
// int main()
// {
//     for (size_t i = 0; i < 1000000; i++)
//     {
//         cout << "Hello, world!" << endl;
//     }
//     return 0;
// }

#include <stdio.h>

int main()
{
    FILE *fp = NULL;

    fp = fopen("log-cpp.txt", "w+");               //第一个逗号前是文件位置。逗号之后是打开文件方式
    for (size_t i = 0; i < 1000000; i++)
    {
        fprintf(fp, "Hello, world!\n"); //逗号之前是一个指针，表明往里面输入。逗号之后fprintf是往文件里面输入
    }
    // fputs("This is testing for fputs...\n", fp);
    fclose(fp); //记得用完关闭文件
}