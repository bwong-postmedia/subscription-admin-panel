# subscription-admin-panel
Django admin panel UI for managing subscription details

## Setup
1. Create a virtual environment for the project

```bash
$ cd mysite
$ python3 -m venv env
```

2. Activate virtual environment and install packages

```bash
$ source env/bin/activate
$ pip install -r requirements.txt
$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py collectstatic
```

3. Create a super user

```bash
$ ./manage.py createsuperuser
```

4. Start the server

```bash
$ ./manage.py runserver
```