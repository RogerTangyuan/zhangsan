import openpyxl

def readExcelData(filename,sheetName,coordinate):
    """
    @功能  :这是用来读取excel表格的方法
    """
    excel = openpyxl.load_workbook(filename)
    sheet = excel[sheetName]
    min_row = coordinate.get("min_row")
    max_row = coordinate.get("max_row")
    min_col = coordinate.get("min_col")
    max_col = coordinate.get("max_col")
    dataList = sheet.iter_rows(min_row,max_row,min_col,max_col)
    result = []
    for row in dataList:
        rows = []
        for i in row:
            rows.append(i.value)
        result.append(rows)
    return result

if __name__ == "__main__":
    coordinate = {
        "min_row":2,
        "max_row":6,
        "min_col":1,
        "max_col":4
    }
    
    res = readExcelData("unittest\data\测试数据.xlsx","登录注册",coordinate)
    print(res)
    
