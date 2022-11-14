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
    # 根据3834的taskid拼接获取3844的taskid
    arbi_taskname = f"{taskname}_review"
    arbi_taskid = dbo.get_task_id_by_name(arbi_taskname)

    delivery_folder = Path(f"H:/Wenjing/test/{strtoday()}/{taskid}_{taskname}")
    delivery_folder.mkdir(parents=True, exist_ok=True)
    csvo_1 = CSVOperator(str(Path(f"{delivery_folder}/{taskname}_annotator1.csv")))
    csvo_2 = CSVOperator(str(Path(f"{delivery_folder}/{taskname}_annotator2.csv")))
    csvo_3 = CSVOperator(str(Path(f"{delivery_folder}/{taskname}_arbitrated.csv")))
    annotator1_lines = []
    annotator2_lines = []
    arbitrated_lines = []
    mhitid_list = []
    mhitid_dict = {}
    for i in range(len(hitids)):
        hitid = hitids[i]
        hit_data = dbo.get_hits_data_handled_done_by_by_hit_id(hitid)
        mhitid = dbo.get_mHitID_by_hitid(hitid)
        given_data = dbo.get_given_data_by_hit_id(hitid)
        given_data_dict = json.loads(given_data)
        data_handled = hit_data[0]
        done_by = hit_data[1]
        qa_data = dbo.get_qadata_by_hitid(hitid)
        # data_handled根据不同情况进行取值
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
        # 构建字典{"mhitid1":[{"given_data":{},"hit_data":{}},{"given_data":{},"hit_data":{}}],"mhitid2":[...]}
        if mhitid_dict.get(mhitid) is None:
            mhitid_dict[mhitid] = [{
                "given_data": given_data_dict,
                "hit_data": data_handled_dict
            }]
        else:
            mhitid_dict[mhitid].append({
                "given_data": given_data_dict,
                "hit_data": data_handled_dict
            })
        # 生成excel1和excel2,根据mhitid来分开一人做两份的数据
        if mhitid not in mhitid_list:
            annotator1_lines.append(given_data_dict)
            mhitid_list.append(mhitid)
        else:
            annotator2_lines.append(given_data_dict)
    i = 0
    arbi_hitids = dbo.get_hits_id_by_task_id(arbi_taskid)
    for key, value in mhitid_dict.items():
        # 当构建字典mhitid_dict中的value长度小于2说明不符合一人做两条
        if len(value) != 2:
            print(f"mhitid {key} result error, length {len(value)}")
            continue
        hit_data_dict_1 = value[0].get('hit_data')
        hit_data_dict_2 = value[1].get('hit_data')
        hit_given_dict_1 = value[0].get('given_data')
        hit_given_dict_2 = value[1].get('given_data')
        if hit_data_dict_1 is None or hit_data_dict_2 is None:
            print(f"mhitid {key} result error, hit_data_dict_1 {hit_data_dict_1} hit_data_dict_2 {hit_data_dict_2}")
            continue
        t_dictMerged_1 = dict(hit_data_dict_1)
        t_dictMerged_1.update(hit_given_dict_1)
        t_dictMerged_2 = dict(hit_data_dict_2)
        t_dictMerged_2.update(hit_given_dict_2)
        arbi_hitid = arbi_hitids[i]
        # 当3834一人做两条数据的数据符合下面判断则不写入，else后则是写入到数据库的数据
        if hit_data_dict_1.get('q_one') == hit_data_dict_2.get('q_one') and \
                hit_data_dict_1.get('q_two') == hit_data_dict_2.get('q_two') and \
                hit_data_dict_1.get('q_three') == hit_data_dict_2.get('q_three') and \
                hit_data_dict_1.get('q_four') == hit_data_dict_2.get('q_four') and \
                hit_data_dict_1.get('q_five') == hit_data_dict_2.get('q_five'):
            arbitrated_lines.append(t_dictMerged_1)
        else:
            arbi_hit_data = dbo.get_hits_data_handled_done_by_by_hit_id(arbi_hitid)
            arbi_data_handled = arbi_hit_data[0]
            arbi_done_by = arbi_hit_data[1]
            arbi_qa_data = dbo.get_qadata_by_hitid(arbi_hitid)
            if arbi_qa_data is None:
                if arbi_data_handled is not None and arbi_done_by is not None:
                    arbi_data_handled = html.unescape(arbi_data_handled)
                else:
                    print(f"{arbi_hitid} not finished")
                    continue
            else:
                arbi_data_handled = html.unescape(arbi_qa_data)
            arbi_given_data = dbo.get_given_data_by_hit_id(arbi_hitid)
            if arbi_given_data is None:
                print(f"No given data found for hit {arbi_hitid}")
                continue
            arbi_given_data = json.loads(arbi_given_data)
            arbi_data_handled_dict = json.loads(arbi_data_handled)
            t_dictMerged_3 = dict(arbi_data_handled_dict)
            t_dictMerged_3.update(arbi_given_data)
            arbitrated_lines.append(t_dictMerged_3)
            i += 1
    # csvo_1.dict_to_csv(annotator1_lines)
    # csvo_2.dict_to_csv(annotator2_lines)
    # csvo_3.dict_to_csv(arbitrated_lines)
    print(arbitrated_lines)


if __name__ == "__main__":
    print("Version: V1.0.0 Update At 20221110 By Tanhao.Chen")
    # taskid_list = sys.argv[1].split(',')
    taskid_list = ['3311255']
    for taskid in taskid_list:
        main(taskid)

