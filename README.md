# MyTutor webapp

App to aid disance learning. This webapp has ability to 
1. Authenticate users.
2. Upload a video by user given permisiions
3. Create courses.
4. Play videos.

## How to deploy


### Prerequisites - 
1. python3 (https://www.python.org/downloads/source/) 
2. pip3 (https://pip.pypa.io/en/stable/installation/)


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
