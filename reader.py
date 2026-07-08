from pathlib import Path
import pandas as pd

folder = Path('./input')


def _is_supported_excel_file(file_path: Path) -> bool:
    return (
        file_path.is_file()
        and file_path.suffix.lower() == '.xlsx'
        and not file_path.name.startswith('~$')
    )


def read_and_merge() -> pd.DataFrame:
    if not folder.exists():
        print('文件夹不存在')
        return pd.DataFrame()

    files = sorted(item for item in folder.iterdir() if _is_supported_excel_file(item))
    if not files:
        print('没有Excel文件')
        return pd.DataFrame()

    dfs = [pd.read_excel(file) for file in files]
    return pd.concat(dfs, ignore_index=True)

