import reader
import analyzer
import reporter
def main():
    df=reader.read_and_merge()
    if df.empty:
        print('数据为空')
    else:
        result = analyzer.analyze_excel(df)
        reporter.report_sales(result,'./output')
        print('excel文件导出成功！')


if __name__ == '__main__':
    main()