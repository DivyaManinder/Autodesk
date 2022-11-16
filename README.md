# adp-infra-takehome

# to build the docker image use the below command
docker build --tag python-docker-takehome

# to run the docker container use the below command
docker run -d -p 5000:5000 python-docker-takehome

# to run the tests change directory to the project directory and run the below command
python3 test_api.py

# run the below curl commands
curl http://localhost:5000

curl --header "Accept: application/json" http://localhost:5000


