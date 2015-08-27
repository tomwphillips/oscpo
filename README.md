# oscpo
Fiddling around with the Ordance Survey Code-Point Open database of post codes, eastings, and northings.

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

## Requirements
* [peewee](https://github.com/coleifer/peewee)