import pandas as pd
import json

# 读取原始 CSV 文件
df = pd.read_csv("Data jobs salaries.csv")

# 按 年份、国家、职位 分组，计算平均薪资
grouped = (
    df.groupby(['work_year', 'company_location', 'job_title'])['salary_in_usd']
    .mean()
    .reset_index()
)

# 构建嵌套结构: year -> country -> [{title, salary}]
nested_data = {}

for _, row in grouped.iterrows():
    year = str(row['work_year'])
    country = row['company_location']
    title = row['job_title']
    avg_salary = round(row['salary_in_usd'], 2)

    nested_data.setdefault(year, {}).setdefault(country, []).append({
        "title": title,
        "salary": avg_salary
    })

# 对每个国家职位列表按薪资从高到低排序
for year_data in nested_data.values():
    for job_list in year_data.values():
        job_list.sort(key=lambda x: x['salary'], reverse=True)

# 保存为 JSON 文件
with open("salary_by_year_country_avg.json", "w") as f:
    json.dump(nested_data, f, indent=2)

print("✅ 平均薪资 JSON 文件已保存为 salary_by_year_country_avg.json")
