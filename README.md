# oscpo
Fiddling around with the Ordance Survey Code-Point Open database of post codes, eastings, and northings.

## Requirements
* [peewee](https://github.com/coleifer/peewee)

## Getting the data

Download the database from the [Ordance Survey web site](https://www.ordnancesurvey.co.uk/business-and-government/products/code-point-open.html). Extract it to this folder.

## Loading the database

From the Python shell:

```
>>> from oscpo import *
>>> create_tables()
Loading file 1 of 120
Loading file 2 of 120
...
Loading file 120 of 120
Loaded 1686482 records
```

This will load the CSV files into a SQLite database `oscpo.db`.

## Looking up the eastings and northings for a postcode

```
>>> from oscpo import *
>>> eastings_northings('SW1A 2AA')
(530047, 179951)
```

## Tests

```
$ python test_oscpo.py
```