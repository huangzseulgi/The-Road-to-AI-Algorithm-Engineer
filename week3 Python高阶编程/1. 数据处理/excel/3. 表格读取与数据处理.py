import pandas as pd

# # 读取CSV表格
# data_loc = r'resources/销售数据.csv'
# data = pd.read_csv(data_loc)
# print(data)

# 读取excel文件
data_loc = r'resources/销售数据.xlsx'
data = pd.read_excel(data_loc)
print(data.head())  # 输入头几行
print(data.tail())  # 输入尾5行

# 行和列在loc索引中就是[行, 列]
# 读取第一行的值
data_0 = data.loc[0]
print(data_0)

# 定位指定列
data_1 = data.loc[:, "大类编码"]
print(data_1)

# 定位指定行和列
data_2 = data.loc[1, "大类编码"]
print(data_2)

# 对行和列使用切片
data_3 = data.loc[1:3, "大类编码"]
print(data_3)

# 提取符合要求的元素
data_4 = data.loc[data["销售数量"] > 10]
print(data_4)
data_5 = data.loc[data["销售数量"] > 10, ["小类编码", "小类名称"]]
print(data_5)

# 数据分组和排序
data_extract = data.groupby('商品类型')['销售金额'].sum()  # 选定商品类型做分组操作 其中将相同商品类型的销售金额进行汇总
data_extract = data_extract.reset_index()  # 排序

# 表格数据保存
data_extract.to_csv('处理好的数据.csv', encoding='gbk', index=False)  # index=false即不要把索引写入表格
data_extract.to_excel('处理好的数据.xlsx', index=False)
