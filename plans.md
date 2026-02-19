  {
    "border": "jordan",
    "zone": "zone-10",
    "timestamp": "2026-02-15T23:32:58.011404",
    "people_count": 2,
    "weapons_count": 0,
    "vehicle_type": "none",
    "distance_from_fence_m": 722,
    "visibility_quality": 0.67
  }


COMPONENT PRODUDER

    load data
        set PRIORITY
        enter into que based on priority
            Urgent/Normal
    INCLUDES -> CONSUMER
        pulls alerts based on PRIORITY
        saves then in the db 
        add INSERTION_TIME  

COMPONENT REDIS
    HANDLES priority order
