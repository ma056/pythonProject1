# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : hashlib1.py
@Author : wenjing
@Date : 2022/11/30 17:33
"""
import hashlib

# 检查两个文件是否一致   aa是MD5检查，h是256检查
with open('file_path', 'rb') as f:
    aa = hashlib.md5(f.read()).hexdigest()
    h = hashlib.sha256(f.read()).hexdigest()

# 用于加密相关的操作，代替了md5模块和sha模块，主要提供SHA1，SHA224，SHA256，SHA384，SHA512,MD5算法。
# md5加密
hash = hashlib.md5()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# sha1加密
hash = hashlib.sha1()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# sha256加密  64位
hash = hashlib.sha256()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# sha384加密
hash = hashlib.sha384()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# sha512加密
hash = hashlib.sha512()
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# 加盐’加密  以上加密算法虽然很厉害，但仍然存在缺陷，通过撞库可以反解。所以必要对加密算法中添加自定义key再来做加密。
######  md5 加密 ############
hash = hashlib.md5('python'.encode('utf-8'))
hash.update('admin'.encode('utf-8'))
print(hash.hexdigest())

# hmac加密    hmac内部对我们创建的key和内容进行处理后在加密
import hmac

h1 = hmac.new('python'.encode('utf-8'))
h1.update('helloworld'.encode('utf-8'))
print(h1.hexdigest())

# 获取文件的MD5
import hashlib


def md5sum(filename):
    """
    用于获取文件的md5值
    :param filename: 文件名
    :return: MD5码
    """
    if not os.path.isfile(filename):  # 如果校验md5的文件不是文件，返回空
        return
    myhash = hashlib.md5()
    f = open(filename, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()
