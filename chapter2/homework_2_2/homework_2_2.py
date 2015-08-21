import pymongo

connection = pymongo.MongoClient("mongodb://localhost")
db = connection.students
collection = db.grades

query = {'type': 'homework'}

docs = collection.find(query).sort([('student_id', pymongo.ASCENDING),('score', pymongo.DESCENDING)])

s_id = ''
for doc in docs:
    if doc['student_id'] == s_id:
        collection.delete_one({'_id': doc['_id']})
    s_id = doc['student_id']
