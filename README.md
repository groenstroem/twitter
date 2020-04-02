# Grøn strøm Twitter bot

This repository contains the code for the Twitter bot posting automatic updates
on the Danish emission intensities, currently live as [@co2prognoser](https://twitter.com/co2prognoser).


## Configuration

To use this, get a consumer key and consumer secret from https://dev.twitter.com/. With that,
allow the app to post as a given user by authenticating with the app as that user; the simplest way
to do this is using `twitter.oauth_dance`, cf. [the documentation](https://pypi.org/project/twitter/).

## Running

With these at hand, fill out `config.json.example` and move the result to `config.json`.

Then, to create a Twitter update with the current emission intensities, get all dependencies and run the only
available script,

```
pip install requests twitter
python tweet.py
``` 

## Docker

Alternatively, use Docker, specifying all configuration parameters as environment variables,

```
docker build -t groenstroem-twitter .
docker run -e OAUTH_TOKEN=... -e OAUTH_SECRET=... -e CONSUMER_KEY=... -e CONSUMER_SECRET=... groenstroem-twitter 
``` 
