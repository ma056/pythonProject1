#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/28 1:30 PM 
@process    :
@change :
'''
import array

print(array.typecodes)  # 所有可用的类型
# 1.array.itemsize
f1 = array.array('b')  # signed char int8
print(f1.itemsize)  # 1 代表单个item占用的字节

fb = array.array('B')  # unsigned char uint8
print(fb.itemsize)  # 1

fu = array.array('u', 'hello \u2641')  # wchar_t
print(fu.itemsize)  # 4 注意u类型 It can be 16 bits or 32 bits depending on the platform.

ff = array.array('f', [1, 2, 3, 4, 5])  # float32
print(ff.itemsize)  # 4

# 2.array.typecode
f4 = array.array('f', [1, 2, 3, 4, 5])  # float32
print(f4.typecode)  # 'f'

# 3.array操作
# 3.1 array.append(x)
f4 = array.array('f', [1, 2, 3, 4, 5])  # float32
f4.append(6)
print(f4)
# f4.append("a")  # TypeError: must be real number, not str

# 3.2array.extend(iterable)
# 3.3array.count(x)
f2 = array.array('u', 'hello \u2641')  # array('u', 'hello ♁') #signed char
f2.count("l")  # 2

# 3.4array.index(x[,start[,stop]])
f4 = array.array('f', [1, 2, 3, 4, 5, 3])  # float32
print(f4.index(3))  # 输出索引：2

# 3.5array.insert(i,x)
f5 = array.array('f', [1, 2, 3, 4, 5, 3])
f5.insert(1, 8)
print(f5)

# 3.6 array.pop([i])
f6 = array.array('f', [3, 2, 1, 4, 5])
f6.pop()
f6.pop(2)
print(f6)

# 3.7array.remove(x)
f4 = array.array('f', [1, 2, 3, 4, 5])
f4.remove(3)  # 删除啊的是第一个找到的3这个元素

# 3.8注意报错
# f4 = array.array('f', ["1", "2", "3"])  # float32

# 4转换array
# 4.1array.tobytes()
f4 = array.array('f', [12, 3, 4, 5])
print(f4.tobytes())  # b'\x00\x00@A\x00\x00@@\x00\x00\x80@\x00\x00\xa0@'

# 4.2array.tofile(f)
f4 = array.array('f', [1, 23, 4, 5])
with open('a.bin', 'wb') as f:
    f4.tofile(f)

# 4.3array.tolist()
f4 = array.array('u', "hello \u2641")
u = f4.tounicode()  # 'hello ♁'
print(type(u))

# 5.构建array
# array.frombytes(s)
# array.fromfile(f, n)
f4 = array.array('f', [1, 2, 3, 4, 5, 3])
with open("/tmp/test.bin", 'wb') as f:
    f4.tofile(f)

f = array.array('f')
with open("/tmp/test.bin", 'rb') as fr:
    f.fromfile(fr, 2)  # 每次取2
    f.fromfile(fr, 2)


f4 = array.array('f', ["1", "2", "3"])
with open("./test1.bin",'wb') as f:
    f4.tofile(f)