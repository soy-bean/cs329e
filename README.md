# cs329e-idb

#### Group Information
[Github Repository](https://github.com/arr3385/cs329e-idb/)
Canvas Group Number: 2




[![Build Status](https://travis-ci.org/arr3385/cs329e-idb.svg?branch=master)](https://travis-ci.org/arr3385/cs329e-idb)


## Installation
These instructions are for bash shells on macOS or most Unix-like operating systems.
To install this make a directory for the project and clone the git repo.

    mkdir canja
    cd canja
    git clone "https://github.com/arr3385/cs329e-idb.git"

Then you'll want to create a virtual environment, activate the virtual environment, then download the dependencies.

    python3.5 -m virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Change to the dev branch to make any changes.

    git checkout dev

To test the application run the make file.

    make test


## Installing PostgreSQL

These are for macOS instructions using [Homebrew](https://brew.sh/)

    brew install postgresql


Then check if it is installed with:

    postgres --version

Next use brew to start the database:

    pg_ctl -D /usr/local/var/postgres start && brew services start postgresql

To stop the psql service use:

    brew services stop postgresql

If you're having trouble starting PostgreSQL then try these commands:

    psql -d template1

If you log into the template1 database, then you have PostgreSQL intalled and running.

    createdb
    psql -h localhost

If you are getting an error about not having a postgres role and used brew to install it, then try:

    /usr/local/Cellar/postgresql/10.0/bin/createuser -s postgres

To create a database use:

    python create_db.py

If it runs and you got no errors then make sure it added it to the database called postgres:

    psql
    \l
    \c postgres
    select * from book;

You should get a table of values.








## Coverage
Checking for code coverage is important to know what part of the app
has not been tested yet.

    coverage run ./test.py
    coverage report -m ./*.py > coverage.txt

The -m flag is going to show us the lines that have not been tested in the canja.py.
So you can open the coverage.txt to see what lines need unit tests.
