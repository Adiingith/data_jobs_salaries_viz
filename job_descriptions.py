import pandas as pd
import json

# 读取 CSV 文件
df = pd.read_csv('Data_jobs_salaries_describe.csv', encoding='utf-8')

# 打印所有列名，这样我们可以看到实际的列名
print("Available columns:", df.columns.tolist())

# 然后再选择列名
selected_columns = ['job_title', 'Role_Summary', 'Key_Responsibilities', 'CommonTools_Technologies', 'Skills_Required', 'Career_Path']
df_selected = df[selected_columns]

# 处理 NaN 值，将其替换为空字符串
df_selected = df_selected.fillna('')

# 根据job_title去重，保留第一次出现的记录
df_selected = df_selected.drop_duplicates(subset=['job_title'], keep='first')

# 转换为字典列表
data = df_selected.to_dict(orient='records')

# 保存为 JSON 文件
with open('job_descriptions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("job_descriptions.json generated successfully.")
