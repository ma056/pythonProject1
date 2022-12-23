# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 实例化uploading.py
@Author : wenjing
@Date : 2022/12/21 16:49
"""
from uploading_class import Uploading
import sys
from pathlib import Path
import math
sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
from DBUtility import OneForma
from DatetimeUtility import strtoday
from FileUtility import ExcelOperator, CSVOperator
import json, time


file_path = r'"C:\Users\Mawenjing\Documents\nl-nl_testing.tsv"'
split_num = 200
webappid = 123

# a = Uploading(file_path, split_num, webappid)
# aa = a.content_dict_list
# print(aa)

class Uploading_Q2T(Uploading):
    def __init__(self, file_path, split_num, webappid, limit_num):
        super().__init__(file_path, split_num, webappid)
        self.limit_num = limit_num

    def get_given_data_json(self):
        '''重写父类的方法'''
        query_item_dict = {}
        for content_dict in self.get_content_dict_list():
            query = content_dict.get("Query")
            pt = content_dict.get("PT")
            pt_definition = content_dict.get("PT Definition")
            url = content_dict.get("URL")
            if query_item_dict.get(query) is None:
                query_item_dict[query] = []
            query_item_dict[query].append({
                "PT": pt,
                "url": url,
                "PT Definition": pt_definition
            })

        dbo = OneForma("main")
        count = 1
        for query, value in query_item_dict.items():
            given_data_dict = {
                "query": query,
                "url": value[0].get("url"),
                "pt": {
                    "pt1": {
                        "pt": "",
                        "description": ""
                    },
                    "pt2": {
                        "pt": "",
                        "description": ""
                    },
                    "pt3": {
                        "pt": "",
                        "description": ""
                    },
                    "pt4": {
                        "pt": "",
                        "description": ""
                    },
                    "pt5": {
                        "pt": "",
                        "description": ""
                    }
                }
            }

            for i in range(len(value)):
                given_data_dict["pt"][f"pt{i + 1}"]["pt"] = value[i].get("PT")
                given_data_dict["pt"][f"pt{i + 1}"]["description"] = value[i].get("PT Definition")
            taskname_suffix = int(count / self.split_num) + 1
            taskname = f"{Path(file_path).stem}_{strtoday()}_{str(taskname_suffix).zfill(3)}"
            count += 1
            dbo.create_txt_hits_multi(taskname, json.dumps(given_data_dict), webappid, self.limit_num)
            print(f"Create hit {count} for {taskname}")


Uploading_Q2T(file_path, split_num, webappid)