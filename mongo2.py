from pymongo import MongoClient
client = MongoClient()
col = client.mydb.test
result = col.insert_one({'x':1})
print result.inserted_id
result = col.insert_many([{'x': 2}, {'x': 3}])
print result.inserted_ids
result = col.replace_one({'x': 1}, {'y': 1})
print result.matched_count
print  result.modified_count

print result

