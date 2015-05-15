## We Vote Base

Need to work with US ballot or election related data? In this Python-Django project, we import election related data from a variety of sources, merge it, and provide models to work with this data. We Vote Education (the sponsor of this project) is a nonprofit applying for 501(c)(3) status. We would like to empower more civic hackers by providing a living guide to working with election related data.

### Overview

We are currently taking in ballot data from:

* Google Civic API
* TheUnitedStates.io

We will be importing data from many sources, including:

* MapLight.com (Voter's Edge)
* VoteSmart.org
* The Sunlight Foundation's Open Civic Data project
* Azavea's Cicero API
* Twitter
* Facebook
* See http://www.ElectionDataSummary.org for links to a variety of election data sources we are exploring, as well as by joining our Google Group: https://groups.google.com/forum/#!forum/electiondata

Our approach is to write importers that take data from these sources into a local database, and then merge that data into a We Vote database structure so we can deliver a complete ballot to any American voter. Please reach out to us if you would like to help: http://www.wevoteeducation.org/#contact-us

### Setup - Dependencies

Once you have cloned this repository to your local machine, set up a virtual environment:

```bash
cd /path_to_dev_environment/wevotebase/
virtualenv venv
source venv/bin/activate
```

Now that your virtualenv is running:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Setup - Configuration

Change your local database configuration settings in (Search for "DATABASES") if you so desire:

wevotebase/settings.py

Add to your local environment the following if you are going to connect to Google Civic API:

```bash
export GOOGLE_CIVIC_API_KEY=<YOUR KEY HERE>
```

### Import Test Data

Start up the webserver:

```bash
python manage.py runserver
```

Visit the site here: http://localhost:8000/

Click on the "Import Tools" link, and import all data under Step 1. Transfer data to the We Vote tables under Step 2.

Now go back to the root http://localhost:8000/ and click on the "My Ballot" link. You should be taken to a San Francisco ballot.
