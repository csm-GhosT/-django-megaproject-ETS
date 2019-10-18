from django.shortcuts import render
from . import forms
from django.core.files.storage import FileSystemStorage
from . import ocr_optifine
from django.http import HttpResponse
import glob
import os
from PIL import Image
import pytesseract
import argparse
import cv2

# Create your views here.
def index(request):
    emptyMedia()
    return render(request,'firstapp/formpage.html')

def form_name_view(request):
    form =forms.FormName()
    emptyMedia()
    if(request.method=='POST'):
        form=forms.FormName(request.POST)
        uploaded_file=request.FILES['document']

        emptyMedia() #delete previous images
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        
      
        
        print("Image saved")
        text=ocr_optifine.main()
        
        renameImage();
        
        if(text!='/0'):
            my_dict ={'text':text}
            return render(request,'firstapp/formpage.html',context=my_dict)


    return render(request, 'firstapp/formpage.html', {'form':form})


def emptyMedia():
    files = glob.glob('media/*')
    for f in files:
        os.remove(f)

def getImagePath():
    IMAGES_DIR=".\media"
    # print(IMAGES_DIR)
    for fileName in os.listdir(IMAGES_DIR):
     print(" ")
    im_dir=os.path.join(IMAGES_DIR, fileName)
    print(im_dir)
    return im_dir

def renameImage():
    os.rename(getImagePath(),"media/img.png")