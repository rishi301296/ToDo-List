# ToDo-List
ToDo List integration for Slack's Slash commands

The webapp is hosted on heroku
the domain for this webapp is http://rishi-webapp.heroku.com

This webapp contains three apis, namely
- https://rishi-webapp.heroku.com/api/task-add/
- https://rishi-webapp.heroku.com/api/task-list/
- https://rishi-webapp.heroku.com/api/task-remove/

These three apis are integrated with three slash commands of slack

/addtodo  ->  https://rishi-webapp.heroku.com/api/task-add/
/listtodo  ->  https://rishi-webapp.heroku.com/api/task-list/
/marktodo  ->  https://rishi-webapp.heroku.com/api/task-remove/

To run the project:-

1. Fork the repo.
2. Clone and download it.
3. Install Python, version=3.5.2
4. Run the command 
-> pip install virtualenv
-> cd ~/../project-directory
-> virtualenv .
-> source ../bin/activate (for MacOS and Linux)
-> pip install -r requirements.txt
-> python manage.py migrate
-> python manage.py runserver 8000

Now the following 3 urls can be accessed using localhost:8000 domain
