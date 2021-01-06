# Installation

## Requirements:

1. Python 3.6+ (Change the Pipenv file for used version)
2. Internet connection
3. Pipenv (commabd: `pip install pipenv`)

## Create VirtuelEnv for the Project:

`cd <dir>`
`pipenv shell`

## Downloading Dependencies:

`pipenv install`

## Set Environment Variables:

The app uses username & password, taken from environment variables. so in order to configure:
Copy the "example.env" to new ".env", and set the values to the variables inside.

# Run Server

`pipenv run uvicorn server:app --host 0.0.0.0 --port 80`

# Docker Image

## Build Image

example tag: "matzov-ctf/website:1.0"
`docker build -t <image_tag> .`

## Run Container from Image

`docker run -p <local_port>:80 --name <container_name> <image_tag>`
