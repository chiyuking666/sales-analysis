import pandas as pd
import os
def report_sales(result_dict: dict,path) -> None:
    os.makedirs(path, exist_ok=True)
    path = os.path.join(path,'summary.xlsx')
    with pd.ExcelWriter(path) as writer:
        for name,df in result_dict.items():
            df.to_excel(writer,sheet_name=name,index=False)
