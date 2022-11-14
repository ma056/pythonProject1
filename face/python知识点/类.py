'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：579817333
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
# coding=utf-8
class Zll():
    def smile(self):
        print('哈哈哈')
class Dcg():
    def smile(self):
        print('啊啊啊啊啊')

class Lw():
    def smile(self):
        print('嘿嘿嘿')

class Xz(Zll,Dcg,Lw):
    def smile(self):   #重写父类的方法
        # Dcg().smile()  #调用了父类
        super(Xz,self).smile()  #这个自动帮你找到父类的，如果这样写会按继承顺序，Zll、Dcg、Lwy一个一个去找，先在哪个类中找到就先使用哪个类里的smile方法
        print('呵呵呵')
x = Xz()
x.smile()
