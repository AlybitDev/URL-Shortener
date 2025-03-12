# URL-Shortener
An URL Shortener made with Python and FastAPI. It uses sqlite3 as it's database.

## Installation
You can choose between two methods.

### Method 1: With the FastAPI Run command.
This is the method how you can manually run the program.

1. Clone this repository.
```gh repo clone AlybitDev/URL-Shortener```
2. Go into the repository and install the needed Python libraries.
```
cd URL-Shortener
pip install -r requirements.txt
```
4. Run the FastAPI Run command.
```
fastapi run main.py --host 0.0.0.0 --port 4650
```
5. Access the WebUI on port 4650.

### Method 2: With Docker.
This is the method how you can run URL-Shortener in a Docker Container with the Docker Run command.

1. Clone this repository.
```gh repo clone AlybitDev/URL-Shortener```
2. Go into the repository, build the Docker Image and Run the Docker Container with the Docker Run command.
```
cd URL-Shortener
docker build -t urlalybitdev . && sudo docker run -d --name URL_Shortener -p 4650:4650 --restart always urlalybitdev
```
3. Now you can access the WebUI on port 4650.

### Method 3: With Docker Compose.
This is the method how you can run URL-Shortener in a Docker Container with the Docker-Compose command.

1. Clone this repository.
```gh repo clone AlybitDev/URL-Shortener```
2. Go into the repository and run the Docker Container with the Docker-Compose command.
```
cd URL-Shortener
docker-compose up -d
```
3. Now you can access the WebUI on port 4650.
