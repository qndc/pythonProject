def func(executor):
    print(f'{executor}调用 file1中的方法')

def func1():
    print(f'from导入方式')

if __name__ == '__main__':
    func('file1')