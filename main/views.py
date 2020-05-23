from django.shortcuts import render
from django.http import HttpResponse
from random import random
import pickle
import face_recognition
import numpy
# Create your views here.


def homepage(request):
    return render(request=request , template_name='asd.html')




def upload(request):
    if request.method == 'POST':
        name=random()
        handle_uploaded_file(request.FILES['file'],name)
        with open('celeb.pickle', 'rb') as handle:
            enc = pickle.load(handle)
        known_image = face_recognition.load_image_file('main/static/uploads/{}.jpg'.format(name))
        testimg = face_recognition.face_encodings(known_image)  
        dm=[]
        outid="no match"
        minenc=9999
        for j in enc:
            if len(j["encoding"])!=0:
                dist=numpy.linalg.norm(j["encoding"][0]-testimg[0])
                if dist < minenc:
                    minenc=dist
                    outid=j["id"]
        return render(request=request , template_name='res.html' , context={"upname":name , "outid":outid})
    else:
        return HttpResponse(' no post request detected')
          










def handle_uploaded_file(f,name):
    with open('main/static/uploads/{}.jpg'.format(name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
