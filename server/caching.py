from redis import Redis
import redis

# dev
# r = redis.from_url('redis://localhost:6380/1')

# prod
r = Redis(host='redis', port=6379)
