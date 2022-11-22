# Liine Take Home
Code assessment

## Technologies used
- Python 3.10
- Docker
- GitHub

## To run on local machine
1. Have Docker up and running.
2. Clone this repository
3. If on windows ( use WSL )
4. Run these commands:

```bash
docker build -t liine-project:latest .
```

```bash
docker run -it -d -p 8080:8080 liine-project
```

## Navigation on Flask site.
The home page references the url and structure to run access the API.
Navigate to : http://127.0.0.1:8080/restaurants/date/2022-11-22 13:00:00/

Please note:
- There is a space between the date and the time.
- The the restaurants.py is json version of the csv provided.#   l i i n e - t a k e - h o m e  
 