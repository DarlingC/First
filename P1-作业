import os

# 定义文件路径用来测试
files = os.scandir('E:\\Desktop\\测试')
# 定义测试文件夹下包含文件名称列表，初始为空
list_ = []
# 定义名字有python的数量为0
name_python_numbers = 0
# （找出当前文件夹下所有非文件夹的文件）将文件夹中所有文件的名称输入到 list_
for file in files:
    if file.is_file():
        list_.append(file.name)
# 遍历所有文件的名字
for name in list_:
    # 所有名字都变为小写，如果'python'在这个里边，则数量+1
    if 'python' in name.lower():
        name_python_numbers += 1
print(f'总共有{name_python_numbers}个名字为python的文件')
