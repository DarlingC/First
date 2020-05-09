import os

# 定义名字有python的数量为0
name_python_numbers = 0

for file in os.scandir('E:\\Desktop\\测试'):
    if 'python' in file.name.lower() and file.is_file():
        name_python_numbers += 1
print(f'总共有{name_python_numbers}个名字为python的文件')
