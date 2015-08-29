from glob import glob
import csv
from peewee import *

database = SqliteDatabase(None)


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
    """Create the database tables."""
    database.connect()
    database.create_tables([Location])


def populate_tables(codepo_gb_location=None):
    """Populate the database tables.

    Argument:
    ---------
    codepo_gb_location: location of the codepo_gb folder. Default is empty,
    i.e. it's in the current directory. No trailing slash.
    """
    database.connect()

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

    if codepo_gb_location is None:
        codepo_gb_location = ''

    cpofiles = glob(codepo_gb_location + '/codepo_gb/Data/CSV/*.csv')

    if len(cpofiles) == 0:
        raise ValueError('Could not locate Code-Point Open CSV files')

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
    """Format a postcode so it can be queried against OS CPO."""
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


def eastings_northings(postcode):
    """Return (eastings, northings) for postcode."""
    query = Location.get(Location.postcode == formatpostcode(postcode))
    return (query.eastings, query.northings)
