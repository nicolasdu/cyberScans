# Cyber Scans

The service processes cyber scans in asynchronous behaviour 

# Prerequisites to run the project from you idea
    - python
    - redis db
    - celery worker

You can install the mentioned above by running the docker-compose.yml file in the project as follows: 
 
    docker-compose up

Then you can run the app locally from your idea.

# APIs 
    - ingest endpoint :  http://127.0.0.1:5000/scan
    - status endpoint :  http://127.0.0.1:5000/scan/<scan-id> // you get a scan id from the ingest endpoint


#Notes 

    - If you decide not to run to docker-compose file and run the prerequisites independently, you will need to install
    the tools mentioned in the requirements.txt file in the project