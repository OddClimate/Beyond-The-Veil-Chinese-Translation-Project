import json

# 读取 JSON 文件
with open("zh_cn.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 读取 lang 文件并解析为字典
lang = {}
with open("zh_cn.lang", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        # 跳过空行和注释行
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            lang[key.strip()] = value.strip()

# 遍历 JSON，替换值
for key in data:
    if key in lang:
        data[key] = lang[key]

# 保存结果
with open("zh.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("替换完成，结果已保存到 output.json")
