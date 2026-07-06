import pandas as pd
import random
from datetime import datetime, timedelta
import os
regions = [
    '上海',
    '广东',
    '福建',
    '北京',
    '河南',
    '河北',
    '浙江',
    '海南',
    '湖南',
    '湖北'
]

products = [
    "笔记本电脑",
    "鼠标",
    "键盘",
    "显示器",
    "耳机",
    "打印机",
    "路由器",
    "移动硬盘",
]



date_formats = [
    '%Y-%m-%d',
    '%Y/%m/%d',
    '%Y.%m.%d',
    '%m/%d/%Y',
    '%d-%m-%Y',
]

def random_date():
    start = datetime(2024,1,1)
    d = start + timedelta(days=random.randint(0,500))
    fmt = random.choice(date_formats)
    return d.strftime(fmt)

def generate_one_excel(index):
    rows = []
    for i in range(1000):
        qty = random.randint(1,20)
        price = round(random.uniform(20,5000),2)
        row = {
            '订单号':f'SO{index}{100000+i}',
            '日期':random_date(),
            "地区":random.choice(regions),
            "产品":random.choice(products),
            "单价":price,
            "数量":qty
        }
        rows.append(row)
    df = pd.DataFrame(rows)

    idx = random.sample(range(len(df)),30)
    df.loc[idx,'地区'] = ''

    idx = random.sample(range(len(df)), 20)
    df.loc[idx, '数量'] = 0

    idx = random.sample(range(len(df)), 20)
    df.loc[idx, '单价'] = None

    dup = df.sample(10,random_state=index)
    df = pd.concat([df,dup],ignore_index=True)

    df = df.sample(frac=1).reset_index(drop=True)

    file_name = f'sales_{index}.xlsx'
    path = os.path.join('./input', file_name)
    df.to_excel(path, index=False)

    print(f'生成{file_name}({len(df)}条数据)')

def main():

    os.makedirs('./input', exist_ok=True)
    for index in range(1,11):
        generate_one_excel(index)
    print('\n全部完成！')

if __name__ == '__main__':
    main()
