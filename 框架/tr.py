# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : tr.py
@Author : wenjing
@Date : 2022/12/22 10:49
"""
import sys
from pathlib import Path

sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
from DBUtility import OneForma
from tr_class import Tranfer
import os, json, time, html


def main(webapp1_id, webapp2_id):
    print(f"Start transfer webapp {webapp1_id} to webapp {webapp2_id}")
    print("Connect to Oneforma Database")
    dbo = OneForma("Main")
    print("List all handoff files")
    taskids = dbo.get_task_ids_by_webapp_id(webapp1_id)
    if taskids is None:
        print("No task found")
        return
    for taskid in taskids:
        not_finished_hits = dbo.get_not_finished_hits_by_task_id(taskid)
        if not_finished_hits is not None and len(not_finished_hits) > 0:
            print(f"Task {taskid} has not finished hits, skip")
            continue
        taskname = dbo.get_task_name_by_id(taskid)
        new_taskname = taskname + "_review"
        review_task_id = dbo.get_task_id_by_name(new_taskname)
        if review_task_id is not None:
            print(f"Task {taskname} already exists, skip")
            continue

        tr = Tranfer(taskid)
        mhitid_dict = tr.get_dict()

        for key, value in mhitid_dict.items():
            if len(value) != 2:
                print(f"mhitid {key} result error, length {len(value)}")
                continue
            hit_data_dict_1 = value[0].get('hit_data')
            hit_data_dict_2 = value[1].get('hit_data')
            if hit_data_dict_1 is None or hit_data_dict_2 is None:
                print(f"mhitid {key} result error, hit_data_dict_1 {hit_data_dict_1} hit_data_dict_2 {hit_data_dict_2}")
                continue
            if hit_data_dict_1.get('pt1') != hit_data_dict_2.get('pt1') or \
                    hit_data_dict_1.get('pt2') != hit_data_dict_2.get('pt2') or \
                    hit_data_dict_1.get('pt3') != hit_data_dict_2.get('pt3') or \
                    hit_data_dict_1.get('pt4') != hit_data_dict_2.get('pt4') or \
                    hit_data_dict_1.get('pt5') != hit_data_dict_2.get('pt5'):
                new_given_data = value[0].get('given_data')
                dbo.create_txt_hits_mhitid(new_taskname, new_given_data, webapp2_id, key)
                print(f"mhitid {key} create arbitration hit")
        print(f"{taskid} -> {new_taskname}")


if __name__ == "__main__":
    webapp1_ids = sys.argv[1]  # 4205
    webapp2_ids = sys.argv[2]  # 4215
    webapp1_id_list = webapp1_ids.split(",")
    webapp2_id_list = webapp2_ids.split(",")
    if len(webapp1_id_list) != len(webapp2_id_list):
        raise ValueError("Webapp1 and Webapp2 id list length not equal")
    for i in range(0, len(webapp1_id_list)):
        webapp1_id = webapp1_id_list[i]
        webapp2_id = webapp2_id_list[i]
        if webapp1_id == "" or webapp2_id == "":
            continue
        main(webapp1_id, webapp2_id)