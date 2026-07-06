from pathlib import Path
import pandas as pd

folder = Path('./input')
files = []
dfs = []

def read_and_merge():
    if not folder.exists():
        print('文件夹不存在')
        return pd.DataFrame()

    for item in folder.iterdir():
        if item.is_file() and item.suffix == '.xlsx':
            files.append(item)
    if not files:
        print('没有Excel文件')
        return pd.DataFrame()
    for file in files:
        df = pd.read_excel(file)
        dfs.append(df)
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame()

print(read_and_merge())
