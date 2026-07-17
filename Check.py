import json
import re
#注意,替换的效果可能存在一些BUG 需要手动进行调整
#黑镜键值在这--------->  ^mirror.*?$
while True:
    input_text=input('请利用正则表达式输入待测键值:'+'\n')
    try:
        pattern = re.compile(input_text)
        break
    except:
        print("正则表达式无效 请重试")
    mode=input('是否启用翻译替换功能(Y/N):\n')
    if mode in ['Y','N']:
        break
#此处引用了M.py的代码
old_version_en = {}
with open("en_us.lang", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # 跳过空行和注释行
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            old_version_en[key.strip()] = value.strip()

#转化旧版本中文汉化为字典
old_version_zh = {}
with open("en_us.lang", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # 跳过空行和注释行
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            old_version_zh[key.strip()] = value.strip()

#保存1.20.1版本文本
with open ('en_us.json','r')as f:
    latest_version_en=json.load(f)
with open ('zh_cn.json','r')as f:
    latest_version_zh=json.load(f)

#获取1.20.1版本 的相关键值
key_list=list(latest_version_en.keys())
latest_key=[]
for key in key_list:
    result=pattern.findall(key)
    if result:
        latest_key.append(key)
#此处定义一个函数，便于我们更换汉化文本 此函数的作用是通过键值来定位键
def find_key(target_dict:dict,target_text:str):
    dict_key_list=list(target_dict.keys())
    dict_value_list=list(target_dict.values())
    num=dict_value_list.index(target_text)
    result_key=dict_key_list[num]
    return result_key
#进行核对
IF_ALL_KEYS_CORRECT=1
for latest_key in latest_key:
    text_en=latest_version_en[latest_key]
    print(text_en)
    if text_en in old_version_en.values():
        print(f'{latest_key} 所对应文本正确')
        if mode=='Y':
            old_key=find_key(old_version_en,text_en)
            text_zh=old_version_zh[old_key]
            latest_version_zh[key]=text_zh
    else:
        print(f'错误: {latest_key} 所对应文本错误')
        IF_ALL_KEYS_CORRECT=0
if IF_ALL_KEYS_CORRECT:
    print('所有结果均正确')
else:
    print('请检查 文本中出现匹配错误或\n1.20.1版本中不含此键值')
if mode=='Y':
    with open ('zh_cn_replaced.json','w') as f:
        json.dump(latest_version_zh, f, ensure_ascii=False, indent=2)
        print('替换结果保存成功')
