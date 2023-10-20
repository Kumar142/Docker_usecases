This project is for counting the number of times any website will be visited.
To Run this command with docker compose: 

docker-compose up --build

If You want to make this with docker network concept:

steps:
(1) Create docker network: docker network create my_network
(2) To start the database in db containers: docker run -d --name db --network my_network -e POSTGRES_USER=your_username -e POSTGRES_DB=your_database -e POSTGRES_PASSWORD=your_password postgres
(3) build the python app image: docker build -t python_app . 
(3) To run a containers with python scripts: docker run -d --name python-app --network my_network -p 8000:8080  python_app



