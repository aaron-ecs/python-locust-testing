# python-locust-testing
A simple load testing framework written in Python using Locust library.

Please note this example simply runs some dummy tests within a docker container.

## Setup
It's recommended you run a Python Virtual Environment in Python 3.7.2 or higher.

For local development please install locustio: `python3 -m pip install locustio`

## Testing
To save you from having to install Python and the dependencies you can run the tests by building the docker image
run `docker build . -t aaronmwilliams/python-locust-testing` in the project root then `docker-compose up` this will also spin up a the API service docker container.

If you want to run the tests locally please checkout and run the API webservice: https://bitbucket.org/aaronmwilliams/user-exercises-rest/src/master/ then run on the of the commands below:

With UI: `locust --host=http://localhost:8080`

No UI: `locust --host=http://localhost:8080 --no-web -c 100000 -r 1000 --run-time 1m`


## Reporting
HTTP Response times are printed in the console.

## Linting
Please ensure you have the `pylint` plugin installed and running on your IDE.

## CI
If the Travis file is used it will build the docker image and then run `docker-compose up --exit-code-from tests` which kicks off the tests.

## To-Do
- Add more tests and abstract general logic and 
- ~~Add to Jenkins~~
- Better test reports