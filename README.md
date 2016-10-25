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
npm install

# One time setup:
datalogy/manage.py migrate
datalogy/manage.py createsuperuser

# Start the livereload server
gulp

# Start the django server
datalogy/manage.py runserver 0.0.0.0:8000
```
Visit [http://localhost:8000](http://localhost:8000)
