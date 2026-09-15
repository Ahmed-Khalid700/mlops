from fastapi import FastAPI
import uvicorn
import redis
import time

app = FastAPI()

cache = redis.Redis(host="redis", port=6379)

def get_count():
    retries = 5
    
    while True:
        try:
            return cache.incr("hits")
        except Exception as exc:
            if retries == 0:
                return exc
            
            retries -= 1
            time.sleep(0.5)
                

@app.get("/")
def hello():
    count = get_count()
    return {"message": f"You have visited me {count}"}    