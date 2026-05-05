# FLASK-WEB-APP

This is my simple Flask web app. Stores input data in MongoDB. Learning to create and deploy a "Dockerfile" which contains: mongo-express container, mongodb container and flask web application. 

Short explanation how i did things:
Created Flask web app, which makes connection to MongoDB
Created index.html file which is attached to FLASK web app file. "server.py"
Created Dockerfile, which pulls docker image from python, installs requirments.txt(flask, pymongo) and creates an docker image of Flask app.
Used Amazon ECR to push the docker image to ECR.
Created mongo.yaml file, which pulls 3 docker images: Flask web app, mongo-express, mongoDB. It compiles all 3 docker images into 1 image and releases 3 containers from it.
Flask web app, mongo-express, mongodb.
Then run docker-compose -f mongo.yaml up to setup all containers and they speak to each other.
To test things out, use localhost:5001
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
To be added
```

## Usage

```python
To be added
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

What kind of license is necessary for this?
