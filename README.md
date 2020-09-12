Buying Cheap
===========

## Installation

**NOTE**: For this to run properly you must have `docker` installed because of `postgres`. If you don't, please refer to [docker-docs](https://docs.docker.com).  If you don't fell familiar with docker, install `postgres` in your machine.

You can create a virtual environment and install the required packages with the following commands:

First, setup the postgres container with docker:

```bash
docker-compose up -d
```

Now create a virtual environment and install the required packages with the following commands:

```bash
    $ virtualenv env --python=python3.8     # Create a virtual environment called env
    $ source env/bin/activate               # Activate the environment
    (env) $ pip install -r requirements.txt # Install the required packages
```

Setup the database:

```bash
    (env) $ python3.8 manage.py makemigrations
    (env) $ python3.8 manage.py migrate
```

Last, but not least, run the server:

```bash
    (env) $ python3.8 manage.py runserver
```

The server will be available at `http://127.0.0.1:8000`

### First Acess
Open django shell window in project root (active virtual environment) and run this commands:

```bash
    (env) $ python3.8 manage.py shell
    In [1]: from main.tasks.register_stores import register
    In [1]: register()
```

### Update Prices
For a while, to update all prices of your products, run this commands:
```bash
    (env) $ python3.8 manage.py shell
    In [1]: from main.tasks.update_prices import task_update_all_prices
    In [1]: task_update_all_prices()
```



### Docker compose error
You may get the following error when running the compose command:
```bash
ERROR: Version in "./docker-compose.yml" is unsupported. You might be seeing this error because you're using the wrong Compose file version. Either specify a supported version (e.g "2.2" or "3.3") and place your service definitions under the `services` key, or omit the `version` key and place your service definitions at the root of the file to use version 1.
For more on the Compose file format versions, see https://docs.docker.com/compose/compose-file/
```

If so, please refer to the compose install link: https://docs.docker.com/compose/install/

