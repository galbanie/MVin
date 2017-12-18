from mvin_db import *
import xlrd
from pprint import pprint
import json


def validate(data_mapping):
    if data_mapping is None:
        return False
    with open('mvin.template.json') as template:
        structure = json.load(template)
        if ordered(data_mapping) != ordered(structure):
            return False
    return True


def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj


def populate(mvin_data):
    for file in mvin_data['files']:
        book = xlrd.open_workbook(file['path'])
        sheets = []
        if not file['sheets']:
            sheets = book.sheets()
        else:
            for sh in file['sheets']:
                if isinstance(sh, int):
                    try:
                        sheets.append(book.sheet_by_index(sh))
                    except IndexError:
                        continue
                elif isinstance(sh, str):
                    try:
                        sheets.append(book.sheet_by_name(sh))
                    except xlrd.biffh.XLRDError:
                        continue
                else:
                    continue
        for sheet in sheets:
            print('Sheet : ' + str(sheet.name))
            for row in range(1, sheet.nrows):
                print('Row number : ' + str(row))
                # vehicle_record = file['map'].fromkeys(file['map'].keys())
                vehicle_record = {
                    "make": None,
                    "model": None,
                    "year": None,
                    "engine": None,
                    "mfrCode": None,
                    "engineCode": None
                }
                vin_record = {
                    "vin": None,
                    "mfrCode": None
                }
                for key, value in file['map'].items():
                    record = value.fromkeys(value.keys())
                    for col in range(0, sheet.ncols):
                        print(str(col_name) + ' - ' + str(col_value))
                        col_name = sheet.cell(0, col).value
                        col_value = sheet.cell(row, col).value
                        if col_name in value.values():
                            record[list(value.keys())[list(value.values()).index(col_name)]] = str(col_value)
                            if None not in record.values():
                                if key == 'vin':
                                    # mfr = record['mfrCode']
                                    # if '.' not in mfr:
                                    #     mfr = mfr[:3] + '.' + mfr[-3:]
                                    record['mfrCode'] = tables['mfrCode'].get_or_create(code=record['mfrCode'])[0]
                                    tables['vin'].get_or_create(defaults=record)
                                    # pprint(record)
                                else:
                                    vehicle_record[key] = tables[key].get_or_create(defaults=record)[0]
                                    # pprint(record)
                                continue
                        else:
                            continue
                if None not in vehicle_record.values():
                    tables['vehicle'].get_or_create(defaults=vehicle_record)
                    # pprint(vehicle_record)
                    continue


# def populate_database_coverage():
#     book = xlrd.open_workbook('xlsx/Coverage.xlsx')
#     sheet = book.sheet_by_index(1)
#     data = []
#     for row in range(1, sheet.nrows):
#         values = {}
#         for col in range(0, sheet.ncols):
#             values[sheet.cell(0, col).value] = sheet.cell(row, col).value
#         data.append(values)
#     print(data[0])
#     for d in data:
#         make, model, year, engine, engine_code, mfr_code = None, None, None, None, None, None
#         try:
#             make = Makes.get_or_create(make=d['Make'])
#             model = Models.get_or_create(model=d['Model'])
#             year = Years.get_or_create(year=d['Year'])
#             engine = EngineBase.get_or_create(
#                 liters=d['EngineLiters'],
#                 cc=d['EngineCC'],
#                 cid=d['EngineCID'],
#                 cylinder=d['EngineCylinder'],
#                 block=d['EngineBlock'],
#                 boreInch=d['EngBoreInch'],
#                 boreMetric=d['EngBoreMetric'],
#                 strokeInch=d['EngStrokeInch'],
#                 strokeMetric=d['EngStrokeMetric'],
#                 display=d['Engine (Display Only)']
#             )
#             engine_code = EngineCodes.get_or_create(code=d['EngineDesignation'])
#             mfr_code = MfrCodes.get_or_create(code=d['MfrBodyCode'])
#             # print(make, model, year, engine, engine_code, mfr_code)
#             # print(type(make), type(model), type(year), type(engine), type(engine_code), type(mfr_code))
#             Vehicles.get_or_create(
#                 make=make[0],
#                 model=model[0],
#                 year=year[0],
#                 engine=engine[0],
#                 engineCode=engine_code[0],
#                 mfrCode=mfr_code[0]
#             )
#         except IntegrityError:
#             pass
#
#
# def populate_database_vin():
#     book = xlrd.open_workbook('xlsx/MVin.xlsx')
#     for sheet in book.sheets():
#         if sheet.name == 'VR':
#             continue
#         for row in range(1, sheet.nrows):
#             values = []
#             for col in range(0, sheet.ncols):
#                 values.append(sheet.cell(row, col).value)
#             # Vin.create(mfrCode=values[0], vin=values[3])


if __name__ == '__main__':
    create_tables()
    # populate_database_coverage()
    # for year in Years.select():
    #     print(year.year)
    # drop_tables()
    with open('mvin.test.json') as test_file:
        populate(json.load(test_file))
    # mfr = '107025'
    # if '.' not in str(mfr):
    #     # mfr = mfr[0:3] + '.' + mfr[3:6]
    #     mfr = mfr[:3] + '.' + mfr[-3:]
    #     pprint(mfr)
