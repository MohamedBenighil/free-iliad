# Example: python-web-app

This example sets up two servers one database and one webserver. The webserver instance runs a Python app and the database instance MariaDB. This deploy demonstrates use of files/template and splitting of tasks between different inventory groups. It looks like:

+ `inventories/docker.py` - inventory pointing at the Docker test containers
+ `deploy.py` - entrypoint/base package install
+ `tasks/database.py` - database server setup
+ `tasks/web.py` - webserver/Python app setup

```sh
# Start Docker containers
./docker-start.sh

# Run pyinfra against them
pyinfra inventories/docker.py deploy.py

# The app should now be accessible in browser on localhost:5000
# (the app is just a fork of a tutorial: https://github.com/Fizzadar/Flask-Web-App-Tutorial)

# Delete Docker containers
./docker-stop.sh
```
