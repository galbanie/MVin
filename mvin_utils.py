from openpyxl import load_workbook
import json


def populate(mvin_data):
    for file in mvin_data['files']:
        wb = load_workbook(file['path'])
        print(wb.get_sheet_names())
        sheets = []
        if not file['sheets']:
            sheets = wb.worksheets
        else:
            for sh in file['sheets']:
                if isinstance(sh, str):
                    sheets.append(wb.get_sheet_by_name(sh))
                else:
                    continue
        for sheet in sheets:
            print(sheet.title)


if __name__ == '__main__':
    with open('test.json') as json_map_file:
        populate(json.load(json_map_file))
