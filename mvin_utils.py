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
        pprint(file)

# def populate(mapping, xlsx_paths, sheet_names=None):
#     if sheet_names is None:
#         sheet_names = []
#     for xlsx in xlsx_paths:
#         book = xlrd.open_workbook(xlsx)
#         sheets = []
#         if sheet_names is None:
#             sheets = book.sheets()
#         else:
#             for n in sheet_names:
#                 sheets.append(book.sheet_by_name(str(n)))
#         for sheet in sheets:
#             data = []
#             for row in range(1, sheet.nrows):
#                 values = {}
#                 for col in range(0, sheet.ncols):
#                     values[sheet.cell(0, col).value] = sheet.cell(row, col).value
#                 data.append(values)


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
    # create_tables()
    # populate_database_coverage()
    # for year in Years.select():
    #     print(year.year)
    # drop_tables()
    # with open('mvin.template.json') as json_file:
    #     data = json.load(json_file)
    #     pprint(data)
    with open('mvin.test.json') as test_file:
        populate(json.load(test_file))
        # pprint(validate(json.load(test_file)))
