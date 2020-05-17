from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import redis

import os

app = FastAPI()

db = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))

@app.get("/", response_class=HTMLResponse)
def read_root():
    page_visit_count = db.incr('pagevisitcount', amount=1)
    html = "<h1>This is the {visits} visitor</h1>" 
    return html.format(visits=page_visit_count)