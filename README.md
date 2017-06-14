# Acceso Group

## Requirements

Python 3.5.x or upper

## Problem 1 - Palindromic number

### Up & Running

By default digits = 3
```
$ python3 problem_1.py
906609
```

You could check for two-digits number too:

```
$ python3 problem_1.py 2
9009
```

## Problem 2 - Spiral

### Up & Running

By default spiral size = 1001

```
$ python3 problem_2.py
669171001
```

You could check for any spiral size too:

```
$ python3 problem_2.py 1000001
666669166671000001
```

## Mafia Web

Web based on Django Rest Framework (backend) and AngularJS (1.6.x) (frontend)

------ INCOMPLETE ------

### Requirements

Django
npm
bower
yeoman
Grunt

### Up & Running

Python

```
$ pip install virtualenvwrapper
$ mkvirtualenv -p /usr/bin/python3 mafia
(mafia)$ pip install -r mafia_web/requirements.txt
(mafia)$ cd mafia_web/fbi_web/ && python manage.py runserver
```

Web

```
$ npm install -g grunt-cli bower yo generator-karma generator-angular
$ cd mafia_web/fbi_web/mafia/web
$ grunt serve
```
