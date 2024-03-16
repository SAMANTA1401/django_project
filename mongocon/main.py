from mongdb_con import db
from mongocon.models import db_collection 

#RUN: python -m mongocon.main 
if __name__=='__main__':
    print("welcome to pymongo")
    dict = {'name':"harry",'marks':50}
    # db_collection.insert_one(dict)

    multidict = [
        {'_id' :1, 'name':'John','age':32},
        {'_id' :2,'name':'Peter','age':46}
    ]
    # db_collection.insert_many(multidict)

    one = db_collection.find_one({'name':'John'})
    print(one)
    allDocs = db_collection.find({'name':'John'})
    print(allDocs)
    allDocs = db_collection.find({'name':'John'},{'name':1,'_id':0})

    for item in allDocs:
        print(item)



    # /////////

    

# 