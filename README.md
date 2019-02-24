# Hyperledger CryptoBonds 

CryptoBonds is a blockchain application that was built using Hyperledger Sawtooth. The goal of the project is to make a stable coin with its value linked to real life company bonds. CryptoBonds acts as a clearing firm and monitors transactions between the banks and the traders. Traders are able to exchange cryptobonds and other cryptocurrencies with other users. 

CryptoBonds is developed [by five people](https://github.com/crypto-bonds/crypto-bonds-server/graphs/contributors) at HackIllinois 2019, with the help of various mentors.

![](https://i.imgur.com/dwm3xdd.jpg)

## Quick Start

[Click here](https://crypto-bonds.herokuapp.com/cryptoserver/) to access our front end web interface. Our Django project is deployed on Heroku.

## Installation

### 0. Server setup

This application is built using python Django framework deployed on heroku. 

Being a PythonWeb framework, Django requires Python. See [What Python version can I use with Django?](https://docs.djangoproject.com/en/2.1/faq/install/#what-python-version-can-i-use-with-django)

### 1. Install pip
```
$ sudo apt-get install python3-pip
```
**Note**: If your distribution already has pip installed, you might need to update it if it’s outdated

### 2. Set up a virtual environment

It’s a good idea to keep all your virtualenvs in one place, for example in .virtualenvs/ in your home directory.
Create it if it doesn’t exist yet
```
$ mkdir ~/.virtualenvs
```

Now create a new virtualenv by running:
```
$ python3 -m venv ~/.virtualenvs/djangodev
```

On some versions of Ubuntu the above command might fail. Use the virtualenv package instead
```
$ pip3 install virtualenv
$ virtualenv --python=`which python3` ~/.virtualenvs/djangodev
```

The final step in setting up your virtualenv is to activate it:
```
$ source ~/.virtualenvs/djangodev/bin/activate
```

If the source command is not available, you can try using a dot instead:
```
$ . ~/.virtualenvs/djangodev/bin/activate
```

### 3. Install Django 

After you’ve created and activated a virtual environment, enter the command
```
$ pip3 install Django 
```

### 4. Clone repository and run server locally
Clone repository using following command
```
git clone https://github.com/crypto-bonds/crypto-bonds-server.git
```

To run server locally
```
cd crypto-bonds-server
python manage.py runserver
```

### 5. Run server on heroku
To get the code up and running on your device follow 
the instructions here: https://devcenter.heroku.com/articles/django-app-configuration

## Technologies

### Hyperledger Sawtooth BlockChain

https://github.com/hyperledger/sawtooth-core


