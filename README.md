# page-visitor-counter
Build app docker image:

`docker build -t app:v0.1 .`

Run the app with redis host passed in as environment variable `REDIS_HOST`

`docker run -d --rm --name app -p 80:80 -e REDIS_HOST=YOUR_REDIS_HOST app:v0.1`