from glob import glob
import csv
from peewee import *

dbname = 'oscpo.db'

database = SqliteDatabase(dbname)


class BaseModel(Model):
    class Meta:
        database = database


class Location(BaseModel):
    postcode = CharField(unique=True, max_length=8)
    positional_quality_indicator = IntegerField()
    eastings = IntegerField()
    northings = IntegerField()
    country_code = TextField()
    NHS_regional_HA_code = TextField()
    NHS_HA_code = TextField()
    admin_county_code = TextField()
    admin_district_code = TextField()
    admin_ward_code = TextField()


def create_tables():
    database.connect()
    database.create_tables([Location])

    headings = ['postcode',
                'positional_quality_indicator',
                'eastings',
                'northings',
                'country_code',
                'NHS_regional_HA_code',
                'NHS_HA_code',
                'admin_county_code',
                'admin_district_code',
                'admin_ward_code']

    cpofiles = glob('codepo_gb/Data/CSV/*.csv')

    for i, cpofile in enumerate(cpofiles):
        print('Loading file {} of {}'.format(i+1, len(cpofiles)))

        f = open(cpofile)
        reader = csv.reader(f, delimiter=',')
        entries = [dict(zip(headings, row)) for row in reader]

        with database.atomic():
            n = 50  # chunks of 50 at a time
            for idx in range(0, len(entries), n):
                Location.insert_many(entries[idx:idx+n]).execute()

    print('Loaded {} records'.format(Location.select().count()))
