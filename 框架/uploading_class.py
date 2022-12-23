# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : uploading_class.py
@Author : wenjing
@Date : 2022/12/21 14:40
"""
import sys
from pathlib import Path
import math
sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
from DBUtility import OneForma
from DatetimeUtility import strtoday
from FileUtility import ExcelOperator, CSVOperator
import json, time

class Uploading():
    def __init__(self, file_path, split_num, webappid):
        self.file_path = file_path
        self.split_num = split_num
        self.webappid = webappid
        self.content_dict_list = self.get_content_dict_list()

    ## 获取客户的数据：list[{},{}..]
    def get_content_dict_list(self):
        if self.file_path.suffix == ".xlsx":
            exo = ExcelOperator(self.file_path)
            content_dict_list = exo.Excel_to_dict()
        elif self.file_path.suffix == ".csv":
            cso = CSVOperator(self.file_path)
            content_dict_list = cso.csv_to_dict()
        elif self.file_path.suffix == ".tsv":
            cso = CSVOperator(self.file_path)
            content_dict_list = cso.csv_to_dict(delimiter="\t")
        else:
            raise Exception("File type not supported.")
        return content_dict_list

    ## 重构given_data数据,输入tasks和tasks_hits数据
    def get_given_data_json(self):
        dbo = OneForma("main")
        content_dict_list = self.content_dict_list
        for i in range(0, len(content_dict_list)):
            taskname_suffix = math.ceil((i+1)/self.split_num)
            taskname = f"{Path(self.file_path).stem}_{strtoday()}_{str(taskname_suffix)}"
            content_dict = content_dict_list[i]
            given_data_json = json.dumps(content_dict)
            dbo.create_txt_hits_multi(taskname, given_data_json, self.webappid, 2)
            print(f"Created {i + 1}/{len(content_dict_list)} hits")
        print(f"Finshed {self.file_path}")
        print(f"")

