# MyTutor webapp

App to aid disance learning

## How to deploy

> Prerequisites - python3 (https://www.python.org/downloads/source/) and pip3 (https://pip.pypa.io/en/stable/installation/)


Execute below commands

```bash
#!/bin/bash
git clone <this git repo>
cd mytutor
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py makemigrations app
python3 manage.py migrate
pythom3 manage.py runserver
```

Once done you can access the website using url <http://localhost:8000>

### TODO list

- Authentication
- store videos in cloud
- REST APIs endpoints
