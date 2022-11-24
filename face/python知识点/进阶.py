'''
1.多线程和多进程：
官方文档： https://docs.python.org/3.9/library/multiprocessing.html?highlight=from%20multiprocessing%20import%20pool
线程池和进程池：https://blog.csdn.net/weixin_38819889/article/details/127251104
知乎：https://zhuanlan.zhihu.com/p/490353142
csdn: https://blog.csdn.net/zong596568821xp/article/details/99678390
多线程
1.1 进程vs线程
    进程（process）指的是正在运行的程序的实例，理解就是：进行中的程序。程序是一个没有生命的实体，只有处理器执行它的时候才能成为一个活动的实体，称之为进程
    线程（thread）包含于进程之中，是操作系统能够进行运算调度的最小单元。一条进程中可以并发多个线程，而同一条线程将共享该进程中的全部系统资源。
    每个进程都有自己独立的地址空间、内存和数据栈，因此进程之间通讯不方便，要是用进程间通讯。而同一个进程中的线程共享资源，因此线程间通讯非常方便，但要注意数据同步与互斥的问题。
    虽然一条进程中可以并发多个线程，但是对于单核CPU而言，同一时间CPU只能运行一个线程
1.2 thread vs threading
    Python处理线程的模块有两个：thread和threading。
    Python 3已经停用了thread模块[3]，并改名为_thread模块。
    Python 3在_thread模块的基础上开发了更高级的threading模块，因此以下的讲解都是基于threading模块
1.3 创建一个线程
    eg:现在我准备创建两个线程，一个线程每隔一秒打印一个“1”，另一个线程每隔2秒打印一个“2”，如何创建并执行呢？两种方法如下：
    func1:  注意args传递的本质是元组，当只有一个元素时注意逗号：（1,）
        import threading
        import time

        def run(n):
            while True:
                print(n)
                time.sleep(n)

        if __name__ == '__main__':
            t1 = threading.Thread(target=run, args=(1,))
            t2 = threading.Thread(target=run, args=(2,))
            t1.start()
            t2.start()
    func2:
        import threading

        class MyThread(threading.Thread):
            def __init__(self, n):
                super(MyThread, self).__init__()  # 重构run函数必须要写
                # super().__init__()  # 注意：一定要调用父类的初始化函数，否则否发创建线程
                self.n = n

            def run(self):
                while True:
                    print("current task：", self.n)

        if __name__ == "__main__":
            t1 = MyThread("thread 1")
            t2 = MyThread("thread 2")
            t1.start()
            t2.start()
1.4 主线程和子线程
    好那么问题来了：当我创建了线程1并开始执行的时候，程序却告诉我有2个活跃的线程呢？同样地，我最终只创建了2个线程，为什么程序却告诉我有3个活跃的线程呢？
        让我们回到进程和线程的定义，当我们开始执行这个程序的时候，这个程序成为一个“有生命的”进程，进程至少有一个线程，这个线程就是主线程。
        当程序执行到第一次t.start()的时候，程序创建了一个子线程，此时活跃的线程个数是2。
        进一步，当执行第二次t.start()的时候，程序又创建了一个子线程，因此最终活跃的线程个数是3。
        结论：每个进程本就存在一个主线程，在创建线程的数量从1开始累加
        注意每个进程只有一个主线程。
    import time
    import threading

    class MyThread(threading.Thread):

        def __init__(self, n):
            self.n = n
            super().__init__()

        def run(self) -> None:
            while True:
                _count = threading.active_count()
                print(self.n, f"当前活跃的线程个数：{_count}")
                time.sleep(self.n)

    for i in range(1, 3):
        t = MyThread(i)
        t.start()
1.5 线程合并
    join()会使主线程进入等待状态（阻塞），直到调用join()方法的子线程运行结束。同时你也可以通过设置timeout参数来设定等待的时间，如：
    eg:
    import time
    import threading

    class MyThread(threading.Thread):

        def __init__(self, n):
            self.n = n
            super().__init__()

        def run(self) -> None:
            while True:
                _count = threading.active_count()
                print(f"线程-{self.n}", f"当前活跃的线程个数：{_count}")
                time.sleep(self.n)

    for i in range(1, 3):
        t = MyThread(i)
        t.start()
        t.join(3)
1.6 互斥锁
    其中，锁定方法acquire可以有一个超时时间的可选参数timeout。
    如果设定了timeout，则在超时后通过返回值可以判断是否得到了锁，从而可以进行一些其他的处理
    import time
    import threading

    num = 0
    mutex = threading.Lock()
    class MyThread(threading.Thread):
        def run(self):
            global num
            time.sleep(1)
            if mutex.acquire(1):
                num = num + 1
                msg = self.name + ':num value is ' + str(num)
                print(msg)
                mutex.release()

    if __name__ == '__main__':
        for i in range(5):
            t = MyThread()
            t.start()
1.7 可重入锁（递归锁）
    为了满足在同一线程中多次请求同一资源的需求，Python提供了可重入锁（RLock）。
    RLock内部维护着一个Lock和一个counter变量，counter记录了acquire 的次数，从而使得资源可以被多次require。
    直到一个线程所有的acquire都被release，其他的线程才能获得资源。
    eg:#创建 RLock
    mutex = threading.RLock()

    class MyThread(threading.Thread):
        def run(self):
            if mutex.acquire(1):
                print("thread " + self.name + " get mutex")
                time.sleep(1)
                mutex.acquire()
                mutex.release()
                mutex.release()
1.8 Timer计时器
    通过threading.Timer类可以实现n秒后执行某操作。注意一个timer对象相当于一个新的子线程。
    for i in range(1, 5):
        t = MyThread(i)
        if i == 4:
            timer = Timer(0.1, t.start)       # 5秒后再开始线程4
            timer.start()
        else:
            t.start()
多进程：
2.1 创建多进程
    func1:
        from multiprocessing import Process

        def show(name):
            print("Process name is " + name)

        if __name__ == "__main__":
            proc = Process(target=show, args=('subprocess',))
            proc.start()
            proc.join()
    func2：
        from multiprocessing import Process
        import time
        class MyProcess(Process):
            def __init__(self, name):
                super(MyProcess, self).__init__()
                self.name = name
            def run(self):
                print('process name :' + str(self.name))
                time.sleep(1)
        if __name__ == '__main__':
            for i in range(3):
                p = MyProcess(i)
                p.start()
            for i in range(3):
                p.join()
2.2多进程通信
    进程之间不共享数据的。如果进程之间需要进行通信，则要用到Queue模块或者Pipe模块来实现
    queue:
        queue是多进程安全的队列，可以实现多进程之间的数据传递。它主要有两个函数put和get
        put()用于插入数据到队列中，put还有两个可选参数：blocked和timeout。如果blocked为True(默认值)，并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。
            如果超时，会抛出queue.Full异常。如果blocked为False，但该queue已满，会立即抛出queue.Full异常。
        get()可以从队列读取并且删除一个元素。同样get有两个可选参数：blocked和timeout。若blocked为True，且timeout为正值，那么在等待时间内没有取到任何元素，会抛出异常queue.empty.
            若blocked为False，有两种情况存在，若queue有一个值可用，则立即返回该值，否则，若队列为空，立即抛出queue.empty异常。
        eg：
            from multiprocessing import Process, Queue
            def put(queue):
                queue.put('queue用法')
                queue.put('11')

            if __name__ == '__main__':
                queue = Queue()
                pro = Process(target=put, args=(queue,))
                pro.start()
                print(queue.get())
                print(queue.get())
                pro.join()
    Pipe
        Pipe的本质是进程之间的用管道数据传递，而不是数据共享，这和socket有点像。
        pipe()返回两个连接对象分别表示管道的两端，每端都有send()和recv()函数。
        若两个进程试图在同一时间的同一端进行读取和写入那么，这可能会损坏管道中的数据
        eg:
            from multiprocessing import Process, Pipe
            def show(conn):
                conn.send('pipe用法')
                conn.close()

            if __name__ == '__main__':
                parent_conn, child_conn = Pipe()    #管道的两端parent_conn, child_conn
                pro = Process(target=show, args=(parent_conn,))
                pro.start()
                print(child_conn.recv())
                pro.join()
'''
'''
线程池进程池
官网：https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor
csdn:https://blog.csdn.net/weixin_38819889/article/details/127251104
1.为什么要使用线程池？
    系统启动一个新线程的成本是比较高的，因为它涉及与操作系统的交互。在这种情形下，使用线程池可以很好地提升性能，尤其是当程序中需要创建大量生存期很短暂的线程时，更应该考虑使用线程池。
    线程池在系统启动时即创建大量空闲的线程，程序只要将一个函数提交给线程池，线程池就会启动一个空闲的线程来执行它。
    当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成空闲状态，等待执行下一个函数。
    此外，使用线程池可以有效地控制系统中并发线程的数量。当系统中包含有大量的并发线程时，会导致系统性能急剧下降，甚至导致 Python 解释器崩溃，而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数。
2.线程池和进程池的介绍
    线程池的基类是 concurrent.futures 模块中的 Executor，Executor 提供了两个子类，即 ThreadPoolExecutor 和 ProcessPoolExecutor，
    其中 ThreadPoolExecutor 用于创建线程池，而 ProcessPoolExecutor 用于创建进程池。
    如果使用线程池/进程池来管理并发编程，那么只要将相应的 task 函数提交给线程池/进程池，剩下的事情就由线程池/进程池来搞定。
3.submit-> Executor.submit(fn, *args, **kwargs)
3.1 ThreadPoolExecutor线程池使用submit()方法
    from concurrent.futures import ThreadPoolExecutor
    import time
    
    # 参数times用来模拟网络请求的时间
    def get_html(times):
        time.sleep(times)
        print("get page {}s finished".format(times))
        return times
    
    executor = ThreadPoolExecutor(max_workers=2)
    # 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
    task1 = executor.submit(get_html, (3))
    task2 = executor.submit(get_html, (2))
    # done方法用于判定某个任务是否完成
    print(task1.done())
    # cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
    print(task2.cancel())
    time.sleep(4)
    print(task1.done())
    # result方法可以获取task的执行结果
    print(task1.result())
    
    # 执行结果
    # False  # 表明task1未执行完成
    # False  # 表明task2取消失败，因为已经放入了线程池中
    # get page 2s finished
    # get page 3s finished
    # True  # 由于在get page 3s finished之后才打印，所以此时task1必然完成了
    # 3     # 得到task1的任务返回值
    解释：
        ThreadPoolExecutor构造实例的时候，传入max_workers参数来设置线程池中最多能同时运行的线程数目。
        使用submit函数来提交线程需要执行的任务（函数名和参数）到线程池中，并返回该任务的句柄（类似于文件、画图），注意submit()不是阻塞的，而是立即返回。
        通过submit函数返回的任务句柄，能够使用done()方法判断该任务是否结束。上面的例子可以看出，由于任务有2s的延时，在task1提交后立刻判断，task1还未完成，而在延时4s之后判断，task1就完成了。
        使用cancel()方法可以取消提交的任务，如果任务已经在线程池中运行了，就取消不了。这个例子中，线程池的大小设置为2，任务已经在运行了，所以取消失败。如果改变线程池的大小为1，那么先提交的是task1，task2还在排队等候，这是时候就可以成功取消。
        使用result()方法可以获取任务的返回值。查看内部代码，发现这个方法是阻塞的。

3.2 ProcessPoolExecutor进程池使用submit()方法
    import time
    from concurrent.futures import ProcessPoolExecutor, wait
    
    def fib(n):
        if n <= 2:
            return 1
        return fib(n - 1) + fib(n - 2)
    
    def execute_process():
        start = time.time()
        numbers = list(range(30, 40))
        with ProcessPoolExecutor(max_workers=4) as executor:
            futures = []
            for num in numbers:
                task = executor.submit(fib, num)
                futures.append(task)
            wait(futures)
            for num, futures in zip(numbers, futures):
                print(f'fib({num}) = {futures.result()}')
        print(f'COST:{time.time() - start}')
    
    
    if __name__ == '__main__':
        execute_process()
    解释：
        Future 提供了如下方法：
        cancel()：取消该 Future 代表的线程任务。如果该任务正在执行，不可取消，则该方法返回 False；否则，程序会取消该任务，并返回 True。
        cancelled()：返回 Future 代表的线程任务是否被成功取消。
        running()：如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True。
        done()：如果该 Funture 代表的线程任务被成功取消或执行完成，则该方法返回 True。
        result(timeout=None)：获取该 Future 代表的线程任务最后返回的结果。如果 Future 代表的线程任务还未完成，该方法将会阻塞当前线程，其中 timeout 参数指定最多阻塞多少秒。
        exception(timeout=None)：获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None。
        add_done_callback(fn)：为该 Future 代表的线程任务注册一个“回调函数”，当该任务成功完成时，程序会自动触发该 fn 函数。
        
4.as_completed和result
    上面虽然提供了判断任务是否结束的方法，但是不能在主线程中一直判断啊。
    有时候我们是得知某个任务结束了，就去获取结果，而不是一直判断每个任务有没有结束。这是就可以使用as_completed方法一次取出所有任务的结果
4.1 ThreadPoolExecutor
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import time
    
    # 参数times用来模拟网络请求的时间
    def get_html(times):
        time.sleep(times)
        print("get page {}s finished".format(times))
        return times
    
    executor = ThreadPoolExecutor(max_workers=2)
    urls = [3, 2, 4] # 并不是真的url
    all_task = [executor.submit(get_html, (url)) for url in urls]
    
    for future in as_completed(all_task):
        data = future.result()
        print("in main: get page {}s success".format(data))
    解释：
        as_completed()方法是一个生成器，在没有任务完成的时候，会阻塞，在有某个任务完成的时候，会yield这个任务，就能执行for循环下面的语句，然后继续阻塞住，循环到所有的任务结束。从结果也可以看出，先完成的任务会先通知主线程。
        前面程序调用了 Future 的 result() 方法来获取线程任务的运回值，但该方法会阻塞当前主线程，只有等到钱程任务完成后，result() 方法的阻塞才会被解除。   
        如果程序不希望直接调用 result() 方法阻塞线程，则可通过 Future 的 add_done_callback() 方法来添加回调函数，该回调函数形如 fn(future)。当线程任务完成后，程序会自动触发该回调函数，并将对应的 Future 对象作为参数传给该回调函数。
4.2 使用 add_done_callback() 方法来获取线程任务的返回值
    from concurrent.futures import ThreadPoolExecutor
    import threading
    import time
    
    # 定义一个准备作为线程任务的函数
    def action(max):
        my_sum = 0
        for i in range(max):
            print(threading.current_thread().name + '  ' + str(i))
            my_sum += i
        return my_sum
    # 创建一个包含2条线程的线程池
    with ThreadPoolExecutor(max_workers=2) as pool:
        # 向线程池提交一个task, 50会作为action()函数的参数
        future1 = pool.submit(action, 50)
        # 向线程池再提交一个task, 100会作为action()函数的参数
        future2 = pool.submit(action, 100)
        def get_result(future):
            print(future.result())
        # 为future1添加线程完成的回调函数
        future1.add_done_callback(get_result)
        # 为future2添加线程完成的回调函数
        future2.add_done_callback(get_result)
        print('--------------')
    解释：
        上面主程序分别为 future1、future2 添加了同一个回调函数，该回调函数会在线程任务结束时获取其返回值。      
        主程序的最后一行代码打印了一条横线。由于程序并未直接调用 future1、future2 的 result() 方法，因此主线程不会被阻塞，可以立即看到输出主线程打印出的横线。
        接下来将会看到两个新线程并发执行，当线程任务执行完成后，get_result() 函数被触发，输出线程任务的返回值。        
        另外，由于线程池实现了上下文管理协议（Context Manage Protocol），因此，程序可以使用 with 语句来管理线程池，这样即可避免手动关闭线程池，如上面的程序所示。
5.map
除了上面的as_completed方法，还可以使用executor.map方法
5.1 ThreadPoolExecutor线程池使用map()方法
    from concurrent.futures import ThreadPoolExecutor
    import time
    
    # 参数times用来模拟网络请求的时间
    def get_html(times):
        time.sleep(times)
        print("get page {}s finished".format(times))
        return times
    
    executor = ThreadPoolExecutor(max_workers=2)
    urls = [3, 2, 4] # 并不是真的url
    
    for data in executor.map(get_html, urls):
        print("in main: get page {}s success".format(data))
    解释：
        使用map方法，无需提前使用submit方法，map方法与python标准库中的map含义相同，都是将序列中的每个元素都执行同一个函数。
        上面的代码就是对urls的每个元素都执行get_html函数，并分配各线程池。
        可以看到执行结果与上面的as_completed方法的结果不同，输出顺序和urls列表的顺序相同，就算2s的任务先执行完成，也会先打印出3s的任务先完成，再打印2s的任务完成。
5.2 ProcessPoolExecutor进程池使用map()方法
    import time
    from concurrent.futures import ProcessPoolExecutor
    
    def fib(n):
        if n <= 2:
            return 1
        return fib(n - 1) + fib(n - 2)
        
    def execute_process():
        start = time.time()
        numbers = list(range(30, 40))
        with ProcessPoolExecutor(max_workers=4) as executor:
            result = executor.map(fib, numbers)
            # print(f'result:{list(result)}')  # 猜测生成器取完数据后就为空了
            for num, value in zip(numbers, result):
                print(f'fib({num}) = {value}')
        print(f'COST: {time.time() - start}')
        
    if __name__ == '__main__':
        execute_process()

6.wait
    from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED
    import time
    
    # 参数times用来模拟网络请求的时间
    def get_html(times):
        time.sleep(times)
        print("get page {}s finished".format(times))
        return times
    
    executor = ThreadPoolExecutor(max_workers=2)
    urls = [3, 2, 4] # 并不是真的url
    all_task = [executor.submit(get_html, (url)) for url in urls]
    wait(all_task, return_when=ALL_COMPLETED)
    print("main")
    # 执行结果 
    # get page 2s finished
    # get page 3s finished
    # get page 4s finished
    # main
    解释：wait方法接收3个参数，等待的任务序列、超时时间以及等待条件。等待条件return_when默认为ALL_COMPLETED，表明要等待所有的任务都结束。
    可以看到运行结果中，确实是所有任务都完成了，主线程才打印出main。等待条件还可以设置为FIRST_COMPLETED，表示第一个任务完成就停止等待。
    
'''
# eg:
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4]  # 并不是真的url
all_task = [executor.submit(get_html, (url)) for url in urls]

for future in as_completed(all_task):
    data = future.result()  # 这里的data是get_htmlreturn的值
    print("in main: get page {}s success".format(data))

# eg:和上面得区别就是map这个顺序        可以看到执行结果与上面的as_completed方法的结果不同，输出顺序和urls列表的顺序相同，就算2s的任务先执行完成，也会先打印出3s的任务先完成，再打印2s的任务完成。
from concurrent.futures import ThreadPoolExecutor
import time


def get_html(times):
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
urls = [3, 2, 4]  # 并不是真的url

for data in executor.map(get_html, urls):
    print("in main: get page {}s success".format(data))

# eg:
from multiprocessing import Pool


def f(x):
    return x * x


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))


'''
1.yield from 可以简化for循环里的yield表达式
    def gene():
        for c in 'AB':
            yield c
        for i in range(3):
            yield i
    def gene1():
        yield from 'ab'
        yield from range(3)
    if __name__ == '__main__':
        print(list(gene()))
        print(list(gene1()))
2.通过yield from 链接可迭代对象
    def chain(*args):
        for i in args:
            # for m in i:
            #  yield m
            yield from i
    p = list(chain("1234", "AB", [1, 2, 3, 4, 5]))
    print(p)
3.扁平化处理嵌套型的数据
    from collections import Iterable
    def flatten(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                yield from flatten(x)
            else:
                yield x
    
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    
    # Produces 1 2 3 4 5 6 7 8
    for x in flatten(items):
        print(x)
    
    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)
4.使用yeild from写一个异步爬虫
    import requests
    from collections import namedtuple  ① 
    Response = namedtuple("rs", 'url status') ②
       
    # 子生产器
    def fetch(): ③
        res=[]
        while 1:
            url = yield ④
            if url is None: ⑤
                break
            req = requests.get(url)
            res.append(Response(url=url, status=req.status_code))
        return res
    
    #委派生成器
    def url_list(l, key):
        while 1: ⑥
            l[key] = yield from fetch() ⑦
    
    #调用方
    def main():
        l = {}
        u = ["http://www.baidu.com", "http://www.cnblogs.com"]
        for index, url in enumerate(u):
            if index == 0:
                ul = url_list(l, index)
                next(ul) ⑧
            ul.send(url)⑨
        ul.send(None)⑩
        return l 
    
    if __name__ == '__main__':
        res = main()
        print(res)
    解读：
    ① 引入一个具名元组,可以后面实现一个简单的类。
    ② 对请求参数做一个格式化处理，后面通过获取属性即可。
    ③一个协程，通过requests模块可以发起网络请求。
    ④main函数的发送的值绑定到这里的url上
    ⑤ url为None即没有url的时候结束循环的。
    ⑥这个循环每次都会新建一个fetch 实例，每个实例都是作为协程使用的生成器对象。
    ⑦ url_list发送的每个值都会经由yield from 处理，然后传给fetch 实例。url_list会在yield from表达式处暂停，等待fetch实例处理客户端发来的值。fetch实例运行完毕后，返回的值绑定到l[key] 上。while 循环会不断创建fetch实例，处理更多的值。
    ⑧激活url_list生成器
    ⑨把各个url以及其序列号index，传给url_list传入的值最终到达fetch函数中,url_list并不知道传入的是什么，同时url_list实例在yield from处暂停。直到fetch的一个实例处理完才进行赋值。
    ⑩关键的一步，ul把None传入url_list，传入的值最终到达fetch函数中，导致当前实例终止。然后继续创建下一个实例。如果没有ul.send(None)，那么fetch子生成器永远不会终止，因为ul.send()发送的值实际是在fetch实例中进行，委派生成器也永远不会在此激活，也就不会为l[key]赋值
'''
