from peewee import *

database = SqliteDatabase('mvin.db')


class BaseModel(Model):
    class Meta:
        database = database


class MfrCodes(BaseModel):
    code = CharField(max_length=7, unique=True, primary_key=True)


class Vin(BaseModel):
    vin = CharField(max_length=17, unique=True,primary_key=True)
    mfrCode = ForeignKeyField(MfrCodes, related_name='mfrs')


class Makes(BaseModel):
    make = CharField(unique=True)


class Models(BaseModel):
    model = CharField(unique=True)


class Years(BaseModel):
    year = CharField(max_length=4, unique=True,primary_key=True)


class EngineCodes(BaseModel):
    code = CharField(max_length=7, unique=True,primary_key=True)


class EngineBase(BaseModel):
    liters = CharField(max_length=4)
    cc = CharField(max_length=4)
    cid = CharField(max_length=4)
    cylinder = CharField(max_length=4)
    block = CharField(max_length=4)
    boreInch = CharField(max_length=4)
    boreMetric = CharField(max_length=4)
    strokeInch = CharField(max_length=4)
    strokeMetric = CharField(max_length=4)
    display = CharField()


class Vehicles(BaseModel):
    make = ForeignKeyField(Makes, related_name='makes')
    model = ForeignKeyField(Models, related_name='models')
    year = ForeignKeyField(Years, related_name='years')
    engine = ForeignKeyField(EngineBase, related_name='engines')
    engineCode = ForeignKeyField(EngineCodes, related_name='engineCodes')
    mfrCode = ForeignKeyField(MfrCodes, related_name='mfrCodes')

    class Meta:
        primary_key = CompositeKey('make','model','year','engine','engineCode','mfrCode')


def create_tables():
    database.connect()
    database.create_tables([MfrCodes, Vin, Makes, Models, Years, EngineCodes, EngineBase, Vehicles])


def drop_tables():
    database.drop_tables([Vehicles, Vin, MfrCodes, Makes, Models, Years, EngineCodes, EngineBase])
