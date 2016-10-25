# datalogy
A site to capture our internal data science challenges and submissions.

## Getting Started
```
vagrant up
vagrant ssh

cd /vagrant

# If this is your first time:
mkvirtualenv --python=`which python3` datalogy

# Else:
workon datalogy

# Install dependencies
pip install -r requirements.txt
bower install

cd /vagrant/datalogy
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8000
```
Visit [http://localhost:8000](http://localhost:8000)
