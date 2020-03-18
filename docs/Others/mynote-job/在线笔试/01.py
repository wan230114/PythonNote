"""思想，边展开边查询(python3环境)"""


class Get_values(object):
    """Usage: L_result = Get_values(Data, 1120).get()"""
    def __init__(self, Data, value):
        self.Data = Data  # 嵌套字典的列表数据
        self.value = value  # 需要查找的值
        self.__stat__ = 0   # 记录查找状态
        self.__p_del__ = 0  # 记录枝末状态

    def get(self):
        while not self.__stat__ and Data:
            self.__stat__ = 0
            self.__p_del__ = 0
            L = self._get_values(self.Data)  # 获取结果
            if self.__p_del__:
                Data.pop(0)
        return L

    def _get_values(self, Data):
        """逐个遍历，两个条件终止，1是查找到，2是分支结束"""
        D = Data[0]
        L = [D['name']]  # 初始化
        if D['id'] == self.value:  # 1) 判断id
            self.__stat__ = 1  # print(D['name'], "已找到")
        elif 'children' in D:  # 2) 处理children
            L += self._get_values(D['children'])
            if self.__p_del__:
                if len(D['children']) > 1:
                    D['children'].pop(0)
                else:
                    D.pop('children')
                self.__p_del__ = 0
        else:  # 3) 处理枝末
            self.__p_del__ = 1
        return L


if __name__ == "__main__":
    import requests
    import json
    re = requests.get('https://job.xiyanghui.com/api/q1/json')
    Data = json.loads(re.text)
    L_result = Get_values(Data, 1120).get()
    print(*L_result, sep=' > ')
