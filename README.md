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
