import sys
from pathlib import Path

sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))
from DBUtility import OneForma
import json, html, time, re, math, os
from DatetimeUtility import strtoday
from FileUtility import CSVOperator


def main(taskid):
    dbo = OneForma("Main")
    hitids = dbo.get_hits_id_by_task_id(taskid)
    taskname = dbo.get_task_name_by_id(taskid)

    arbi_taskname = f"{taskname}_review"
    arbi_taskid = dbo.get_task_id_by_name(arbi_taskname)

    delivery_folder = Path(f"H:/PipelineFTP/Amazon - Luigi/Handback_q8/{strtoday()}/{taskid}_{taskname}")
    delivery_folder.mkdir(parents=True, exist_ok=True)
    csvo_1 = CSVOperator(str(Path(f"{delivery_folder}/{taskname}_annotator1.csv")))
    csvo_2 = CSVOperator(str(Path(f"{delivery_folder}/{taskname}_annotator2.csv")))
    csvo_3 = CSVOperator(str(Path(f"{delivery_folder}/{taskname}_arbitrated.csv")))
    annotator1_lines = []
    annotator2_lines = []
    arbitrated_lines = []
    mhitid_list = []
    for i in range(len(hitids)):
        hitid = hitids[i]
        hit_data = dbo.get_hits_data_handled_done_by_by_hit_id(hitid)
        mhitid = dbo.get_mHitID_by_hitid(hitid)
        given_data = dbo.get_given_data_by_hit_id(hitid)
        given_data_dict = json.loads(given_data)
        data_handled = hit_data[0]
        done_by = hit_data[1]
        qa_data = dbo.get_qadata_by_hitid(hitid)
        if qa_data is None:
            if data_handled is not None and done_by is not None:
                data_handled = html.unescape(data_handled)
            else:
                print(f"{hitid} not finished")
                continue
        else:
            data_handled = html.unescape(qa_data)
        data_handled_dict = json.loads(data_handled)
        given_data_dict.update(data_handled_dict)
        if mhitid not in mhitid_list:
            annotator1_lines.append(given_data_dict)
            mhitid_list.append(mhitid)
        else:
            annotator2_lines.append(given_data_dict)

    arbi_hitids = dbo.get_hits_id_by_task_id(arbi_taskid)

    csvo_1.dict_to_csv(annotator1_lines)
    csvo_2.dict_to_csv(annotator2_lines)
    # csvo_3.dict_to_csv(arbitrated_lines)


if __name__ == "__main__":
    print("Version: V1.0.0 Update At 20220514 By Andrew")
    # taskid_list = sys.argv[1].split(',')
    taskid_list = ['3311255']
    for taskid in taskid_list:
        main(taskid)

