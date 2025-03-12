# URL-Shortener
An URL Shortener made with Python and FastAPI. It uses sqlite3 as it's database.

## Installation
You can choose between 3 methods.

### Method 1: With the FastAPI Run command.
This is the method how you can manually run the program.

1. Clone this repository.
```gh repo clone AlybitDev/URL-Shortener```
2. Go into the repository and install the needed Python libraries.
```
cd URL-Shortener
pip install -r requirements.txt
```
3. Change example.com in templates/urlshortened.html to your own Domain or IP.
In This [file](https://github.com/AlybitDev/URL-Shortener/blob/main/templates/urlshortened.html).
4. Run the FastAPI Run command.
```
fastapi run main.py --host 0.0.0.0 --port 4650
```
5. Access the WebUI on port 4650.

### Method 2: With Docker.
This is the method how you can run URL-Shortener in a Docker Container with the Docker Run command.

1. Clone this repository.
```gh repo clone AlybitDev/URL-Shortener```
2. Go into the repository and change example.com in templates/urlshortened.html to your own Domain or IP.
```cd URL-Shortened```
In this [file](https://github.com/AlybitDev/URL-Shortener/blob/main/templates/urlshortened.html).
3. Build the Docker Image and Run the Docker Container with the Docker Run command.
```docker build -t URL-Shortener . && sudo docker run -d --name URL-Shortener -p 4650:4650 --restart always URL-Shortener```
4. Now you can access the WebUI on port 4650.

### Method 3: With Docker Compose.
This is the method how you can run URL-Shortener in a Docker Container with the Docker-Compose command.

1. Clone this repository.
```gh repo clone AlybitDev/URL-Shortener```
2. Change example.com in templates/urlshortened.html to your own Domain or IP.
```cd URL-Shortened```
In this [file](https://github.com/AlybitDev/URL-Shortener/blob/main/templates/urlshortened.html).
3. Run the Docker Container with the Docker-Compose command.
```docker-compose up -d```
4. Now you can access the WebUI on port 4650.
