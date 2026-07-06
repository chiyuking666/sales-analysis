import pandas as pd

def analyze_excel(df: pd.DataFrame):
    df = clean_data(df)
    df = calculate_sales(df)
    df_region = group_by_region(df)
    df_products = group_by_products(df)
    result = {
        '总销售表':df,
        '地区销售统计':df_region,
        '产品销售统计':df_products,
    }
    return result

def calculate_sales(df: pd.DataFrame) -> pd.DataFrame:
    df['销售额'] = df['数量'] * df['单价']
    return df

def group_by_region(df: pd.DataFrame) -> pd.DataFrame:
    dg = df.groupby('地区')
    df_region = dg['销售额'].sum().reset_index()
    df_region.columns = ['地区','总销售额']
    return df_region

def group_by_products(df: pd.DataFrame) -> pd.DataFrame:
    dg = df.groupby('产品')
    df_products = dg['销售额'].sum().reset_index()
    df_products.columns = ['产品','总销售额']
    return df_products
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    REQUIRED_COLUMNS = {'数量', '单价', '产品', '地区'}
    df = df.copy()
    df = df.dropna(how='all')
    df = df.drop_duplicates()

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f'缺少必需列：{missing}')
    df['数量'] = pd.to_numeric(df['数量'],errors='coerce')
    df['单价'] = pd.to_numeric(df['单价'],errors='coerce')

    df = df.dropna(subset=['数量', '单价'])
    df["地区"] = df["地区"].fillna("未知")
    df["地区"] = df["地区"].replace("", "未知")
    df["地区"] = df["地区"].str.strip().replace("", "未知")
    df = df[(df['数量']>0) & (df['单价']>0)]
    df = df.drop_duplicates()
    return df

