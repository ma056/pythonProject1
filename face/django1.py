'''
https://blog.csdn.net/happygjcd/article/details/105316944
'''

'''

1、Django 的生命周期？
    前端发起请求
    nginx
    uwsgi
    中间件
    URL
    view视图
    通过orm与model层进行数据交互
    拿到数据返回给view
    试图将数据渲染到模板中拿到字符串
    中间件
    uwsgi
    nginx
    前端渲染
2、中间件的五种方法？
    process_request : 请求进来时,权限认证
    process_view : 路由匹配之后,能够得到视图函数
    process_exception : 异常时执行
    process_template_responseprocess : 模板渲染时执行
    process_response : 请求有响应时执行
3、django 自带的中间件？
    SecurityMiddleware
    SessionMiddleware
    CommmonMiddleware
    CsrfViewMiddleware
    AuthenticationMiddleware
    MessageMiddleware
    XFrameOptionMiddleware
8 列举django orm 中所有的方法
    <1> all(): 查询所有结果
    <2> filter(**kwargs): 它包含了与所给筛选条件相匹配的对象。获取不到返回None
    <3> get(**kwargs): 返回与所给筛选条件相匹配的对象，返回结果有且只有一个。
    如果符合筛选条件的对象超过一个或者没有都会抛出错误。
    <4> exclude(**kwargs): 它包含了与所给筛选条件不匹配的对象
    <5> order_by(*field): 对查询结果排序
    <6> reverse(): 对查询结果反向排序
    <8> count(): 返回数据库中匹配查询(QuerySet)的对象数量。
    <9> first(): 返回第一条记录
    <10> last(): 返回最后一条记录
    <11> exists(): 如果QuerySet包含数据，就返回True，否则返回False
    <12> values(*field): 返回一个ValueQuerySet——一个特殊的QuerySet，运行后得到的
    并不是一系 model的实例化对象，而是一个可迭代的字典序列
    <13> values_list(*field): 它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
    <14> distinct(): 从返回结果中剔除重复纪录
4、csrf 攻击、危害与防御
    csrf 攻击全称为Cross-site request forgery 中文名称 跨站请求伪造 也被称为“One Click Attack”或者“Session Riding”，通常缩写为CSRF或者XSRF，是一种对网站的恶意利用。
    XSS主要是利用站点内的信任用户，而CSRF则通过伪装来自受信任用户的请求，来利用受信任的网站。与XSS相比，CSRF更具危险性。
    主要的危害来自于攻击者盗用用户身份，发送恶意请求。比如：模拟用户发送邮件，发消息，以及支付、转账等。
    如何防御CSRF攻击?
    1、重要数据交互采用POST进行接收，当然POST也不是万能的，伪造一个form表单即可破解。
    2、使用验证码，只要是涉及到数据交互就先进行验证码验证，这个方法可以完全解决CSRF。
    3、出于用户体验考虑，网站不能给所有的操作都加上验证码，因此验证码只能作为一种辅助手段，不能作为主要解决方案。
    4、验证HTTP Referer字段，该字段记录了此次HTTP请求的来源地址，最常见的应用是图片防盗链。
    5、为每个表单添加令牌token并验证
'''