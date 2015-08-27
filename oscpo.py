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


def formatpostcode(postcode):
    """Format a postcode so it can be queried against OS CPO.

    Examples
    --------
    'W1 2AA' --> 'W1  2AA'
    'SW7 2AZ' --> 'SW7 2AZ'
    'WC2H 8LG' --> 'WC2H8LG'
    """
    postcode = postcode.replace(' ', '') # remove all spaces
    postcode = postcode.upper()
    if len(postcode) == 7:
        return postcode
    elif len(postcode) == 6:
        return postcode[0:3] + ' ' + postcode[3:]
    elif len(postcode) == 5:
        return postcode[0:2] + '  ' + postcode[2:]
    else:
        raise ValueError('Postcode too long or short.')
