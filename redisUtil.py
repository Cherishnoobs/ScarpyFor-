import redis

class redisUtil(object):

    r = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
    
    @classmethod
    def get_state(cls):
        return cls.r is not None

    @classmethod
    def setredis(cls, url, key):
        if not cls.r.sismember(key, url):
            cls.r.sadd(key,url)

    @classmethod
    def exists(cls ,url, key):
        lst = cls.r.lrange(key, 0, -1)
        for a in lst:
            if a == url:
                return True
        return False

    @classmethod
    def add(cls, url, key):
        if not cls.exists(url, key):
            cls.r.rpush(key, url)
           
    
    @classmethod
    def remove(cls, url, key):
        if not cls.exists(url, key):
            cls.r.lrem(key, 0, url)        
    
    @classmethod
    def total(cls, key):
        return cls.r.llen(key)

