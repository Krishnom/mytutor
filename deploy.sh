#Install prerequisites
sudo yum -y install epel-release;
sudo yum -y install nginx
sudo yum -y install python-virtualenv


#Prepare directory
sudo mkdir /opt/mytutor
sudo chown -R $USER:$USER  /opt/mytutor
cd /opt/mytutor; git clone https://github.com/Krishnom/mytutor.git .
sudo ln -s /opt/mytutor/nginx.conf /etc/nginx/sites-enabled/
#activate virtualenv
virtualenv -p python3 /opt/mytutor/venv-mytutor
source /opt/mytutor/venv-mytutor/bin/activate

#Activate virtual env
activate

#Setup
pip install -r requirements.txt
python manage.py makemigrations app
python manage.py migrate
python manage.py collectstatic

#Run server
uwsgi --http :8001 --module mytutor.wsgi

