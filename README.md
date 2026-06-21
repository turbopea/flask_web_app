# FLASK-WEB-APP

This is my simple Flask web app. It holds my Curriculum Vitae for Juniour DevOps role. It is being hosted on EC2 instance on flask server.
Built with Python (Flask), containerized with Docker, and deployed on an
AWS EC2 instance. The Docker image is stored in Amazon ECR.


The site is a single page (`index.html`) styled with hand-written CSS,
served by Flask. It started as a multi-container project (Flask +
MongoDB + mongo-express) to practice Docker Compose and database
integration; it has since been simplified to a static CV with no
database, since storage wasn't needed for a CV site.
## Technologies
- Python 3 / Flask
- Docker
- Amazon ECR (image registry)
- AWS EC2 (hosting)

## Usage

**Run locally:**
```bash
python server.py
```
Then open `http://localhost:5001` in your browser.
**Run with Docker:**
```bash
docker build -t flask-cv .
docker run -p 80:5001 flask-cv
```
Then open `http://localhost:5001`.
## License
MIT LICENSE
