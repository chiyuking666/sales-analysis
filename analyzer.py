import pandas as pd
def analyze_excel(df: pd.DataFrame):
    df = calculate_sales(df)
    df_region = group_by_region(df)
    df_products = group_by_products(df)
    result = {
        '总销售表':df,
        '地区销售统计':df_region,
        '产品销售统计':df_products,
    }
    return pd.DataFrame(result)

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

