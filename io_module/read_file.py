import os;

print('当前目录=', os.getcwd())
_path = os.getcwd() + '/test.py'
print('_path=', _path)

try:
  f = open(_path, 'r')
  print(f.read())
except os.error as e:
  print('错误：',e)
finally:
  if f:
    f.close()


with open(_path, 'r') as file:
  print('第二种方式打开文件=', file.read())
  file.close();
