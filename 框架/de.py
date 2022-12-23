# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : de.py
@Author : wenjing
@Date : 2022/12/22 15:00
"""

# -- coding: utf-8 --

import sys
from pathlib import Path

sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
from DBUtility import OneForma
from FileUtility import CSVOperator
import json, html
from de_class import Delivery

def main(taskid):
    dbo = OneForma("Main")
    taskname = dbo.get_task_name_by_id(taskid)

    handback_folder = Path(f"H:/PipelineFTP/Amazon - Q2PT/Handback/{taskid}_{taskname}")
    handback_folder.mkdir(parents=True, exist_ok=True)

    anno1_path = Path(f"{handback_folder}/anno1.tsv")
    anno2_path = Path(f"{handback_folder}/anno2.tsv")
    arbi_path = Path(f"{handback_folder}/arbi.tsv")
    anno1_list = []
    anno2_list = []
    arbi_list = []

    delivery = Delivery(taskid)
    mhitid_dict = delivery.get_mhitid_dict()

    for mhitid in mhitid_dict:
        if mhitid_dict[mhitid].get('anno1') is None:
            raise Exception(f"anno1 not found for mhitid {mhitid}")
        if mhitid_dict[mhitid].get('anno2') is None:
            raise Exception(f"anno2 not found for mhitid {mhitid}")
        if mhitid_dict[mhitid].get('arbi') is None:
            mhitid_dict[mhitid]['arbi'] = mhitid_dict[mhitid]['anno1']

        anno1 = mhitid_dict.get(mhitid).get('anno1')
        anno2 = mhitid_dict.get(mhitid).get('anno2')
        arbi = mhitid_dict.get(mhitid).get('arbi')

        anno1_ret_list = generate_delivery_content(anno1)
        anno2_ret_list = generate_delivery_content(anno2)
        arbi_ret_list = generate_delivery_content(arbi)

        anno1_list.extend(anno1_ret_list)
        anno2_list.extend(anno2_ret_list)
        arbi_list.extend(arbi_ret_list)

    anno1_csvo = CSVOperator(anno1_path)
    anno2_csvo = CSVOperator(anno2_path)
    arbi_csvo = CSVOperator(arbi_path)

    anno1_csvo.dict_to_csv(anno1_list, delimter='\t')
    anno2_csvo.dict_to_csv(anno2_list, delimter='\t')
    arbi_csvo.dict_to_csv(arbi_list, delimter='\t')
    print("Done")


def generate_delivery_content(anno):
    given_data = anno.get('given_data')
    query = given_data.get('query')
    url = given_data.get('url')
    pt = given_data.get('pt')
    hit_data = anno.get('hit_data')

    ret_dict_list = []

    pt1 = pt.get('pt1').get('pt')
    pt1_des = pt.get('pt1').get('description')
    pt1_eval = hit_data.get('pt1')
    pt1_comment = hit_data.get('pt1_comment')

    pt2 = pt.get('pt2').get('pt')
    pt2_des = pt.get('pt2').get('description')
    pt2_eval = hit_data.get('pt2')
    pt2_comment = hit_data.get('pt2_comment')

    pt3 = pt.get('pt3').get('pt')
    pt3_des = pt.get('pt3').get('description')
    pt3_eval = hit_data.get('pt3')
    pt3_comment = hit_data.get('pt3_comment')

    pt4 = pt.get('pt4').get('pt')
    pt4_des = pt.get('pt4').get('description')
    pt4_eval = hit_data.get('pt4')
    pt4_comment = hit_data.get('pt4_comment')

    pt5 = pt.get('pt5').get('pt')
    pt5_des = pt.get('pt5').get('description')
    pt5_eval = hit_data.get('pt5')
    pt5_comment = hit_data.get('pt5_comment')

    comment = hit_data.get('comment')
    if comment is None:
        comment = f"{pt1_comment}, {pt2_comment}, {pt3_comment}, {pt4_comment}, {pt5_comment}"
    # Query	URL	PT	PT Definition	Evaluation	Comments
    if pt1 is None or pt1 == "":
        raise Exception(f"pt1 is empty for hit {anno.get('hitid')}")
    ret_dict = {
        "Query": query,
        "URL": url,
        "PT": pt1,
        "PT Definition": pt1_des,
        "Evaluation": pt1_eval,
        "Comments": comment
    }
    ret_dict_list.append(ret_dict)

    if pt2 != "":
        ret_dict = {
            "Query": query,
            "URL": url,
            "PT": pt2,
            "PT Definition": pt2_des,
            "Evaluation": pt2_eval,
            "Comments": ""
        }
        ret_dict_list.append(ret_dict)
    if pt3 != "":
        ret_dict = {
            "Query": query,
            "URL": url,
            "PT": pt3,
            "PT Definition": pt3_des,
            "Evaluation": pt3_eval,
            "Comments": ""
        }
        ret_dict_list.append(ret_dict)
    if pt4 != "":
        ret_dict = {
            "Query": query,
            "URL": url,
            "PT": pt4,
            "PT Definition": pt4_des,
            "Evaluation": pt4_eval,
            "Comments": ""
        }
        ret_dict_list.append(ret_dict)
    if pt5 != "":
        ret_dict = {
            "Query": query,
            "URL": url,
            "PT": pt5,
            "PT Definition": pt5_des,
            "Evaluation": pt5_eval,
            "Comments": ""
        }
        ret_dict_list.append(ret_dict)
    return ret_dict_list


if __name__ == "__main__":
    taskids = sys.argv[1]
    if taskids[-1] == ",":
        taskids = taskids[:-1]
    taskid_list = taskids.split(",")
    for taskid in taskid_list:
        main(taskid)
