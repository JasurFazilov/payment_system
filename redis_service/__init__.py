import redis


redis_db = redis.from_url('redis://redis_db')


# redis_db.set('spam', 10)


data = redis_db.get('spam')
print(data)


# redis_db.set('spam2', 'hello', 5)
data2 = redis_db.get('spam2')
print(data2)