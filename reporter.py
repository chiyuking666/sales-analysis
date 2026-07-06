import pandas as pd
import os
def report_sales(result_dict: dict,path: str) -> str:
    os.makedirs(path, exist_ok=True)
    path = os.path.join(path,'summary.xlsx')
    try:
        with pd.ExcelWriter(path) as writer:
            for name,df in result_dict.items():
                df.to_excel(writer,sheet_name=name,index=False)
    except PermissionError:
        raise PermissionError(
            f'无法写入 {path}，请先关闭已打开的Excel文件。'
        )
    return path