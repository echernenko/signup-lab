import json
import os
import threading
from collections import defaultdict
from threading import Lock

import uvicorn
from fastapi import FastAPI
from confluent_kafka import Consumer

app = FastAPI()
aggregation: dict[str, int] = defaultdict(int)
lock = Lock()


def consume():
    consumer = Consumer({
        "bootstrap.servers": os.environ["KAFKA_BOOTSTRAP_SERVERS"],
        "group.id": "signup-workers",
        "auto.offset.reset": "earliest",
        "enable.auto.commit": False,
    })
    consumer.subscribe(["signups"])
    while True:
        msg = consumer.poll(1.0)
        if msg is None or msg.error():
            continue
        event = json.loads(msg.value())
        with lock:
            aggregation[event["date"]] += 1
        consumer.commit(msg)


@app.get("/aggregation")
def get_aggregation():
    with lock:
        return dict(aggregation)


if __name__ == "__main__":
    threading.Thread(target=consume, daemon=True).start()
    uvicorn.run(app, host="0.0.0.0", port=8001)
