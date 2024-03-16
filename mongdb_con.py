import pymongo
import gridfs

url =  "mongodb://localhost:27017"
client = pymongo.MongoClient(url)

db = client['demodb']

db_collection = db['democoll']

gfs = gridfs.GridFS(db, collection='democoll')