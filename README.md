# Overview

ModelDB is a computational neuroscience resource seeking to facilitate discovery of modeling work, analyses of the work, and meta-analyses of the relationship between models.

This is the development repository for the redesign of ModelDB intended to be launched in summer 2020.

Primary goals of this redesign include:

- Facilitating analysis: with built-in tools and easier data querying.
- Improved community engagement: using standard technologies and ontologies to make it easier for others to contribute and for us to interoperate with the broader neuroinformatics community.
- Support on more devices: the resource should be useful to people on mobile devices, desktops, and anything in between.

**Pull requests are welcome. Please make an issue first so we understand the problem solved or feature being added by the pull request.**

## Bootstrapping system and data
This repository is currently intended to be bootstrapped from the classic EAV/CR version of ModelDB. One approach to do so follows:

- Download the [bitnami django stack OVA][1]
- Import it into a virtual machine such as [VirtualBox][2]
- Install the community edition of MongoDB following [these directions][3]
  - note: if you're using Amazon lightsail instead, you'll need to switch to the instructions for Ubuntu. At this writing it's using Ubuntu 16.04.
- Create a MongoDB account with readwrite access to a specific database (for simplicity, you may want to call it `modeldb`)
  - launch MongoDB by typing `mongo`
  - switch to the database you want to use e.g. `use modeldb`
  - create the user:
  
        db.createUser({
            user: "username",
            pwd: "password",
            roles: [{role: "userAdmin", db:"modeldb"}]})
            
- Install git so you can clone this repository, if it's not already installed `sudo apt install git`
- Clone this repository
- Install Python dependencies (`sudo pip3 install -r requirements.txt`)
- Create four directories for storing (1) the model zip files, (2) private model zip files, (3) unprocessed references, (4) modelview data.
- Create a settings file in the exact path `/home/bitnami/modeldb-settings.json`. It should have values for:
  - `secret_key` (I'm unclear on if there are any rules on this, but I guess a random 50 character string should work)
  - `mongodb_user`
  - `mongodb_pw`
  - `db_name` -- set this to `modeldb` or whatever you called the database you wish to use.
  - `modeldb_zip_dir` 
  - `modeldb_private_zip_dir`
  - `unprocessed_refs_dir`
  - `modelview_dir`
  - `metadata-predictor-rules` (points to a file with predictor rules; you can use the one in `resources`)
  - `smtp_server` (optional, but required for sending mail)
  - `smtp_user` (optional, but required for sending mail)
  - `smtp_password` (optional, but required for sending mail)
- Run the scripts in the `extract_data` directory in this order:
  - `init_db.py`
  - `extract_data.py`
    - note: there are a large number of data items (especially papers). This will take a while.
  - `get-zips.py`
  - `setup_cell_links.py`
  - `setup_trees.py`
  - `get_icg_mapping.py`
  - `get_file_hashes.py`
    - this generates the file reuse detection data
  - `sync_neuron_dict.py`
    - this updates the neurons included in celltypes
- Apply the django migrations
  `python3 manage.py migrate`
- You will also want to use django admin to create a user with admin permissions from within the
  shell you get via `python3 manage.py shell`.
  Example from: https://docs.djangoproject.com/en/3.0/topics/auth/default/#creating-users
  ```python
  from django.contrib.auth.models import User
  user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  ```
- Pull links to biosimulations: `python3 pull_biosimulations.py` (in the `extract_data` folder). The website will still work without this, you just won't get any links to biosimulations.org
- Insert static links to Open Source Brain: `python3 pull_opensourcebrain.py` (in the `extract_data` folder)
- You can run a development server via, e.g. `python3 manage.py runserver 8888`
  - This will make the website available on port 8888 (you can then access it from your host system via port-forwarding.
  - This is separate from apache, which is also running and can later be connected to your django system.

## On the pipeline
- This requires some files copied over from https://github.com/mcdougallab/pipeline
  - cp pipeline/Project/pipeline_* ~/apps/django/django_projects/Project/Project/
  - cp -r pipeline/Project/templates/pipeline/ ~/apps/django/django_projects/Project/Project/templates/
- Also, note the authentication will need to be setup to use the different database

## Deployment hints
- If you're deploying on bitnami's django stack, see their instructions at: https://docs.bitnami.com/virtual-machine/infrastructure/django/get-started/deploy-django-project/
- be sure to turn off debugging in the settings file
- the sqlite3 database needs to be writeable and it needs to be in a folder that's writeable (so not in a path that hosts the website code)
  (e.g. you might put it in /home/bitnami/db/ and modify settings.py accordingly)
- make sure the folders with private-zips and unprocessed refs can be written to by the server
- if you make any changes on a bitnami machine with apache setup; run `sudo /opt/bitnami/ctlscript.sh restart apache` to restart
- wsgi.py needs the correct name of the settings module... e.g. if you put it in `Project` instead of `modeldb2020`, you should
  change `modeldb2020.settings` to `Project.settings`
 - the settings file may need the full path to `TEMPLATES["DIRS"]`

## on Analysis
The `analysis` folder contains scripts for analyzing ModelDB in ways that may
or may not be supported in the web interface. It includes:
- `metadata_repeat_list.py` -- provides a list of all used metadata; combine with a free word-cloud generator to visualize

## On ModelViews

You can gather a morphology suitable for frontpage display via

    result = []

    for sec in h.allsec():
        xs = [sec.x3d(i) for i in range(sec.n3d())]
        ys = [sec.y3d(i) for i in range(sec.n3d())]
        zs = [sec.z3d(i) for i in range(sec.n3d())]
        ds = [sec.diam3d(i) for i in range(sec.n3d())]
        arcs = [sec.arc3d(i) for i in range(sec.n3d())]
        result.append([xs, ys, zs, ds, arcs])

but note that in order to color by segment, you need each piece of result to correspond
to a segment instead of to a section.

## Technologies

The ModelDB website is powered in part by a number of other technologies, including:

### Backend
- [python](https://python.org)
- [django](https://www.djangoproject.com/)
- [mongodb](https://mongodb.com)
- [pymongo](https://pypi.org/project/pymongo/)
- [bitnami django stack][1]

### Frontend
- [jQuery](https://jquery.com)
- [jQuery UI](https://jqueryui.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com)
- [plotly](https://plotly.com)
- [select2](https://select2.org/)
- [popper](https://popper.js.org)
- [Bootstrap Table](https://bootstrap-table.com/)

Did we miss something from this list? Submit a pull request!

[1]: https://bitnami.com/stack/django/virtual-machine "Bitnami django OVA"
[2]: https://www.virtualbox.org/ "VirtualBox"
[3]: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/ "MongoDB installation guide"
