from math import e
from pymongo import MongoClient

dsn = 'mongodb://localhost'
client = MongoClient(dsn)

db = client.dma

lst = 

where = {} #1 to show, 0 to supress in query
select_list = {"Business Title" = 1, "Salary" = 1, "id_" = 0}

#decreasing order
order_by = {"Salary Range to": -1}

res = db.jobs.find(where, select_list).sort(order_by).limit(50)

res = db.jobs.aggregate([{"title": "$Business Title"}])
OR 

res = db.jobs.aggregate([{"$project": {"Business Title": 1} }])
'$match' '$gt' '$project'