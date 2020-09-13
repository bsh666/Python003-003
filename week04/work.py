# -*- coding:utf-8 -*-
import pprint
import pandas as pd


# 初始化数据
df = pd.DataFrame(
    [
        ["Tim", 22, "male"],
        ["Tom", 24, "male"],
        ["Jack", 26, "male"],
        ["Anna", 31, "female"],
        ["Jones", 18, "female"]
    ] * 500,
    columns=["name", "age", "gender"]
)
df2 = pd.DataFrame(
    [["pork", 10, "$"], ["lamp", 12, "$"], ["beef", 15, "$"]],
    columns=["goods", "price", "unit"]
)


# 1. SELECT * FROM data;
value = df.values
python_value = value.tolist()
pprint.pprint(value)
pprint.pprint(python_value)


# 2. SELECT * FROM data LIMIT 10;
value = df.head(10)
python_value = value.to_numpy().tolist()
pprint.pprint(value)
pprint.pprint(python_value)


# 3. SELECT id FROM data;  //id 是 data 表的特定一列
ids = df.index
python_value = value.to_numpy().tolist()
pprint.pprint(ids)
pprint.pprint(python_value)


# 4. SELECT COUNT(id) FROM data;
count = df.index.size
pprint.pprint(count)


# 5. SELECT * FROM data WHERE id<1000 AND age>30;
value = df.loc[:1000].query("age >30")
python_value = value.to_numpy().tolist()
pprint.pprint(value)
pprint.pprint(python_value)

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# 这题没太读懂意思
value = df.groupby(df.index).age.nunique()
pprint.pprint(value)

# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
value = pd.merge(df, df2, left_index=True, right_index=True, how="inner")
python_value = value.to_numpy().tolist()
pprint.pprint(value)
pprint.pprint(python_value)

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
value = pd.concat([df, df2])
python_value = value.to_numpy().tolist()
pprint.pprint(value)
pprint.pprint(python_value)
#
# 9. DELETE FROM table1 WHERE id=10;
deleted_row_df = df.drop([10])
pprint.pprint(deleted_row_df)
#
# 10. ALTER TABLE table1 DROP COLUMN column_name;  column_name = name

deleted_column_df = df.drop("name", axis=1)
pprint.pprint(deleted_column_df)
