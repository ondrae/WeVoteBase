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

Our approach is to write importers that take data from these sources into a local database, and then merge that data into a We Vote database structure so we can deliver a complete ballot to any American voter. 

### Live Demo

You can see a live demo for a San Francisco ballot here: 
http://my.wevoteeducation.org/

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

NOTE: We are running Django version 1.7 and if you are running Django version 1.8 you will encounter problems with the current code base.
NOTE: We are running Python version 

Once you have cloned this repository to your local machine, set up a virtual environment:

    cd /path_to_dev_environment/wevotebase/
    virtualenv venv
    source venv/bin/activate

Now that your virtualenv is running:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Setup - Install the Postgres database

TODO: These Postgres installation instructions need to be verified.

Install Postgres: 

    $ sudo port install postgresql94
    $ sudo port install postgresql94-server

Next, follow these instructions:

    http://gknauth.blogspot.com/2014/01/postgresql-93-setup-after-initial.html

Create the initial database:

    $ python manage.py syncdb

When prompted for a super user, enter your email address and a simple password. This admin account is only used in development.

If you are not prompted to create a superuser, run the following command:

```bash
python manage.py createsuperuser
```

Run the server:

    $ python manage.py runserver

We also recommend installing pgAdmin3 as a WYSIWYG database administration tool.


### Setup - Local Configuration

Change your local database configuration settings in (Search for "DATABASES") if you so desire:

wevotebase/settings.py (Also see "Heroku Configuration" below)

```bash
createdb WeVoteDB
```

Populate your database with the latest database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

Add the following to your local environment if you are going to connect to Google Civic API:

```bash
export GOOGLE_CIVIC_API_KEY=<YOUR KEY HERE>
```

### Setup - Heroku Configuration

We use Heroku for publishing a public version anyone can play with (see "Live Demo" above), and you can publish a public version too. Here are the instructions: https://devcenter.heroku.com/articles/getting-started-with-django

In the wevotebase/setting.py file, search for "Heroku". There are comments that tell you which parts of the settings file to comment or uncomment to get a version running on Heroku.

### Import Test Data

Start up the webserver:

```bash
python manage.py runserver
```

Open your browser to login to the admin account:

    $ xdg-open http://localhost:8000/admin/login/?next=/admin/

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