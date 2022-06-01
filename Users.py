from spyMonk.spyMonkDB import spyMonkDB, Query
import random
import time
from faker import Faker

db = spyMonkDB(connection="users.json")
User = Query(db)

start = time.time()
# insert random faker data
for x in range(101):
    db.insert({
        "name": "Shubhajeet",
        "age": "21",
        "fav_letter": int(random.random())
    })

print(round(time.time() - start, 4))

# insert - no mmap - 100 insert - 0.0988 secs
# insert - no mmap - 1000 insert - 9.0446 secs
