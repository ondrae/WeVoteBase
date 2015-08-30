## We Vote Base

Need to work with US ballot or election related data? In this Python-Django project, we import election related data from a variety of sources, merge it, and provide models to work with this data. We Vote Education (the sponsor of this project) is a nonprofit applying for 501(c)(3) status. We would like to empower more civic hackers by providing a living guide to working with election related data.

### Overview

We are currently taking in ballot data from:

* Google Civic API
* TheUnitedStates.io

We will be importing data from many sources, including:

* Ballot API: https://github.com/sfbrigade/ballotapi
* SF Base Election Data (SFBED): https://github.com/cjerdonek/sf-base-election-data
* MapLight.com (Voter's Edge)
* VoteSmart.org
* The Sunlight Foundation's Open Civic Data project
* Azavea's Cicero API, for identifying the voting districts any voter is in, so we know what ballot data to display. See: http://www.azavea.com/products/cicero/
* Catalist.us, for access to 270+ Million Voter Files
* Nationbuilder.com, for access to Voter Files
* Twitter
* Facebook
* See http://www.ElectionDataSummary.org for links to a variety of election data sources we are exploring
* [MaxMind GeoIP](https://www.maxmind.com/en/home)

Our approach is to write importers that take data from these sources into a local database, and then merge that data into a We Vote database structure so we can deliver a complete ballot to any American voter.

### Live Demo

You can see our current wireframe mockup for a San Francisco ballot here:
http://my.wevoteusa.org/

### Join Us - Contributing to We Vote Base
Please reach out to us if you would like to help or have any questions:
http://www.wevoteeducation.org/#contact-us

To see what we are currently working on, see our Pivotal tracker:
https://www.pivotaltracker.com/n/projects/1346856

Join our Google Group here to discuss the We Vote Base application (creating a social ballot):
https://groups.google.com/forum/#!forum/wevoteengineering

You may join our Google Group here for questions about election related data (importing and exporting):
https://groups.google.com/forum/#!forum/electiondata

### Setup - Dependencies

NOTE: We are running Django version 1.8
NOTE: We are running Python version 2.7.6

Once you have cloned this repository to your local machine, set up a virtual environment:

    cd /path_to_dev_environment/wevotebase/
    virtualenv venv
    source venv/bin/activate

We recommend running this within your virtual environment:

    pip install django-toolbelt
    pip install --upgrade pip
    pip install -r requirements.txt


### Setup - Install the Postgres database

#### METHOD 1
For Mac, download the DMG from http://postgresapp.com/

Run this on your command line:

    export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.4/bin

Start up the command line for postgres (there is an 'open psql' button/navigation item if you installed postgresapp.
Run these commands:

    create role postgres;
    alter role postgres with login;

#### METHOD 2

Install Postgres:

    $ sudo port install postgresql94
    $ sudo port install postgresql94-server

Next, follow these instructions:

    http://gknauth.blogspot.com/2014/01/postgresql-93-setup-after-initial.html

#### FINALLY

We also recommend installing pgAdmin3 as a WYSIWYG database administration tool.
NOTE: You may need to turn off the restriction in "Security & Privacy" on "unidentified developers"
to allow this tool to be installed.
See: http://blog.tcs.de/program-cant-be-opened-because-it-is-from-an-unidentified-developer/

In pgadmin add a server. You can use your sign in name as the server name.


### Setup - Environment Variables Configuration - wevotebase/environment_variables.json

WeVoteBase is currently configured (in manage.py) to look for a "wevotebase/local.py" file (configured in the
"wevotebase/settings.py" file). When we run this on a production server, we will startup with a production settings
file like "production_heroku.py".

Copy "environment_variables-template.json" to "environment_variables.json". You will configure many variables for your
local environment in this file. New variables needed by WeVoteBase will be added to
"environment_variables-template.json" from time to time, so please check for updates by comparing your local version
with the template file.

#### LOG_FILE
Create a file on your computer to match the one expected in the environment_variables.json file:

    sudo mkdir /var/log/wevote/
    sudo touch /var/log/wevote/wevote.log
    sudo chmod -R 0777 /var/log/wevote/

As configured in github, only errors get written to the log.
Logging has five levels: CRITICAL, ERROR, INFO, WARN, DEBUG.
It works as a hierarchy (i.e. INFO picks up all messages logged as INFO, ERROR and CRITICAL), and when logging we
specify the level assigned to each message. You can change this to info items by changing this:

    LOG_FILE_LEVEL = logging.INFO

#### GOOGLE_CIVIC_API_KEY
If you are going to connect to Google Civic API, add your key to this variable.
TODO: Describe the process of getting a Google Civic API Key


### Setup - Database Creation

If you would like to match the local database settings from the "wevotebase/environment_variables.json" file,
(Search for "DATABASES"):

    createdb WeVoteDB

Populate your database with the latest database tables:

    python manage.py makemigrations
    python manage.py migrate

Create the initial database:

    $ python manage.py syncdb

When prompted for a super user, enter your email address and a simple password. This admin account is only used in development.

If you are not prompted to create a superuser, run the following command:

    python manage.py createsuperuser

    Import GeoIP data:

        $ python manage.py update_geoip_data

### Setup - Heroku Configuration

We use Heroku for publishing a public version anyone can play with (see "Live Demo" above), and you can publish a public version too. Here are the instructions:
https://devcenter.heroku.com/articles/getting-started-with-django

In the wevotebase/setting.py file, search for "Heroku". There are comments that tell you which parts of the settings file to comment or uncomment to get a version running on Heroku.

### Import Test Data

Start up the webserver:

    python manage.py runserver

Open your browser to login to the admin account so you can have access to the import_export tools:

    http://localhost:8000/admin/login/?next=/admin/

Visit the site here:

    http://localhost:8000/import_export/

Click all the import links, going from top to bottom.

Now go back to the root and you should be taken to a San Francisco ballot.

     http://localhost:8000/

### Coding Standards

Please use descriptive full word variable names.

* In the lifecycle of most projects, fixing bugs and maintaining current features end up taking 50%+ of total engineering time.
* Our goal is to create a code base that is easy to understand, making fixing bugs and maintaining current features as painless as possible. We will have many engineers working with this code, and we want to be welcoming to engineers who are new to the project.
* Short variable names can often create confusion, where a new engineer needs to spend time figuring out what a short variable name actually means. (Ex/ “per” or “p” instead of “person”.) For this project please use descriptive full word variable names.
* Fellow engineers should be able to zoom around the code and not get stopped with riddles created by short names.
