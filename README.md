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

## Coverage
Checking for code coverage is important to know what part of the app
has not been tested yet.

    coverage run ./test.py
    coverage report -m ./*.py > coverage.txt

The -m flag is going to show us the lines that have not been tested in the canja.py.
So you can open the coverage.txt to see what lines need unit tests.
