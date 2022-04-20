
# Django + Cassandra

A Django Project Configured with Open Source Apache Cassandra Database.  

Get You Free Datastax Cassandra DB from [here](https://www.datastax.com/)   

## Features:
- [x] Can Use Multiple Database.
- [x] Can use Cassandra Database in Admin Panel.
- [x] Configured for Production Ready.
- [x] Encrypt and Decrypt  Cassandra DB for Security.
- [x] Easy to Configure for Your Need.


### Get the Code

#### Clone Repository 

```
$ mkdir django_with_cassandra
$ cd django_with_cassandra
$ git clone https://github.com/Arvind-4/Django-Cassandra.git .
```
- Create Virtual Environment for Python

```
$ pip install virtualenv
$ python3.9 -m venv .
```

- Activate Virtual Environment

```
$ source bin/activate
```

- Install Dependencies (for virtual environment)

```
$ pip install -r requirements.txt
```

- Install Dependencies (for Poetry)

```
$ poetry install
```

Create a **.env** file in the Root of the Project. Add Your Credentials to **.env** file.

```
ASTRA_DB_CLIENT_ID=xxxx
ASTRA_DB_CLIENT_SECRET=ixxxx
ASTRA_DB_TOKEN=xxxx
ASTRA_DB_KEYSPACE=xxxx

ENCRYPTION_KEY=xxxx

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=1234
DJANGO_SUPERUSER_EMAIL=admin@admin.com

DJANGO_SECRET_KEY=secret-key
DJANGO_DEBUG=1
DJANGO_ALLOWED_HOSTS=*
```

- Make a Folder **ignored** in the Root of the Project.
- Copy the Connection Bundle to **ignored** folder.
- Rename th file to **connect.zip** for convenience.


- Your Project Structure should be Similar to this
```
$ ls 
	bin  				# Python Virtual Environment Files
	commands  			# Shell Commands
	ignored  			# Cassandra DB
	lib  				# Python Virtual Environment Files
	poetry.lock  		# Poetry lock file
	pyproject.toml  	# Poetry config file
	pyvenv.cfg  		# Config Files
	requirements.txt  	# Python Requirements for Project
	runtime.txt  		# Python Version
	web 				# Python Backend Code
```

- Run Server 
```
$ cd web
$ uvicorn backend.asgi:application --reload
```

- To run Commands from **commands** directory
```
$ chmod +x commands/*.sh
$ commands/run.prod.sh
```
