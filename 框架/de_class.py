# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : de_class.py
@Author : wenjing
@Date : 2022/12/22 14:59
"""
# -- coding: utf-8 --

import sys
from pathlib import Path

sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
from DBUtility import OneForma
from FileUtility import CSVOperator
import json, html


class Delivery():

    def __init__(self, taskid):
        self.taskid = taskid

    def get_mhitid_dict(self):
        dbo = OneForma("Main")
        taskid = self.taskid
        taskname = dbo.get_task_name_by_id(taskid)

        if "_review" in taskname:
            taskname = taskname.replace("_review", "")
            taskid = dbo.get_task_id_by_name(taskname)
        arbi_taskname = taskname + "_review"
        arbi_task_id = dbo.get_task_id_by_name(arbi_taskname)
        hitids = dbo.get_hits_id_by_task_id(taskid)
        arbihitids = dbo.get_hits_id_by_task_id(arbi_task_id)

        mhitid_dict = {}
        for i in range(len(hitids)):
            hitid = hitids[i]
            given_data = dbo.get_given_data_by_hit_id(hitid)
            given_data_dict = json.loads(given_data)
            hit_data = dbo.get_qadata_by_hitid(hitid)
            if hit_data is None:
                print(f"No QA data found for hit {hitid}")
                hit_data = dbo.get_datahandeld_by_hitid(hitid)
                if hit_data is None:
                    print(f"No data handled found for hit {hitid}")
                    continue
            hit_data = html.unescape(hit_data)
            hit_data_dict = json.loads(hit_data)
            mhitid = dbo.get_mHitID_by_hitid(hitid)
            if mhitid is None:
                print(f"No mhitid found for hit {hitid}")
                continue
            if mhitid_dict.get(mhitid) is None:
                mhitid_dict[mhitid] = {}
            if mhitid_dict[mhitid].get('anno1') is None:
                mhitid_dict[mhitid]['anno1'] = {
                    "hitid": hitid,
                    "given_data": given_data_dict,
                    "hit_data": hit_data_dict
                }
            else:
                mhitid_dict[mhitid]['anno2'] = {
                    "hitid": hitid,
                    "given_data": given_data_dict,
                    "hit_data": hit_data_dict
                }

        for i in range(len(arbihitids)):
            arbihitid = arbihitids[i]
            given_data = dbo.get_given_data_by_hit_id(arbihitid)
            given_data_dict = json.loads(given_data)
            hit_data = dbo.get_qadata_by_hitid(arbihitid)
            if hit_data is None:
                print(f"No QA data found for hit {arbihitid}")
                hit_data = dbo.get_datahandeld_by_hitid(arbihitid)
                if hit_data is None:
                    print(f"No data handled found for hit {arbihitid}")
                    continue
            hit_data = html.unescape(hit_data)
            hit_data_dict = json.loads(hit_data)
            mhitid = dbo.get_mHitID_by_hitid(arbihitid)
            if mhitid is None:
                print(f"No mhitid found for hit {arbihitid}")
                continue
            if mhitid_dict.get(mhitid) is None:
                raise Exception(f"mhitid {mhitid} not found for arbi hit {arbihitid}")
            if mhitid_dict[mhitid].get('arbi') is None:
                mhitid_dict[mhitid]['arbi'] = {
                    "hitid": arbihitid,
                    "given_data": given_data_dict,
                    "hit_data": hit_data_dict
                }
            else:
                raise Exception(f"Duplicate arbi hit {arbihitid}")

        return mhitid_dict






