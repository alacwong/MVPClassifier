from redis import Redis


# dev
# r = redis.from_url('redis://localhost:6380/1')
r = Redis(host='redis', port=6379)
