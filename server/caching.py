from redis import Redis
import redis
import os
import json

# dev
# r = redis.from_url('redis://localhost:6380/1')

# prod
# r = Redis(host='redis', port=6379)
with open('config.json', 'r') as f:
    uri = json.load(f)['heroku']

r = redis.from_url(uri)
