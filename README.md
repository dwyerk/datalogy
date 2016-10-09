# datalogy
A site to capture our internal data science challenges and submissions.

## Getting Started
```
vagrant up
vagrant ssh
cd /vagrant/datalogy
pip install -r requirements.txt
bower install
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8000
```
Visit [http://localhost:8000](http://localhost:8000)
