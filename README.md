# 销售统计整合工具

## 项目简介

这是一个使用 Python 编写的销售数据统计工具。

支持读取多个 Excel 文件，自动合并数据、清洗异常数据、统计销售情况，并生成汇总报表。

---

## 项目结构

```
sales_project/
│
├── input/            # 输入Excel文件
├── output/           # 输出统计结果
│
├── reader.py         # 读取Excel       
├── analyzer.py       # 数据清洗，数据统计
├── exporter.py       # 导出Excel
├── main.py           # 程序入口
│
└── README.md
```

---

## 环境要求

- Python 3.13+
- pandas
- openpyxl

---

## 安装依赖

```bash
pip install pandas openpyxl
```

---

## 使用方法

把所有销售 Excel 放入

```
input/
```

运行

```bash
python main.py
```

程序将在

```
output/
```

生成

```
summary.xlsx
```

---

## 输入数据要求

Excel 至少包含以下字段：

| 列名 |
|----|
| 日期 |
| 地区 |
| 产品 |
| 数量 |
| 单价 |

程序会自动计算销售额。

---

## 输出结果

summary.xlsx 包含多个工作表：

- 总销售表
- 地区销售统计
- 产品销售统计

---

## 数据清洗

程序会自动：

- 删除完全空白行
- 删除重复数据
- 将地区为空的数据修改为“未知”
- 转换数量、单价为数值类型
- 删除非法数据（数量≤0、单价≤0）

---

## 作者

chiyuking666