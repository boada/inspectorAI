# Inspector AI

Inspector AI is a tool that helps New York City health inspectors prioritize their inspections based on a restaurant's past inspection history and the environment around the restaurant.

## Basic Pitch

Each year the CDC estimates that 1 in 6 Americans contract a food borne illness, all the while Americans continue to eat out at ever increasing rates. I am using the New York City restaurant health inspection histories to develop a framework which can aid in prioritizing the inspection order. As I’ll show, the NYC historical inspection data set paints an incomplete picture of a restaurant’s history and NYC can improve their serious violation detection using a more data driven approach.

## Installation

Requires:
* Python>=3.6
* pandas
* scikit-learn
* matplotlib

Optional:
* keras
* xgboost
* tqdm

Required for API:
* flask
* flask-restplus
* gunicorn

Use `requirements.txt` to install everything that you'll need to get going.

## Product

To enable these predictions to be rolled into NYC's existing workflow, I've created an API that provides restaurant violation probabilities given an inspection window. The API is written in flask with swaggerUI documentation and hosted on Amazon AWS EC2. There is a ton of functionality that could be added to the API, but right now it should be thought of as a proof-of-concept.

To make deployment to EC2 as easy as possible. I've created (borrowed from various places on the internet) a deployment script which can be copied to the EC2 instance and run to set everything up for you. Start your EC2 instance with Ubuntu and copy `deploy_backend.sh` to the instance. Run it (might need to modify permissions) and it should create a `launch.sh` and `terminate.sh` script which will launch and terminate the API. Access the API using the instance's public IP address and go to town.
