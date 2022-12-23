# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : tr_class.py
@Author : wenjing
@Date : 2022/12/22 10:50
"""
import sys
from pathlib import Path

sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
from DBUtility import OneForma
import html,json


class Tranfer():

    def __init__(self,taskid):
        self.taskid = taskid

    def get_dict(self):
        dbo = OneForma("Main")
        mhitid_dict = {}
        hitids = dbo.get_hits_id_by_task_id(self.taskid)
        for i in range(len(hitids)):
            hitid = hitids[i]
            hit_data = None
            qa_data = dbo.get_qadata_by_hitid(hitid)
            if qa_data is None:
                print(f"No QA data found for hit {hitid}")
                datahandled = dbo.get_datahandeld_by_hitid(hitid)
                if datahandled is None:
                    print(f"No data handled found for hit {hitid}")
                    continue
                hit_data = html.unescape(datahandled)
            else:
                hit_data = html.unescape(qa_data)
            if hit_data is None:
                print(f"No data found for hit {hitid}")
                continue
            hit_data_dict = json.loads(hit_data)
            if hit_data_dict.get('comment') is None:
                print(f"No comment found for hit {hitid}, json data invalid")
                continue
            del hit_data_dict['comment']
            mhitid = dbo.get_mHitID_by_hitid(hitid)
            given_data = dbo.get_given_data_by_hit_id(hitid)
            if given_data is None:
                print(f"No given data found for hit {hitid}")
                continue
            done_by = dbo.get_done_by_by_hit_id(hitid)
            if done_by is None:
                print(f"No done_by found for hit {hitid}")
                continue
            user_id = dbo.get_user_id_by_done_by(done_by)
            if user_id is None:
                print(f"No user_id found for done_by {done_by}")
                continue
            if mhitid_dict.get(mhitid) is None:
                mhitid_dict[mhitid] = [{
                    "given_data": given_data,
                    "hit_data": hit_data_dict
                }]
            else:
                mhitid_dict[mhitid].append({
                    "given_data": given_data,
                    "hit_data": hit_data_dict
                })
        return mhitid_dict