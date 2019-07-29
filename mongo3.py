from pymongo import MongoClient
import pprint

client = MongoClient()
# db = client['test-database']
# post = {"author": "Mike",
#         "text": "My first blog post!",
#         "tags": ["mongodb", "python", "pymongo"] }
#
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
#
# print post_id
#
#
# pprint.pprint(posts.find_one())

db = client['info']
print db.collection_names()
collection = db.users
mas_collection_names=db.collection_names()
for i in range(len(mas_collection_names)):
   print mas_collection_names[i]
# print str(collection.find_one())

# for post in collection.find():
#    print  post

# pprint.pprint(collection.find_one())

# collection.save({"languages":['russian','english'],'age':25.0,"name":"Vadim",'_id': '5d39a093993c4e574e99a6d1'})
# collection.update({"name": "Vadim"}, {"age": 25.0})
# collection.update({"name": "Vadim"}, {"surname":"Kim"})
# collection.remove({'age':27.0})

post_str=[]


# for post in collection.find({"name": "Vadim"}):
#    post_str.append(str(post))
#    print  post_str['name']

for post in collection.find():


   post_name = post['name']
   post_age = post['age']
   # post_str.append('name : %8s age  %s ' % (str(post_name),str(post_age)))
   post_str.append('name : {0:<6} age : {1:0<5}'.format(str(post_name), str(post_age)))

for i in post_str:
   print i