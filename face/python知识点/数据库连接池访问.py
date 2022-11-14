# pip install  DBUtils==1.3
import pymysql
import mysql5.mysql.connector as mysql5conn
import mysql8.mysql.connector as mysql8conn
from DBUtils.PooledDB import PooledDB, SharedDBConnection

'''
def execute_select_sql(self, sql):
    if self.pool != None:
        conn = self.pool.connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print(e)
            raise
        finally:
            conn.close()
    else:
        print("DB pool not created")
        raise
'''


class MysqlDB(object):

    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块   例如：mysql8conn,
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            # mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            # maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            # maxshared=3,
            # # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
            # blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            # maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            # setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            # ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            database='textrobot2',
            charset='utf8'
        )

    def __new__(cls, *args, **kw):
        '''启用单例模式'''
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def connect(self):
        '''启动连接'''
        conn = self.pool.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    def connect_close(self, conn, cursor):
        '''关闭连接'''
        cursor.close()
        conn.close()

    def fetch_all(self, sql, args):
        '''批量查询'''
        conn, cursor = self.connect()
        cursor.execute(sql, args)
        record_list = cursor.fetchall()
        self.connect_close(conn, cursor)
        return record_list

    def fetch_one(self, sql, args):
        '''查询单条数据'''
        conn, cursor = self.connect()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        self.connect_close(conn, cursor)
        return result

    def insert(self, sql, args):
        '''插入数据'''
        conn, cursor = self.connect()
        row = cursor.execute(sql, args)
        conn.commit()
        self.connect_close(conn, cursor)
        return row


if __name__ == '__main__':
    # 实例化
    mysql_db_ = MysqlDB()
    '''
    查询单条
    '''
    data = mysql_db_.fetch_one("select ip,port from t_robotTrainingCoreConfig where robotId=%s", (1,))
    print(data)
    mysql_db_.insert("insert into t_modelversion(robotId,version) values(%s,%s)", (888, "model_name"))
