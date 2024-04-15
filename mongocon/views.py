from django.shortcuts import render, redirect
from django.http import  HttpResponse, JsonResponse, FileResponse
from mongdb_con import db
import os
from django.core.files.storage import FileSystemStorage
from mongdb_con import gfs
from bson.objectid import ObjectId
from  io import BytesIO,StringIO

import base64





# Create your views here.
def error_404_view(request,exception):
    return render(request,'404.html')

def index(request):
    namedict ={
            "allnames" : db.democoll.files.find()
            # "allnames" : db.democoll.find()
        }
        
    return render(request,'mongocon\index.html', context=namedict)

def add_person(request):
    records = {
        # "first_name": request.GET['f_name'],
        # "last_name": request.GET['l_name']
        "first_name" : "sourav",
        "last_name" : "khanra"
    }
    # db_collection.insert_one(records)
    return HttpResponse("new person is added")

def get_person(request):
    # persons = db_collection.find()
    # return HttpResponse(persons)
    return HttpResponse("ok")

def file_store(filedata):
     if filedata:
            fs = FileSystemStorage()
            # fs = FileSystemStorage(location='/media/')
            file = fs.save(filedata.name, filedata)
            fileurl = fs.url(file)
            return fileurl

def calculate_hash(content): ## check for duplicate
    md5 = hashlib.md5()
    md5.update(content)
    return md5.hexdigest()

def upload_file(request):
    if request.method == 'POST':
        # try:
            filedata = request.FILES.get('document') if 'document' in request.FILES else None

            # myfile = request.FILES.getlist("uploadefiles")

            #//////to store local file media/////
            # file_store(filedata=filedata)
            

            ##///////// to  store  data into mongodb//////
            pdf_content = filedata.read()  #bytesIO >> hex
            # pdf_hash = calculate_hash(pdf_content)
            # if db_collection.find_one({'hash':pdf_hash}):
            #     return JsonResponse({'status':'duplicate','message':'File already exists.'})
            #///////using gridfs/////// stores  as democoll.files and democoll.chunks in collections
            file_id = gfs.put(pdf_content, filename=filedata.name)
            #////////using simple insert method////////
            # print("r")
            # filedict = {
            #     "filename" : filedata.name,
            #     # "hash" : pdf_hash,
            #     "content" : pdf_content
            

            # }
            # db.democoll.insert_one(filedict)
            # namedict ={
            #     "allnames" : db.democoll.find(),
            # }

            #///////
            namedict ={
                "allnames" : db.democoll.files.find(),
            }
            return render(request,'mongocon\index.html',context=namedict)
        # except:
        #     return render(request,'mongocon\error.html')
    
def download_file(request):
    if request.method == 'POST':
        # try:
            filename = request.POST.get('filename')

            #////// download from local media directory///////
            # fs = FileSystemStorage()
            # response = FileResponse(fs.open(filename,'rb'),content_type='application/force-download')
            # response['Content-Disposition'] = 'attachment; filename=filename'
            # return response
            #///////download from mongodb//// using gridfs///
            print(filename)

            file = gfs.find_one({"filename": filename})
            file_data = file.read()

            # for grid_out in gfs.find({"filename": filename},no_cursor_timeout=True):
            #     bytes_data = grid_out.read()

            # print(bytes_data)
            # pdf_data_base64 = base64.b64encode(file_data).decode('utf-8')

            # response = FileResponse(pdf_data_base64, content_type='application/pdf')
            response = HttpResponse(BytesIO(file_data),content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename={filename}'
            print("pdf")
            #/////////using simple find_one methods////
            # data =db.democoll.find_one({'filename':filename},{'_id':0})
            # filename = data['filename']
            # file_bytes = data['content']
            # response = FileResponse(BytesIO(file_bytes), content_type='application/octet-stream')
            # response['Content-Disposition'] = f'attachment; filename={filename}'
            #////////
          
            return response
        # except:
        #     return render(request,'mongocon\error.html')

def update_file(request,name):
    if  request.method=='POST':
        # try:
            filename = name
            dict={
                "filename" : filename
            }
            return render(request,'mongocon/update.html',context=dict)
        # except:
        #     return render(request,'mongocon\error.html')

def update_submit_file(request,name):
    if request.method=='POST':
        # try:
            filename = name
            newdata = request.FILES.get("content")
            newfile = newdata.read()
            newname = newdata.name
            # /////using gridfs////
            f_id = db.democoll.files.find_one({"filename":filename})
            id = ObjectId(str(f_id["_id"]))
            file_files = db.democoll.files.update_one({"filename":filename},{
                "$set":{
                    "filename": newname
                    }
                })
            file_chunks = db.democoll.chunks.update_one({"files_id":id},{
                "$set": {
                    "data" : newfile
                    }
                })
            datalist = {
                "allnames" : db.democoll.files.find()
            }
            #//////usig normal update_one methods///
            # file_data = db.democoll.update_one({"filename":filename},{
            #     "$set": {
            #         "filename" : newname,
            #         "content" : newfile
            #         }
            #     })
            # datalist = {
            #     "allnames" : db.democoll.find()
            # }
            #/////

            return render(request,'mongocon\index.html', context=datalist)
        # except:
        #     return render(request,'mongocon\error.html')


def delete_file(request,name):
    if  request.method == 'POST':
        # try:
            delname = name
            #/////delete files and chunks using gridfs////
            f_id = db.democoll.files.find_one({"filename":delname})
            id = ObjectId(str(f_id["_id"]))
          

            # Get _id of file to delete
            # file_id = gfs.upload_from_stream("test_file", "data I want to store!")
            gfs.delete(id)
            ##//////using simple delete methods///
            # db.democoll.delete_one({"filename":delname})
            # datalist = {
            #     "allnames" : db.democoll.find()
            # }
            #////
            datalist = {
                "allnames" : db.democoll.files.find()
            }
            return render(request,'mongocon\index.html', context=datalist)
        # except:
        #     return render(request,'mongocon\error.html')



def read_file(request):
    if request.method == 'POST':
        # try:
            filename = request.POST.get('filename')
            print(filename)
            # print("x")
            # Retrieve a file from GridFS
            file = gfs.find_one({"filename": filename})
            file_data = file.read()

            # for grid_out in gfs.find({"filename": filename}, no_cursor_timeout=True):
            #     file_data = grid_out.read()
            #////// normal method//////
            # data =db.democoll.find_one({'filename':filename},{'_id':0})
            # print(data)
            
            # filename = data['filename']
            # file_bytes = data['content']
           
            # pdf_data_base64 = base64.b64encode(file_bytes).decode('utf-8')
            

            pdf_data_base64 = base64.b64encode(file_data).decode('utf-8')


            # response = HttpResponse(BytesIO(file_bytes), content_type='application/pdf')
            # response['Content-Disposition'] = f'inline; filename={filename}'

            # read = {
            #     "filename" : filename,
            #     # "filedata": response
            # }
#python manage.py runserver
            # print(response)

            # return response
            # return render(request, 'mongocon/read.html',context=read)
            # return render(request, 'mongocon/read_pdf.html', {'pdf_data_base64': pdf_data_base64})
            return render(request, 'mongocon/read.html', {'pdf_data_base64': pdf_data_base64,"filename":filename})
    
    
        # except:
        #     return render(request,'mongocon\error.html')
        # return render(request,'mongocon/read.html')


def pdf_view(request):
    pass


    



        


    

