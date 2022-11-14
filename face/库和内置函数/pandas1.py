#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/9/27 1:39 PM 
@process    :
@change :
openpyxl：
https://www.cnblogs.com/hls-code/p/15674197.html
'''
import pandas as pd
# 两个括号就是维持原来的dim. 如果一个括号就会降维。 但是也要注意本身括号里的是不是一个list-like
# df2[ df2['a']>2 ]
# df2[ (df2['a']>0) & (df2['b']>0) ]#如果两个条件要加括号
# df2[ ~(df2['a']>2)] #取反也要记得加括号
# loc:以列名或者行名作为参数，当只有一个参数时，默认选取(行名)
# iloc:值接受
# # 查找某个值所在的行
df = pd.DataFrame({'name': ['小王', '小李'], 'age': [15, 16]})
index = df.loc[df.name == '小王'].index.to_list()
aa = df['name'] == '小王'
a = df[df['name'] == '小王']
aaa = df.loc[0]
aaaa = df.iloc[0]
# print(a.index.values)
# print(index)

df1 = pd.DataFrame([
    ["u1","xiaoming"],
    ["u3","xiaohong"]
],columns=['uid','name'])
df2 = pd.DataFrame(
    data = [{"uid":"u1","score":1},{"uid":"u2","score":2}]
)
df = pd.merge(df1,df2,on="uid",how="right")
df1 = pd.concat([df1,df2],axis=0)
print(df1)


# [pandas官方文档](https://pandas.pydata.org/docs/user_guide/index.html)
import numpy as np
import pandas as pd
import json
# Series和DataFrame
## Series
sr = pd.Series([1,2,3])
sr
### Series操作
sr[0]
sr[[0,1]]
## DataFrame
df1 = pd.DataFrame([
    [1,2], # 第一行
    [3,4], # 第二行数据
    [5,6]
])
df1
df1[0] # index变成以列为维度。一般来说df中都会定义column。这种不定义的情况较少
df1[[0,1]]#这个地方也是column
df2 = pd.DataFrame([
    [1,2],
    [3,4]
],columns=['a','b'])
df2
df2.index
df2.columns
df2.values # 二维数组
df2.dtypes
### DataFrame操作
#df2[0] # dataframe不能用数字索引,除非定义的columns是数字
df2['b'] #选择b列 返回series
df2[['a','b']] # 选取两列
df2[[True,False]] # 布尔索引是按行来索引的
df2[0:1] # 选取索引0-1 不包含1
###两个括号就是维持原来的dim. 如果一个括号就会降维。 但是也要注意本身括号里的是不是一个list-like

df2[ df2['a']>2 ]

df2[ (df2['a']>0) & (df2['b']>0) ]#如果两个条件要加括号

df2[ ~(df2['a']>2)] #取反也要记得加括号
df3 = pd.DataFrame([
    [1,2],
    [3,4]
],columns=['a','b'],index=['A','B'])
df3
df3['A':'B'] # 如果不是数字索引，那么是两端都包含
## df[[col1]]和df[col1]结果都是一列 但是他们两性质不一样  前者还是返回dataframe 后者是series
# 数据存储与读取
## CSV
### read_csv()
# pd.read_csv('', sep=NoDefault.no_default, delimiter=None, header='infer', names=NoDefault.no_default, index_col=None, usecols=None, squeeze=False, prefix=NoDefault.no_default, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None)
# 常用
# - filepath_or_buffer 可以是文件路径也可以是url
# - encoding 一般使用utf-8，如果是平台的bom格式，使用utf-8-sig
# - index_col 指定索引列
# - usecols 一般用来指定列的范围
# - dtype 用于指定列的数值类型
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/350_0af71498f139412cb602f67a18371098.csv",encoding='utf-8-sig')
#df.info()
df.head(1)
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/350_0af71498f139412cb602f67a18371098.csv",
                 index_col = "file_id",
                 encoding='utf-8-sig')
df.loc[18060742]  # loc by index
# 被设置成index 将不在输出字段内
df.loc[18060742].to_dict()
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/350_0af71498f139412cb602f67a18371098.csv",
                 usecols= ["project_id","lang"],
                 encoding='utf-8-sig')
df.head(1)
### 扩展dtypes
#### 默认
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/350_0af71498f139412cb602f67a18371098.csv",
                 encoding='utf-8-sig')
df.dtypes
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df ## pandas会自动判断类型，可以指定类型
df.dtypes
#### 根据值做可能转换
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df =df.convert_dtypes()
df.dtypes # object被转成了string
#### 读取文件的时候指定dtype
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv",
                dtype={"flag":str,"text_content":"string"})
df
# df.dtypes ## 注意text_content是str类型
df.dtypes ## 注意text_content是str类型
df["text_content"]
### to_csv()
df.to_csv(
    "test_01.csv",
    sep=",",#默认
    encoding='utf-8-sig', # 默认'utf-8'，
    index=False # 默认是true, 一般记得要加
)
## Excel
### read_excel()
pd.read_excel(
    '', #"io 路径或者url"
    sheet_name=0, #"默认是第一个sheet  可以是int,str,list,None None是全部 list和None返回的是字典"
    header=0, #"默认第一行，列索引 如果没有表头，指定header=None"
    index_col=None, #'默认没有'
    usecols=None, #"默认拿出所有的列, 几种方式A:C, A,C [0,2] ['AAA','CCC] lambda i:i=='AAA' "
    skiprows=None, #跳过行 skiprows=1跳过的行数，或者 shiprows=[0,2]，
    names = ['a','b','c'] ,# header是None的时候，指定names,否则会替换掉第一行的数据。
    dtype={'a':'str'},# 注意都是字符串
    parse_dates=False ,# True 尝试解析 [0,1] [[0,1,2]] ['a','b']
    date_parser=None ,#function 日期解析函数 为None的时候会使用内部的解析器解析.
    na_values = None,#'a' #'NA' ['NA','#NA','0',0],
    converters=None, #{"a":lambda i:i+1},
    mangle_dupe_cols=True,#"默认允许重复并且会重命名重复的列 不能设置成False 还不支持"
)
# excel_df = pd.read_excel("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/email_update.xlsx")
# excel_df.head()
# 如果要读excel 需要安装 xlrd和xlwt
#df = pd.read_excel("test.xlsx", sheet_name=["Sheet1", "Sheet3"]) 可以一次获取多个sheet
### to_excel()
df.to_excel(
    '',#excel_writer 文件目录名
    sheet_name='Sheet1',
    index=False,
    na_rep='' # 缺失值的表示方式
)
### 如果要讲多个dataframe写入到不同的sheet
with pd.ExcelWriter("test.xlsx") as wt:
    df1.to_excel(sheet_name="sheet1")
    df2.to_excel(sheet_name="sheet2")
## 添加新的数据
df3 = df1.copy()
with pd.ExcelWriter('output.xlsx', mode="a", engine="openpyxl") as writer:
    df3.to_excel(writer, sheet_name='Sheet_name_3_3_3')
## SQL
import psycopg2
conn = psycopg2.connect(host=RDS_DATA_DB_HOST, user=RDS_DATA_DB_USER,
                            password=RDS_DATA_DB_PSW, database=RDS_DATA_DB_NAME,
                                port=RDS_DATA_DB_PORT)
### read_sql()
pd.read_sql(sql, conn)
### to_sql()
DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None, method=None)
engine = create_engine(
        f'postgresql+psycopg2://{RDS_DATA_DB_USER}:{RDS_DATA_DB_PSW}@{RDS_DATA_DB_HOST}:{RDS_DATA_DB_PORT}/{RDS_DATA_DB_NAME}',
        poolclass=NullPool,
        connect_args={'connect_timeout': 30}
    )

df.to_sql('nums', con=engine,index=False,if_exists="append") # nums是表名，con
### 实际的工作中，尽量使用appen 不要使用replace,或者fail
# if_exists
#  - fail
#  - append # 不存在会创建新的
#  - replace # 慎用，会清空原有数据
# method{None, ‘multi’, callable}, optional
# Controls the SQL insertion clause used:
# None : Uses standard SQL INSERT clause (one per row).
# ‘multi’: Pass multiple values in a single INSERT clause.

# append有事务的作用
## json
### read_json
# pandas.read_json(path_or_buf=None, orient=None, typ='frame', dtype=None, convert_axes=None, convert_dates=True, keep_default_dates=True, numpy=False, precise_float=False, date_unit=None, encoding=None, encoding_errors='strict', lines=False, chunksize=None, compression='infer', nrows=None,
# orients is:
#
# 'split' : dict like {index -> [index], columns -> [columns], data -> [values]}
# 'records' : list like [{column -> value}, ... , {column -> value}]
# 'index' : dict like {index -> {column -> value}}
# 'columns' : dict like {column -> {index -> value}}
# 'values' : just the values array

# records
'''
[
  {
    "project_id": "531",
    "ss_folder": "Ake_P15924_ARA_EGY_QN377998_20210725-101610",
    "person_id": "QN377998",
    "audio_url": "appen://531_Ake__ARA_EYG/.../xx.wav",
    "audio_type": "SZSJ",
    "lang": "Arabic(Egypt)",
    "valid_duration": 3.986,
    "content_text": "لقد إشتريت ثلاث طائرات وست سفن حربية.",
    "audio_start": "1.548",
    "audio_end": "5.534",
    "pid": 741693,
    "age": 19,
    "gender": "M",
    "submit_date": "20220124",
    "pack_audio_name": "ArabicEgypt_abqfer_M_19_0949.wav",
    "is_pack": 1,
    "pack_path": "/appen-delivery/wooey_rs/ake/1e09bae1ecdd4360b94c762846075c02"
  },
  ...
]
'''
df1 = pd.read_json("http://projecteng.oss-cn-shanghai.aliyuncs.com/0_ProjectData/data_bak/0f207f4f16e34c4caf7b576ab8e535b7.json")
df1.head(1)
#split
'''
{
    "columns":["col 1","col 2"],
    "index":["row 1","row 2"],
    "data":[["a","b"],["c","d"]]}
'''
#index
'''
{ 
    "row 1":{"col 1":"a","col 2":"b"},
    "row 2":{"col 1":"c","col 2":"d"}
}
'''

### to_json
# DataFrame.to_json(path_or_buf=None, orient=None, date_format=None, double_precision=10, force_ascii=True, date_unit='ms', default_handler=None, lines=False, compression='infer', index=True, indent=None, storage_options=None
import json
df = pd.DataFrame(
    [["a", "b"], ["c", "d"]],
    index=["row 1", "row 2"],
    columns=["col 1", "col 2"],
)
df.to_json(orient="split")
df.to_json(orient="records")
df.to_json(orient="index")
df.to_json(orient="columns")
df.to_json(orient="values")
df.to_json(orient="table")
### json_normalize
# pandas.json_normalize(data, record_path=None, meta=None, meta_prefix=None, record_prefix=None, errors='raise', sep='.', max_level=None)
data = [
    {"id": 1, "name": {"first": "Coleen", "last": "Volk"}},
    {"name": {"given": "Mark", "family": "Regner"}},
    {"id": 2, "name": "Faye Raker"},
]
pd.json_normalize(data)
## 会自动创建每个字段， 内层的字段通过.拼接
data = [
    {
        "id": 1,
        "name": "Cole Volk",
        "fitness": {"height": 130, "weight": 60},
    },
    {"name": "Mark Reg", "fitness": {"height": 130, "weight": 60}},
    {
        "id": 2,
        "name": "Faye Raker",
        "fitness": {"height": 130, "weight": 60},
    },
]
pd.json_normalize(data, max_level=0) # max_level如果是0 那么解析第一层
data = [
    {
        "state": "Florida",
        "shortname": "FL",
        "info": {"governor": "Rick Scott"},
        "counties": [
            {"name": "Dade", "population": 12345},
            {"name": "Broward", "population": 40000},
            {"name": "Palm Beach", "population": 60000},
        ],
    },
    {
        "state": "Ohio",
        "shortname": "OH",
        "info": {"governor": "John Kasich"},
        "counties": [
            {"name": "Summit", "population": 1234},
            {"name": "Cuyahoga", "population": 1337},
        ],
    },
]
# pd.json_normalize(
#     data
# )

## 以counties 作为解析的行
pd.json_normalize(
    data, "counties", ["state", "shortname", ["info", "governor"]]
)
data = [{"A": [[1, 2],[3,4]]}]
pd.json_normalize(data, "A", record_prefix="Prefix.")

## Table
### read_table()
df = pd.read_table("test.txt", names = ["col1", "col2"], sep=' ')
## to_list
sr = pd.Series([1,2,3])
sr_lst = sr.tolist()
print(type(sr),type(sr_lst))
df2 = pd.DataFrame([
    [1,2],
    [3,4]
],columns=['a','b'])
# df2.tolist()
# df没有to_list
## to_dict
df2
df2.to_dict() # index 为key,值为series 转还后的 dict
type(df2.to_dict()["a"])
df2.to_dict(orient="list")
df2.to_dict(orient="dict")  # 默认行为
df2.to_dict(orient="series")
df2.to_dict(orient="records")   # 常用
df2.to_dict(orient="index")   # key是index
# 常用
## isnull(isna)和notnull(notna)
# pandas中不要用is None等来完成比较，可能会存在非常多的情况!
# pd.isnull == pd.isna
# pd.notnull == pd.notna
# Pands会把np.nan、None以及数据缺失认为为NULL
pd.isnull(np.nan)
# 同pd.isnull(np.NaN)
pd.isnull(pd.NA)
pd.isnull(pd.NaT) # 日期空只在pd中定义
pd.isnull(None)
### 从数据结构加载
sr = pd.Series(["a","b",1,None],dtype="string")
sr

sr.isnull()
sr[3] is pd.NA # True

# 不要使用 == 判断
print("na", sr[3] == pd.NA,type(sr[3] == pd.NA)) #na <NA> <class 'pandas._libs.missing.NAType'>
pd.isnull(sr[3]) # True
sr2 = pd.Series(["a","b",1,None],dtype="str")
sr2 # dtype object
pd.isnull(sr[3]) # True
sr2.isnull()  # 依然有效
sr3 = pd.Series(["a","b",1,None],dtype="string")
sr3.isnull() # None也是可以被isnull识别
sr4 =  pd.Series(["a","b",1,None])
sr4 # dtype object
sr4 = sr4.convert_dtypes()
sr4
sr5 =  pd.Series(["a","b","c",None])
sr5 # dtype object
sr5 = sr5.convert_dtypes()  # 专成了string
sr5
### 时间类型
st1 = pd.Series([pd.to_datetime('2018-09-08'),None],dtype="datetime64[ns]")
st1
st1.isnull() # is null也是用于pd.NaT类型
### 从csv加载数据
#### 读取的时候指定
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv",dtype={"text_content":"str"})
df
df.isnull()
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv",dtype={"text_content":"string"})
df
df.isnull()
#### astype事后转换 string和str存在差异
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df["text_content"] = df["text_content"].astype("str")
df.isnull() #astype str会强转
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df["text_content"] = df["text_content"].astype("string") # 如果事后再转换类型，会强转字符串类型
df
df.isnull()  # string会保留null值
#type(df["text_content"][3])  # pandas._libs.missing.NAType
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df["text_content"] = df["text_content"].astype("string") # 在老本版这样用可能会报错。 在老version中要先转“str” 再转string



# loc
# df.loc[row_idx] # 选择一行
# df.loc[row_idx,col_idx] #选择一个元素
## count和len
### count
# count是统计非空值的个数,len是不管空还是非空都会统计
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df
# df.count().to_dict()  # {'text_content': 2, 'flag': 4, 'full_text': 4}
# df["text_content"].count() # 2
sr1 =  pd.Series(["a","b","c",None])
print("sr1",sr1.count())

sr2 = pd.Series(["a","b","c",None]).astype("string")
print("sr2",sr2.count())

sr3 = pd.Series(["a","b","c",None]).astype("str")
print("sr3",sr3.count())
### len
sr4 =  pd.Series(["a","b","c",None])
print("sr4",len(sr4))

sr5 = pd.Series(["a","b","c",None]).astype("string")
print("sr5",len(sr5))

sr6 = pd.Series(["a","b","c",None]).astype("str")
print("sr6",len(sr6))
## loc 和 iloc
# loc:以列名或者行名作为参数，当只有一个参数时，默认选取(行名)
# iloc:值接受
sr= pd.Series(["a","b","c",None])
sr.loc[0]
sr.iloc[0]
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df
df.loc[0]  #第一个index=0行
df.iloc[0]
df.loc[:,"text_content"] # 选取一列,多个参数的时候别忘记逗号  等价于df["text_content"]
#df.loc[:,0]  # 用loc的是以后第一个参数必须是index 第二个必须是标签名，否则 KeyError
df.iloc[:,0] # iloc可以用数字，但是尽量避免
df.loc[:,["text_content","flag"]] # 用数字可以一次选择多个，标签是左右包含关系 等价于df[["text_content","flag"]]
df.loc[[0,2]] # 第二个参数可省略
df.loc[0:2] #loc 如果使用区间都是包含的关系
df.iloc[0:2] # iloc是不包含右侧的索引
# 注意切片后，index不会自动更新，比如
df= pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_filter.csv")
df
df.loc[2:6] = 1 # 会直接修改原来的值
df
df2 = df.loc[2:6]
df2 # 注意index 是 2-6
for idx,row in df2.iterrows():
    print(idx)
## 增加数据
### 赋值增加一列数据
#### 直接赋值
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df["add_col1"] = 1
df["add_col2"] = ["a","b","c","d"]
df["add_col3"] = pd.Series(["1","2","3","4"])
df["add_col4"]  = pd.NA
df
#### 通过loc赋值
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.loc[:, "add_col5"] = pd.NA
df
#### 通过insert
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.insert(1,"add_col6",pd.NA)
df.insert(1,"add_col7",[1,3,4,6])
df
### 添加一行数据
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.loc[4]= ["text","flag","full_text"]
df.loc[3] = pd.NA  #!注意 对已存在index 会直接覆盖数据
df
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df["text_content"][2] = "cover text"  # 直接这样赋值会出现SettingWithCopyWarning
df
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.loc[2,"text_content"] = "cover text"  # 这种不会有warnning  注意index不一定是所在的顺序
df
### append增加一行或多行
#### append字典
task_df = pd.DataFrame()
task_df = task_df.append({"id":1,"text":"test1"},ignore_index=True) # append 并返回最新的数据,注意赋值
task_df
task_df = pd.DataFrame()
task_df = task_df.append({"id":1,"text":"test1"},ignore_index=True)
task_df = task_df.append({"id":2,"text":"test2","add_col1":"x"},ignore_index=True) # pd 会自动扩展列，不存在的为空
task_df
#### appen列表
task_df = pd.DataFrame()
task_df = task_df.append([{"id":1,"text":"test1"},{"id":2,"text":"test2"}]) # 也可以接受数组
task_df = task_df.append([{"id":3,"text":"test1"},{"id":4,"text":"test2"}]) # 注意index会重复
task_df
task_df = pd.DataFrame()
task_df = task_df.append([{"id":1,"text":"test1"},{"id":2,"text":"test2"}],ignore_index=True)
task_df = task_df.append([{"id":3,"text":"test1"},{"id":4,"text":"test2"}],ignore_index=True) # 如果不想index重复可以使用ignore_index=True
task_df
#### append sr 或者df
task_df = pd.DataFrame()
sr = pd.Series([1,2,3,4])
task_df = task_df.append(sr,ignore_index=True)
task_df
df1 = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df2 = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")

df = pd.DataFrame()
df = df.append(df1,ignore_index=True)
df = df.append(df2,ignore_index=True)
df
## 修改列名和数据
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df
### 直接赋值columns(不推荐)
df.columns = ["col1","col2","col3"] # 直接生效
df
### rename修改
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.rename(columns={"text_content":"col1","f":"col2","full_text":"col3"}) # 不存在的列不会报错!
df # 原来的未变
df.rename(columns={"text_content":"col1","f":"col2","full_text":"col3"},inplace=True) # 不存在的列不会报错!
df ## 如果原地替换注意加上inplace参数，否则原来的df不会修改
### rename修改行索引
df.rename({0:"line1",1:"line2"},axis=0,inplace=True) # 1. 第一个参数不是columns.第二 axis=0
df
df["col1"]["line1"]
df.loc["line1","col1"]
### 使用loc修改数据
df.loc["line1","col1"] = "update_text"
df
## 删除数据
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df
df.columns
df.drop("flag",axis=1,inplace=True)
#df.drop("flag",axis=1,inplace=True)
#df
df
# 也可以删除多列
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.drop(["flag","full_text"],axis=1,inplace=True)
df
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.drop(columns=["flag","full_text"],inplace=True)  # 如果传入columns,则不需要axis
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.drop([0,2],inplace=True) #原地按index删除
# df.drop(index=[0,2],inplace=True) # 结果同上
# df.drop(labels=[0,2],inplace=True) # 结果同上
df
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.drop(index=[0,2],inplace=True) #原地按index删除
# df.drop(index=[0,2],inplace=True) # 如果没找到会报错
df
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.rename({0:"line1",1:"line2"},axis=0,inplace=True)
df.drop(index =["line1",2],inplace=True)
df
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.drop(index=df[df["flag"]>2].index,inplace=True)
df
## 缺失值
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.dropna(inplace=True) # 加了参数是原地修改 默认只要存在缺失就删除
df
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df.dropna(inplace=True,how="all") # 全部为空才删除
df
df["col1"] = pd.NA
df
df.fillna(0,inplace=True) # 加inplace 原地修改
df
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/string_test.csv")
df["text_content"].fillna("empty",inplace=True)
df
## 重复值
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_dup.csv")
df.duplicated() # 返回每一列是否重复，完全重复
df.drop_duplicates(inplace=True)
df # index2被删除
df.drop_duplicates("test_flag")# 如果要原地修改加inplace
df.drop_duplicates(["test_flag","test_text"])
df.drop_duplicates(["test_flag","test_text"],keep="last") # first last
## 索引重置
### reindex
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_dup.csv")
df.drop_duplicates(["test_flag","test_text"],keep="last",inplace=True) # first last
df

df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_dup.csv")
df = df.reindex(["b1","b2",1])
df # 如果少了，
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_dup.csv")
df
df = df.reindex([1,2,3,4,5,6,7,8,9,10,11]) #有点类似切片重组
df
### reset_index
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_dup.csv")
df.drop_duplicates(["test_flag","test_text"],keep="last",inplace=True) # first last
df.reset_index(inplace=False)
df.reset_index(drop=True,inplace=False) # drop=True 删除原来的index列，默认保留，注意该方法默认inplace=False
### set_index
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_dup.csv")
df = df.set_index("test_text")
df
df.loc["text1"]
# 设置多列索引
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_dup.csv")
df = df.set_index(["test_text","id"])
df.loc["text1"].loc["a"]
## 数据排序
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_dup.csv")
df
df.sort_values(by="id",inplace=True)
df
df.sort_values(by=["test_text","id"],inplace=True)
df
df.sort_values(by=["test_text","id"],inplace=True,ascending=False) # 默认升序，降序False
df
# 数据计算
## 计算函数
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_cal.csv")
df
df["test_col"].sum()
df["test_col"].max()
df["test_col"] = df["test_col"].round(decimals=2)
df
## groupby
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_cal.csv")
df.groupby(by=["test_text"])

df.groupby(by=["test_text"]).sum() # ，自动sum可以增加的列
df.groupby(by=["test_text","id"]).sum()
for gp,newdf in df.groupby(by=["test_text"]):
    print(gp,type(newdf))
#agg聚合
df.groupby(by=["test_text"]).agg(["mean","sum"]) # 自动对可以计算的列进行 对应方法的计算
## interrows
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_cal.csv")
for idx,row in df.iterrows():
    print(idx,type(row))
## apply
df = pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_cal.csv")
df
df["test_col"] = df["test_col"].apply(lambda x : x*2)
df
df =  pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_cal.csv")

def cal1(row):
    return row["test_col"] * row["col2"]

df["new_col"] = df.apply(cal1,axis=1)
df["col2"] = df.apply(lambda row: row["test_col"] + row["col2"]  ,axis=1)
df
df =  pd.read_csv("http://appen-pe.oss-cn-shanghai.aliyuncs.com/example_data/pandas_kt/test_cal.csv")
df = df[df["test_col"]>1.2]
df["col2"] = df.apply(lambda row: row["test_col"] + row["col2"]  ,axis=1)
df
## merge
df1 = pd.DataFrame([
    ["u1","xiaoming"],
    ["u3","xiaohong"]
],columns=['uid','name'])
df1
df2 = pd.DataFrame(
    data = [{"uid":"u1","score":1},{"uid":"u2","score":2}]
)
df2
df = pd.merge(df1,df2)
df
df = pd.merge(df1,df2,on="uid",how="left")
df
df = pd.merge(df1,df2,on="uid",how="right")
df
df = pd.merge(df1,df2,on="uid",how="inner") # 默认inner
df
df = pd.merge(df1,df2,on="uid",how="outer")
df
df1.merge(df2,how="right") #df2默认是右表 # 不指定的情况下
## 如果字段不一样可以通过left_on,right_on指定
df = pd.merge(df1,df2,left,how="outer")
df3 = pd.DataFrame([
    ["u1","xiaoming","M"],
    ["u3","xiaohong","M"]
],columns=['uid','name',"gender"])
df3
df4 = pd.DataFrame(
    data = [{"uid":"u1","score":1,"gender":"F"},{"uid":"u2","score":2,"gender":"M"}]
)
df4
pd.merge(df3,df4) # 没有on的时候 默认相同字段merge
pd.merge(df3,df4,left_on="uid",right_on="uid")
## 如果希望通过索引合并
pd.merge(df3,df4,left_index=True,right_index=True)  # 如果使用索引就使用xx_index=True
df5 = pd.DataFrame(
    data = [{"uid":"u1","score":1,"gender":"F","idx":0},{"uid":"u2","score":2,"gender":"M","idx":1},{"uid":"u8","score":99,"gender":"M","idx":1}]
)
df5
#  如果希望通过索引合并
pd.merge(df3, df5, left_index=True,right_on="idx")  # left_index和right_index必须都传

#  注意一对多的关系，可能会导致数据比之前多

#  concat
dfc1 = pd.DataFrame([
    ["u1","xiaoming"],
    ["u3","xiaohong"]
],columns=['uid','name'])
dfc1
dfc2 = pd.DataFrame(
    data = [{"uid":"u1","score":1},{"uid":"u2","score":2},{"uid":"u8","score":99}]
)
dfc2
pd.concat([dfc1,dfc2]) #默认是纵向合并
pd.concat([dfc1,dfc2],axis=1) # 按照index合并
pd.concat([dfc1,dfc2],axis=1,join="inner") # join 只有inner和outter,默认outter ,一般只有axis=1的时候才会用inner或者outer
pd.concat([dfc1,dfc2]) #默认是纵向合并