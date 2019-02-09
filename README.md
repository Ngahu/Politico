[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6024222a8fcf4c5dab269b82d20ee2e3)](https://www.codacy.com/app/Ngahu_2/Politico?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Ngahu/Politico&amp;utm_campaign=Badge_Grade) [![Maintainability](https://api.codeclimate.com/v1/badges/05539977faa426d8712e/maintainability)](https://codeclimate.com/github/Ngahu/Politico/maintainability)   [![Build Status](https://travis-ci.org/Ngahu/Politico.svg?branch=develop)](https://travis-ci.org/Ngahu/Politico) [![Coverage Status](https://coveralls.io/repos/github/Ngahu/Politico/badge.svg)](https://coveralls.io/github/Ngahu/Politico)

## Project Overview
Politico is a platform that enables citizens to give their mandate to politicians running for different government offices while building trust in the process through transparency.





## Required Features

1. A user should be able to get all parties record.
2. A user with an account should be able to log into Politico.
3. An administrator should be able to crete a political party in Politico.
4. A user with an account should be able to declare candidacy for specific post.
5. A user should be able to see election results.
6. Admin should be able to edit a party information.
7. A user should be able to sign up to Politico.
8. An admin should be able to delete a political party.
9.  A user should be able to log out of Politico.
10.  A user should be able to get a specific politician profile.




# Installation and Setup
```
https://github.com/Ngahu/Politico.git
```


## Create a virtual environment

```
python3 -m venv venv;
source venv/bin/activate
```
If you need to install virtualenv:
```
virtualenv venv
```

## Activate the virtual environment
Before you begin you will need to activate the corresponding environment
```
source venv/bin/activate
```
## Install requirements
```
pip install -r politico_api/requirements.txt
```


## Running the application
After the configuration, you will run the app 
```
cd political_api

export FLASK_APP=run.py
export FLASK_ENV=development
flask run
```


#Api Endpoints
