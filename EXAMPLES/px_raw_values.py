import openpyxl as px

def main():
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb['US Presidents']  # get active sheet
    values = ws.values
    next(values)
    for row in values:  # loop over rows in generator
        print(row[:5])   # print first 5 elements of row tuple


if __name__ == '__main__':
    main()
