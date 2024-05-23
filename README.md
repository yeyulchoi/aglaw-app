# aglaw-app
# This is for our clients to be able to keep tract of their transactions and see 
# what is outstanding to close the deal and when to expect to sign the documents.


# postgresql connection.
# Create db in postgresql using cmd
#    in postgreSQL\16\bin >psql -U postgres/ prompt for pw.
#     \ls  - showing entire db
#   To create new db: command: CREATE DATABASE aglaw_db;
# The error : UTC is not set in DB.
# - solution: set 'UTC' to timezone in postgresql.confi
#  -settings.py: MUST-DO: USE_TZ = False , not True!!  This is KEY...

# pip install psycopg2-binary (dont have to use degraded version as said on internet)
# and then python manage.py createsuperuser.
#         where you set up username/email/pw to create superuser.
# and then python manage.py makemigrations
# and then python manage.py migrate
# and python manage.py runserver.
