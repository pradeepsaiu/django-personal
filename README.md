# Django-Skelton-Structure
Skelton for displaying projects

How to Navigate through Django App.

1. Install Virtualenv (pip install virtualenv)
  1.1 Open virtualenv (virtualenv name)
  1.2 Install prerequisites (pip install -r requirements.txt) => installs all requirements in particular virtual env.

2. Try running the app.
  2.1 running app (python manage.py runserver)
  2.2 open url to check how the current app looks.

3. Modifying the CSS
  3.1 Navigate to the app(www), and open static folder where all CSS files are present.
  3.2 Modify changes and check the url to see how changes effect.
  
5. Database
  5.1 Models are the database for django, need to create classes (equal to table)
  5.2 Update attributes (equivalent to columns of table)
  
4. Adding to Database
  4.1 This can be achieved in 3 ways
      4.1.1 GUI (fastest way if only one file is present)
      4.1.2 Python Shell (to work with command line)
      4.1.3 JSON file (best approach when large content of file is present)
        4.1.3.1 Save file according to model and in required format (refer sample json in fixtures)
        4.1.3.2 use loaddata filename
        
5. Updating Database
  5.1 All database changes have to be commited ( python manage.py makemigrations, python manage.py migrate)
  
6. Deploy to heroku (...)
