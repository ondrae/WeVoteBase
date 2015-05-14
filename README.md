## We Vote Base

Need to work with US ballot or election related data? In this Python-Django project, we import election related data from a variety of sources, merge it, and provide models to work with this data.

### Overview

We are currently taking in ballot data from:

* Google Civic API
* TheUnitedStates.io

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

Start up the webserver:

```bash
python manage.py runserver
```

### Setup - Configuration

Change your local database configuration settings in (Search for "DATABASES"):

wevotebase/settings.py

