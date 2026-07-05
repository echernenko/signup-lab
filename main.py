from collections import defaultdict
from datetime import date
from threading import Lock

from fastapi import FastAPI

app = FastAPI()

# In-memory store: {date_str: count}. This is step 1 only — no Kafka, no DB yet.
aggregation: dict[str, int] = defaultdict(int)
lock = Lock()


@app.get("/signup")
def signup(country: str):
    today = date.today().isoformat()
    with lock:
        aggregation[today] += 1
    return {"status": "ok", "country": country, "date": today}


@app.get("/aggregation")
def get_aggregation():
    with lock:
        return dict(aggregation)
