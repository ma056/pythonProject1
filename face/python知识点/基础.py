'''
0、面向对象和面向过程
    面向过程：从上至下，实现功能       实现：函数的创建和调用
    面向对象：将程序看作一组对象的集合，先考虑创建某个类，在类中设定属性和方法，然后创建实例化对象，实现类          实现：类的创建和调用
    面向对象三大特征：封装性：放在对象内部，外部无法访问，继承性：多继承，一个类可以继承多个父类，多态性：一个接口多种实现
http://t.zoukankan.com/guofeng-1016-p-10115230.html
1.Python的六大数据类型：
    数字（Number)，字符串(String)，元组(Tuple)，列表(List)，集合(Set)，字典(Dictionary)
    可变的（不可哈希）：列表、集合、字典（可以进行更改，并且更改后物理地址不会发生改变）
    不可变的（可哈希）：数字、字符串、元组（不可以进行更改，更改后就是一个新的对象了，物理地址发生了变化）
    set操作：
        新增：数字、字符串、元组或者布尔类型（True 和 False）值，不能添加列表、字典、集合这类可变的数据
            a = {1,2,3}
            a.add((1,2))
            print(a)    {(1,2),1,2,3}
        删除：
            a = {1,2,3}
            a.remove(1)
            print(a)
        set集合做交集、并集、差集运算：
            交集：     &  set1={1,2,3} 和 set2={3,4,5}   -->{3}
            并集：     |  set1={1,2,3} 和 set2={3,4,5}   -->{1，2，3，4，5}
            差集：     -  set1={1,2,3} 和 set2={3,4,5}   -->set1-set2->{1,2}    set2-set1->{4,5}
            对称差集：  ^	 set1={1,2,3} 和 set2={3,4,5}   -->{1,2,4,5}   注释：取集合 A 和 B 中不属于 A&B 的元素
    是否可哈希：
        ('asd',[1,2,3])是不可哈希也就是可变数据类型
        检验的方法：hash(('asd',[1,2,3]))

2、解释Python的内置数据结构？
    Python中主要有四种类型的数据结构
    列表：列表是从整数到字符串甚至另一个列表的异构数据项的集合。列表是可变的。列表完成了其他语言中大多数集合数据结构的工作。列表在[ ]方括号中定义。
        例如：a = [1,2,3,4]
        append：在列表末尾添加新元素。
            NumList1 = [1,2,3]
            NumList2 = ['a','b','c']
            NumList1.append(NumList2)
            输出：[1, 2, 3, [‘a’, ‘b’, ‘c’]]
        insert：在列表的特定位置添加元素。
        extend：通过添加新列表来扩展列表。
            NumList1.extend(NumList2)
            输出：[1, 2, 3, ‘a’, ‘b’, ‘c’]
        删除：
             del目标或del(目标)
                eg:
                    del list1
                    del list1[0]
             pop 删除指定下标的数据，如果不指定下标，默认删除最后一个数据
                eg:
                    del_list = list1.pop()  #这里的del_list是被删的元素
                    del_list2 = list2.pop(1)
             remove：移除列表中某个数据的第一个匹配项
                eg:
                    list1.remove('python')
             clear：清楚列表，返回一个空列表
    集合：集合是唯一元素的无序集合。集合运算如联合|，交集&和差异，可以应用于集合。{}用于表示一个集合。
        例如：a = {1,2,3,4}
        remove:使用 remove 方法删除元素时，如果元素不存在集合中，那么程序会报错。
        discard:使用 discard 方法删除元素时，如果元素不存在集合中，那么程序不会报错。
        pop:使用 pop 方法删除集合中的元素时，会自动删除集合中的第一个元素，并返回被删除的元素，如果集合为空，程序报错。
    元组：Python元组的工作方式与Python列表完全相同，只是它们是不可变的。()用于定义元组。
        注意：当要创建的元组中只包含一个元素时，必须带逗号。如果不带逗号会将左右括号默认视为运算符
            例如：a = (1)   type(a)->输出 int
                 a = (1,)   type(a)->输出 tuple
            例如：a =（1,2,3,4）
            **34、元组是不可变的，元组中存一个列表，列表中元素是否可以改变？
            可以**
    字典：字典是键值对的集合。它类似于其他语言中的hash map。在字典里，键是唯一且不可变的对象。
        例如：a = {'number'：[1,2,3,4]}
        删除：
             del可根据“键”删除字典中的元素
                eg:
                    del stu_info['number']
             pop 用于获取指定“键”的值，并将这个“键-值”对从字典中移除。
                eg:
                    A=stu_info.pop('number')
             popitem：用于随机获取一个“键-值”对，并将其删除。
                eg:
                    a=stu_info.popitem()
             clear：清楚字典，返回一个空字典
        38、python 中字典的底层实现原理？
        在Python中，字典是通过散列表（哈希表）实现的。字典也叫哈希数组或关联数组，，所以其本质是数组。

3、浅拷贝与深拷贝的区别？
    浅拷贝：将一个对象的引用拷贝到另一个对象上，若在拷贝中改动，会影响原对象。
    深拷贝：深拷贝将一个对象拷贝到另一个对象中，如果对一个对象作出改变时，不会影响原对象

4、help()内置函数->作用查看函数和详细说明模块
   Dir()内置函数->不带参数时：返回当前范围内的变量、方法和定义的类型列表
               ->带参数时：返回参数的属性、方法和列表

5、python运算符
  (1)算术运算符：
    标准运算符：加减乘除
    整除运算符：//
    取余运算符：%
    幂运算符：2**4->表示2的四次方
  (2)赋值运算符
    直接赋值：=
    链式赋值：a=b=c=10
    参数赋值：a+=b
    系列解包赋值：a,b,c = 1,2,3
  (3)比较运算符（!=   is not）
    == 比较两个对象或值的相等性
    is运算符用于检查两个对象是否属于同一内存对象。
  (4)逻辑运算符：and, or, not

6、什么是lambda函数？
    Lambda函数是不带名称的单行函数，可以具有n个参数，但只能有一个表达式。也称为匿名函数。
    lambda 参数：表达式     lambda 函数可接受任意数量的参数，但只能有一个表达式
    eg: a=[(lambda x:x*x)(x) for x in range(5)]
    eg1、字典根据键从小到大排序
        dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
        print(dict(sorted(dic.items(),key=lambda x:x[0],reverse=False)))
    eg2、从给定列表中取出所有的偶数和奇数
        a = [1,2,3,4,5,6,7,8,9,10]
        odd, even = [el for el in a if el % 2==1], [el for el in a if el % 2==0]
        print(odd,even)
        > ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    eg3
        [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
        列表推导式：
        print([j for i in li for j in i])
        numpy方法:
        import numpy as np
        print(np.array(li).flatten().tolist())

7、*和**区别：
 python函数传递参数的方式有两种：位置参数、关键词参数
 *args：表示任何多个无名参数，本质是一个tuple
 **kwargs：表示关键字参数，本质是一个dict
 注意：：：：：：：tuple一个元素时逗号:  (1,)
 两个都是可变参数，同时使用，必须*args要在**kwargs前
 eg:
    def fun(*args,**kwargs):
        print('args=',args)
        print('kwargs=',kwargs)
    fun(1,2,3,4,A='a',B= 'b')
    输出：
    args=(1,2,3,4)
    kwargs = {'A':'a','B':'b'}


8、 Map ,reduce,filter
    map函接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
        例如：
        def f(x):
             return x * x
        r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        list(r)
        输出：[1, 4, 9, 16, 25, 36, 49, 64, 81]
    reduce函数，从左到右对一个序列的项累计的应用：有两个参数的函数，以此合并序列到一个单一值（累加乘）
        例如：
        from functools import reduce
        def add(x, y):
            return x + y
        reduce(add, [1, 3, 5, 7, 9])
        输出：25
    filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
        例如：
        def is_odd(n):
            return n % 2 == 1
        list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
        输出: [1, 5, 9, 15]

9、Python中使用的zip函数是什么？
    zip函数获取可迭代对象，将它们聚合到一个元组中，然后返回结果。
    zip()函数的语法是zip(*iterables)
    numbers = [1, 2, 3]
    string = ['one', 'two', 'three']
    result = zip(numbers,string)
    print(set(result))
    -------------------------------------
    {(3, 'three'), (2, 'two'), (1, 'one')}


10.with
    with语句的使用，可以简化了代码，有效避免资源泄露的发生
    打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open
    写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close

11、Python中的装饰器是什么？**
    开放封闭原则
    开放：指的是对拓展功能是开放的
    封闭：指的是对修改源代码是封闭的
    它用于向现有代码添加功能。这也称为元编程，因为程序的一部分在编译时会尝试修改程序的另一部分。
    def addition(func):
        def inner(a,b):
            print("numbers are",a,"and",b)
        return func(a,b)
    return inner

    @addition
    def add(a,b):
       print(a+b)
    add(5,6)
    输出：
    numbers are 5 and 6
    sum: 11

12、闭包 和 nonlocal关键字
    nonlocal关键字：该代码就可以很好的解释了，第一行的count和a()函数中的count是两个变量，而a()函数中的count变量只是在该函数内部起作用，因为它是一个局部变量。
    nonlocal只能在封装函数中使用，在外部函数先进行声明，在内部函数进行nonlocal声明，这样在b()函数中的count与a()中的count是同一个变量。
        count = 1
        def a():
            count = 'a函数里面'  　　#如果不事先声明，那么函数b中的nonlocal就会报错
            def b():
                nonlocal count
                print(count)
                count = 2
            b()
            print(count)

        if __name__ == '__main__':
            a()
            print(count)

13、闭包和装饰器：
什么是闭包？
闭包就是外部函数中定义了一个内部函数，当外部函数返回内部函数对象（注意是函数对象）时，程序接收了内部函数的定义（此时并未被执行），当再次执行这个返回值时，这个被返回的函数才能被执行。
闭包和装饰器的区别：闭包传递的是变量，而装饰器传递的是函数，除此之外没有任何区别，或者说装饰器是闭包的一种，它只是传递函数的闭包。
创建一个闭包必须满足以下几点:
    必须有一个内嵌函数
    内嵌函数必须引用外部函数中的变量
    外部函数的返回值必须是内嵌函数
eg1:
    def xiaoai(func):
        def say():
            print("我在")
            func()
            print("再见")
    return say
    @xiaoai
    def answer():
        q = input("咋来，你说：")
        print(f'对不起，不理解{q}是啥意思')
    answer()


    def answer():
        q = input("咋来，你说：")
        print(f'对不起，不理解{q}是啥意思')

    def xiaoai(func):
        def say():
            print("我在")
            func()
            print("再见")
        return say
    a = xiaoai(answer)
    a()
eg2.# 2、闭包
        def answer():
            q = input("咋来，你说：")
            print(f'对不起，不理解{q}是啥意思')

        def performance():
            q = input("要我表演啥：")
            print(f'表演一个{q}')
        def xiaoai(func):
            def say():
                print("我在")
                func()
                print("再见")
            return say
        # a = xiaoai(answer)
        # a()
        a = xiaoai(performance)
        a()
        # 装饰器
        def answer():
            q = input("咋来，你说：")
            print(f'对不起，不理解{q}是啥意思')
        def performance():
            q = input("要我表演啥：")
            print(f'表演一个{q}')
        def xiaoai(func):
            def say():
                print("我在")
                func()
                print("再见")
            return say
        @xiaoai
        def answer():
            q = input("咋来，你说：")
            print(f'对不起，不理解{q}是啥意思')
        answer()

14、python 常见的魔法方法
    __init__
    __new__
    __call__
    __str__
    __repr__

15、简述面向对象中__new__和__init__区别？
    创建一个类的过程是分为两步的，一步是创建类的对象，还有一步就是对类进行初始化。：
    __new__先被调用，__new__返回值将传递给__init__方法的第一个参数，然后__init__被调用
    （1）__new__是在实例创建之前呗调用的，用于实例创建，然后返回该实例对象，是静态方法
    （2）__init__是当实例对象创建完成后被调用的，用于初始化一个类的实例，是实例方法

16、GIL全局解释器锁
    （1）作用：限制多进程同时执行，保证同一时间内只有一个线程在执行，
    线程非独立，在同一进程里线程是数据共享，当各个线程访问数据资源时会出现'竞争'状态，
    即数据可能会同时被多个线程占用，造成数据混乱，引起互斥锁确保只有一个线程是从头到尾完整的执行的
    （2）gil它是cpython解析器的特征，不是python的，它要求线程执行前，需要获取gil锁
    （3）线程释放gil锁的情况：
        在io操作等可能引起阻塞的system call之前，可以暂时释放锁，但执行完成后，必须从新获取锁
        python3。0使用计时器（达到执行时间的时候，释放锁）
    （4）多线程比单线程性能好，因为遇到io阻塞会自动释放锁，这样在线程阻塞的情况下

17、类和对象有什么区别？
    用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例
    类(Class)被视为对象的蓝图。
    使用class关键字可以创建了一个类。一个类包含变量和成员组合，称为类成员。
    对象(Object)是真实存在的实体。
    例如：obj = num()
    使用类的对象，我们可以访问类的所有成员，并对其进行操作。
    self、你对Python类中的self有什么了解？
        self表示类的实例。
        通过使用self关键字，我们可以在Python中访问类的属性和方法。
        注意，在类的函数当中，必须使用self，因为类中没有用于声明变量的显式语法。

40、python 装饰器函数装饰器与类装饰器
    函数装饰器：函数能作为参数传递给其他函数，可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内；
    类装饰器：类具有__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法；
    应用场景： 插入日志、性能测试、事务处理、缓存、权限校验等

18、类-带括号与不带括号的区别
    python3中创建类的方式有两种一种是带括号，一种是不带括号
    可以不带括号，也可以带，也可以显示继承object，如果带个()空括号，其实也是隐士的继承了object。这三种方式是相等的
    类的实例化（python的类，带括号是实例化，不带括号是赋值）
    不带括号实例化
    class tea:
        def __init__(self):
            print('111')
    a = tea
    print(id(tea))
    print(id(a))    一样·
    带括号实例化
    b = tea()
    print(id(tea()))
    print(id(b))    不一样


**33、多线程、多进程和协程的区别与联系**
    多线程：
    线程是进程的一个实体，是CPU进行调度的最小单位，他是比进程更小能独立运行的基本单位。
    线程基本不拥有系统资源，只占用一点运行中的资源（如程序计数器,一组寄存器和栈），但是它可以与同属于一个进程的其他线程共享全部的资源。
    提高程序的运行速率，上下文切换快，开销比较少，但是不够稳定，容易丢失数据，形成死锁。
    多进程：
    进程是系统进行资源分配的最小单位，每个进程都有自己的独立内存空间，不用进程通过进程间通信来通信。
    但是进程占据独立空间，比较重量级，所以上下文进程间的切换开销比较大，但是比较稳定安全。
    协程：
    协程：是更小的执行单位，是一种轻量级的线程，协程的切换只是单纯的操作CPU的上下文，所以切换速度特别快，且耗能小。
    gevent是第三方库，通过greenlet实现协程，其基本思想是：
    当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。

11.实例方法 静态方法
    实例方法
    定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
    调用：只能由实例对象调用。
    类方法
    定义：使用装饰器@classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
    调用：类和实例对象都可以调用。
    静态方法
    定义：使用装饰器@staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
    调用：类和实例对象都可以调用。

12.可迭代对象和迭代器
    区别：
    可迭代对象：Iterable,可以直接作用于for循环的对象【可以使用for循环遍历其中元素的对象】， 如：list,tuple,dict,set，str,range(),生成器等
    迭代器:Iterator,可以直接作用于for循环,或者可以通过next()获取下一个元素的对象， 如：生成器
    联系：
    迭代器一定是可迭代对象，可迭代对象不一定是迭代器
    但是，可以通过系统功能iter()将不是迭代器的可迭代对象转换为迭代器

12.2 生成器
    使用了yield的函数被称为生成器
    生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器
    在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行
    例如：
        def testyield():
            for i in range(5):
                yield i * i
        generator = testyield()
        for i in generator:
            print(i)
        等同于：for i in range(5):
                  print(next(generator))


43、为什么是三次握手 而不是两次呢？
防止出现请求超时脏链接

44、Python是如何进行内存管理的
    答:从三个方面来说,一对象的引用计数机制,二垃圾回收机制,三内存池机制
    一、对象的引用计数机制
        Python内部使用引用计数，来保持追踪内存中的对象，所有对象都有引用计数。
        引用计数增加的情况：
            1，一个对象分配一个新名称
            2，将其放入一个容器中（如列表、元组或字典）
        引用计数减少的情况：
            1，使用del语句对对象别名显示的销毁
            2，引用超出作用域或被重新赋值
        Sys.getrefcount( )函数可以获得对象的当前引用计数
        多数情况下，引用计数比你猜测得要大得多。对于不可变数据（如数字和字符串），解释器会在程序的不同部分共享内存，以便节约内存。
    二、垃圾回收
        1，当一个对象的引用计数归零时，它将被垃圾收集机制处理掉。
        2，当两个对象a和b相互引用时，del语句可以减少a和b的引用计数，并销毁用于引用底层对象的名称。
            然而由于每个对象都包含一个对其他对象的应用，因此引用计数不会归零，对象也不会销毁。（从而导致内存泄露）。
            为解决这一问题，解释器会定期执行一个循环检测器，搜索不可访问对象的循环并删除它们。
    三、内存池机制
        Python提供了对内存的垃圾收集机制，但是它将不用的内存放到内存池而不是返回给操作系统。
        1，Pymalloc机制。为了加速Python的执行效率，Python引入了一个内存池机制，用于管理对小块内存的申请和释放。
        2，Python中所有小于256个字节的对象都使用pymalloc实现的分配器，而大的对象则使用系统的malloc。
        3，对于Python对象，如整数，浮点数和List，都有其独立的私有内存池，对象间不共享他们的内存池。也就是说如果你分配又释放了大量的整数，用于缓存这些整数的内存就不能再分配给浮点数。
'''


# https://blog.csdn.net/weixin_44536215/article/details/125249874
# https://zhuanlan.zhihu.com/p/512261354
# 1。
# def make_averager():
#     nums = []
#     print(f'======{nums}')
#
#     def averager(n):
#         print(f'------{n}')
#         nums.append(n)
#         print(f'nums:{nums}----{sum(nums)}')
#         return sum(nums) / len(nums)
#
#     return averager
#
#
# averager = make_averager()
# print(averager(10)) #10。0
# print(averager(20)) # 15。0
# 2。
# num = 10
#
#
# def outter():
#     num = 20
#
#     def inner():
#         num = 30
#         print('inner:', num)  # 10 20 30-----》 30
#
#     print("outter:", num)  # 10 20 ----》20
#     return inner
#
#
# f = outter()
# f()
# print("global:", num)  # 10

# def deco(func):
#     def inner():
#         print(f"耗子尾汁")
#
#     return inner
#
#
# # 装饰器将target替换成了inner
#
# @deco
# def target():
#     print("年轻人，不讲武德！")
#
#
# target()


# 闭包
# def a():
#     series = []
#     def b(value):
#         print(f'{value}----')
#         series.append(value)
#         total = sum(series)
#         return total/len(series)
#     return b
#
# avg = a()
# print(avg(10))

# 1、
# def print_msg(msg):
#     print(msg + "111")
#
#     def printer():
#         print('1123')
#
#     return printer  # 这变了
#
#
# another = print_msg("Hello")
# another()


def xiaoai(func):
    def say():
        print("我在")
        func()
        print("再见")
    return say
@xiaoai
def answer():
    q = input("咋来，你说：")
    print(f'对不起，不理解{q}是啥意思')
answer()
#
#
# def answer():
#     q = input("咋来，你说：")
#     print(f'对不起，不理解{q}是啥意思')
#
# def xiaoai(func):
#     def say():
#         print("我在")
#         func()
#         print("再见")
#     return say
a = xiaoai(answer)
a()


dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
print(dict(sorted(dic.items(),key=lambda x :x[0])))
print(dict(sorted(dic.items(),key=lambda x:x[0],reverse=False)))


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1


for n in fab(5):
    print(n)
import glob
print(glob.glob('*'))