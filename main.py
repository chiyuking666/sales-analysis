import reader
import analyzer
import exporter
def main():
    df=reader.read_and_merge()
    if df.empty:
        print('数据为空')
    else:
        result = analyzer.analyze_excel(df)
        try:
            exporter.export_sales(result,'./output')
            print('excel文件导出成功！')
        except PermissionError as e:
            print(e)


if __name__ == '__main__':
    main()