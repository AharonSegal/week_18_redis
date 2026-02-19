"""
Consumer - continuously listening to both redis queues 
         - fetching by priority 
         - add "insertion_time" field
         - save in mongo

INPUT:
    - alerts from redis based on queue

OUTPUT:
    - saves to mongo

FLOW:
    alert from redis -> add "insertion_time" field -> saves to mongo
"""

import json
import time
from datetime import datetime, timezone
from redis_connection import r
from mongo_connection import mongo

QUEUE_URGENT = "queue_urgent"
QUEUE_NORMAL = "queue_normal"

collection = mongo.collection("alerts")


def process():
    print("consumer running...")
    while True:
        # try urgent queue first
        message = r.lpop(QUEUE_URGENT)

        # if no urgent, try normal queue
        if message is None:
            message = r.lpop(QUEUE_NORMAL)

        # if both queues empty stop for 5 seconds
        if message is None:
            time.sleep(5.0)
            continue

        alert = json.loads(message)

        # add insertion time before saving
        alert["insertion_time"] = datetime.now(timezone.utc).isoformat()

        # save to mongodb - _id is auto generated
        collection.insert_one(alert)

        print(f"saved alert: border={alert['border']}, zone={alert['zone']}, priority={alert['priority']}")


process()