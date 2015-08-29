# oscpo
Fiddling around with the Ordance Survey Code-Point Open database of post codes, eastings, and northings.

## Requirements
* [peewee](https://github.com/coleifer/peewee)

## Install

```
$ git clone https://github.com/tomwphillips/oscpo.git
$ python setup.py install
```

## Loading the data

Download the database from the [Ordance Survey web site](https://www.ordnancesurvey.co.uk/business-and-government/products/code-point-open.html).

It's a zip file containing a folder called `codepo_gb`. Extract it somewhere, in this example the current folder. Then from the Python shell:

```
>>> from oscpo import *
>>> database.init('oscpo.db')  # whatever name you want
>>> create_tables()
>>> populate_tables()
Loading file 1 of 120
Loading file 2 of 120
...
Loading file 120 of 120
Loaded 1686482 records
```

This will load the CSV files into a SQLite database `oscpo.db`. You can now delete `codepo_gb`. If you extracted it somewhere else, specify the path to it as an argument to populate_tables().

## Looking up the eastings and northings for a postcode

```
>>> from oscpo import *
>>> database.init('oscpo.db')  # or wherever you created the db
>>> eastings_northings('SW1A 2AA')
(530047, 179951)
```

## Tests

Tests assume the database is `oscpo.db` and in the same directory as `test_oscpo.py`.