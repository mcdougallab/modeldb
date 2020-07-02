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
- Create a MongoDB account with readwrite access to a specific database (for simplicity, you may want to call it `modeldb`)
- Install pymongo (`sudo pip3 install pymongo`)
- Install git so you can clone this repository, if it's not already installed `sudo apt install git`
- Install bcrypt: `sudo pip3 install bcrypt`
- Clone this repository
- Create two directories for storing (1) the model zip files and (2) private model zip files
- Create a settings file in the exact path `/home/bitnami/modeldb-settings.json`. It should have values for:
  - `secret_key` (I'm unclear on if there are any rules on this, but I guess a random 50 character string should work)
  - `mongodb_user`
  - `mongodb_pw`
  - `db_name` -- set this to `modeldb` or whatever you called the database you wish to use.
  - `modeldb_zip_dir` 
  - `modeldb_private_zip_dir`
  - `unprocessed_refs_dir`
- Run the scripts in the `extract_data` directory in this order:
  - `init_db.py`
  - `extract_data.py`
    - note: there are a large number of data items (especially papers). This will take a while.
  - `get-zips.py`
  - `setup_cell_links.py`
  - `setup_trees.py`
- Apply the django migrations
  `python3 manage.py migrate`
- You will also want to use django admin to create a user with admin permissions.
- You can run a development server via, e.g. `python3 manage.py runserver 8888`
  - This will make the website available on port 8888 (you can then access it from your host system via port-forwarding.
  - This is separate from apache, which is also running and can later be connected to your django system.

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

Did we miss something from this list? Submit a pull request!

[1]: https://bitnami.com/stack/django/virtual-machine "Bitnami django OVA"
[2]: https://www.virtualbox.org/ "VirtualBox"
[3]: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/ "MongoDB installation guide"
