from redis import Redis
import redis
import os

# dev
# r = redis.from_url('redis://localhost:6380/1')

# prod
# r = Redis(host='redis', port=6379)
r = redis.from_url(os.environ['REDISCLOUD_URL'])
