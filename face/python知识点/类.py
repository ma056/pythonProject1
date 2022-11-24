# coding=utf-8
'''
类的命名：大小写驼峰（TestCase），首字母大写，私有类可用一个下划线开头
https://blog.csdn.net/weixin_42570192/article/details/124090742
'''
'''
给属性指定默认值
'''

# class User():
#     def __init__(self, first_name, last_name, gender, age):
#         self.name = first_name.title() + '--' + last_name.title()
#         self.gender = gender
#         self.age = age
#         self.login_attempts = 0
#
#     def print_login_attempts(self):
#         print('login_attempts in function:' + str(self.login_attempts))
#
#
# user = User('A', 'B', 'male', 3)
# print('name:' + user.name)
# print('gender:' + user.gender)
# print('age:' + str(user.age))
# print('login_attempts:' + str(user.login_attempts))
# user.print_login_attempts()

'''
修改类属性的值
'''
# class User():
#     def __init__(self,first_name,last_name,gender,age):
#         self.name = last_name+'  '+ first_name
#         self.gender = gender
#         self.age = age
#         self.login_attempts = 0
#     def print_login_attempts(self):
#         print('print_login_login_attempts:'+str(self.login_attempts))
#
#     def update_login_attempts(self, value):
#         '''修改属性login_attempts的值'''
#         self.login_attempts = value
#         print('update_login_attempts:'+str(self.login_attempts))
#
#     def increment_login_attempts(self,value):
#         self.login_attempts += value
#         print('increment_login_attempts：'+str(self.login_attempts))
#
# user = User('A', 'B', 'male', 3)
# print('name:' + user.name)
# print('gender:' + user.gender)
# print('age:' + str(user.age))
# print('login_attempts:' + str(user.login_attempts))
# user.print_login_attempts()
# user.update_login_attempts(20)
# print('login_attempts:' + str(user.login_attempts))
# user.increment_login_attempts(30)

'''
类的继承
'''

# class User():
#     '''定义用户类'''
#
#     def __init__(self, first_name, last_name, gender, age):
#         self.name = first_name + ' ' + last_name
#         self.gender = gender
#         self.age = age
#
#     def describe_user(self):
#         # if self.gender == 'male':
#         print('this user name is:' + self.name + 'gender is :' + self.gender + 'age is:' + str(self.age))
#
#     def greet_user(self):
#         print('hello:' + self.name)
#
#
# class Adminstrator(User):
#     '''定义子类Adminstrator 继承父类User'''
#
#     def __init__(self, first_name, last_name, gender, age):
#         '''初始化父类的属性'''
#         super().__init__(first_name, last_name, gender, age)
#         self.identity = 'adminstrator'  # 添加子类的属性
#
#     def greet_amdin(self):  # 添加子类的特有方法
#         print('dear:' + self.identity)
#         print('welcome to login:' + self.name)
#
#
# admin = Adminstrator('A', 'B', 'male', 3)
# admin.greet_user()  # 调用父类的方法
# print('+'*40)
# admin.greet_amdin()  # 调用子类的方法

'''
重写父类的方法
'''


# class User():
#     '''定义用户类'''
#
#     def __init__(self, first_name, last_name, gender, age):
#         self.name = first_name + ' ' + last_name
#         self.gender = gender
#         self.age = age
#
#     def describe_user(self):
#         # if self.gender == 'male':
#         print('this user name is:' + self.name + 'gender is :' + self.gender + 'age is:' + str(self.age))
#
#     def greet_user(self):
#         print('hello:' + self.name)
#
#
# class Administrator(User):
#     def __init__(self, first_name, last_name, gender, age):
#         super().__init__(first_name, last_name, gender, age)
#         self.identity = 'administrator'
#
#     def greet_admin(self):
#         print('dear:' + self.identity)
#         print('welcome to login:' + self.name)
#
#     def describe_user(self):
#         '''重写父类的方法'''
#         print('重写得方法：' + self.name + ' gender:' + self.gender + 'age:' + str(self.age))
#
#
# user = User('A', 'B', 'MALE', 3)
# user.describe_user()
# admin = Administrator('c', 'd', 'female', 4)
# admin.describe_user()

'''
将实例用作属性
'''
class User():
    def __init__(self,first_name,last_name):
        self.name = first_name+'  '+last_name

    def print_name(self):
        print('name: '+self.name)

class Attribute():
    '''定义一个属性类'''
    def __init__(self,gender,age):
        self.gender = gender
        self.age = age

    def describute_attribute(self):
        print('gender: '+self.gender)
        print('age :'+str(self.age))

class Administrator(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.attribute = Attribute('female',3)

admin = Administrator('A','B')
admin.print_name()
admin.attribute.describute_attribute()

'''
类的多继承
'''

# class Zll():
#     def smile(self):
#         print('哈哈哈')
#
#
# class Dcg():
#     def smile(self):
#         print('啊啊啊啊啊')
#
#
# class Lw():
#     def smile(self):
#         print('嘿嘿嘿')
#
#
# class Xz(Zll, Dcg, Lw):
#     def smile(self):  # 重写父类的方法
#         # Dcg().smile()  #调用了父类
#         super(Xz, self).smile()  # 这个自动帮你找到父类的，如果这样写会按继承顺序，Zll、Dcg、Lwy一个一个去找，先在哪个类中找到就先使用哪个类里的smile方法
#         print('呵呵呵')
#
#
# x = Xz()
# x.smile()
