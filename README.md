# Vibrato Technical Assessment

## To run

```bash
$ docker-compose up -d
$ curl http://localhost:5000
$ docker-compose down
```

## Design decisions

* Using Flask for Python to serve simple http requests, it's the quickest way to get a web response up and running.
* Using Docker to containerise the python app. It's a super reliable and straightforward way to bundle an app up into a discrete unit.
* Using Alpine Linux as the base image for the app as it's stable and tiny.
* Using Docker Compose to tie the Docker containers together. It's the most straightforward thing to setup on your dev machine. The app is static so there's no need to mount a volume, generally I try to 12-factor web apps and avoid the need for mounting a volume by pushing files that are large or do change to an s3 bucket or similar.
* Using Redis as all I need is a key-value store, no schema necessary. I'm also using Alpine Linux as the OS for the Redis image for the same reasons, it's stable and tiny.
