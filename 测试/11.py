dict_list = [
    {
        'productionA': "Vanity Fair Women's Perfect Lace Spin Cami   #17166",
        'productionB': True,
        'des': 'They are both used for the same purpose',
    },
    {
        'des': 'The person wants to wear a costume of Mad Hatter',
        'productionB': False,
        'productionA': 'Mad Hatter Bandolier Thread Belt Colourful Yarn Costume Bandoleer',

    },
    {
        'des': 'They are both used for the same purpose',
        'productionA': 'Crenova XPE490 HD, Mini, Portable Video Projector, Black',
        'productionB': True,
    },
]


def dict_to_csv(dict_list, delimter=','):
    written_line = []
    # 若字典顺序不对会造成乱序
    for i in range(0, len(dict_list)):
        dict_content = dict_list[i]
        if i == 0:
            headers = ""
            for key in dict_content.keys():
                if isinstance(key, str) and key.startswith('"') and key.endswith('"'):
                    headers += str(key) + delimter
                elif isinstance(key, str) and delimter in str(key):
                    key = '"' + key + '"'
                    headers += str(key) + delimter
                else:
                    headers += str(key) + delimter
            headers = headers[:-len(delimter)]
            written_line.append(headers + "\n")
        contents = ""
        for j in range(len(dict_content.values())):
            value = list(dict_content.values())[j]

            if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
                contents += str(value) + delimter
            elif isinstance(value, str) and delimter in str(value):
                value = '"' + value + '"'
                contents += str(value) + delimter
            else:
                contents += str(value) + delimter
        contents = contents[:-len(delimter)]
        written_line.append(contents + "\n")
    # 对字典的顺序进行排序
    for i, info_dict in enumerate(dict_list):
        header_list = list(dict_list[0].keys())
        if i == 0:
            header = ','.join(header_list)
            written_line.append(header + '\n')
        new_info_dict = {}
        for index in header_list:
            new_info_dict[index] = info_dict[index]
        contents = ""
        for j in range(len(new_info_dict.values())):
            value = list(new_info_dict.values())[j]

            if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
                contents += str(value) + delimter
            elif isinstance(value, str) and delimter in str(value):
                value = '"' + value + '"'
                contents += str(value) + delimter
            else:
                contents += str(value) + delimter
        contents = contents[:-len(delimter)]
        written_line.append(contents + "\n")
    with open('z.csv', "w", encoding='utf-8') as f:
        f.writelines(written_line)


dict_to_csv(dict_list, delimter=',')
