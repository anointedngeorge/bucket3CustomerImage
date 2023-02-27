

from ninja import Router
from bucket.models import *
from image.schema.imageSchema import *
from django.shortcuts import get_object_or_404
from typing import List
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
import pickle
import os
import sys
import base64

router = Router(tags=["Gallery"])


filename =  'imageGallery/imagebyte.txt'
image_filename = os.path.realpath('storage/fb')



@router.post('/register-gallery/{code}/')
def register_image_gallery(request, code, file: UploadedFile = File(...)):
    filedata = file.read()
    # print(name)
    encode =  base64.encodebytes(filedata)
    filetype =  str(file.name).split('.')[1]
    g= Gallery.objects.all()
    name =  uuid.uuid4().hex
    req = request.META
    path= ''
    if req.get('SCRIPT_NAME') == '':
        path += f"{req.get('wsgi.url_scheme')}://{req.get('HTTP_HOST')}"
    else:
        path += f"{req.get('wsgi.url_scheme')}://{req.get('HTTP_HOST')}{req.get('SCRIPT_NAME')}"
    # http://127.0.0.1:8000/media/storage/fb/Screenshot_from_2023-02-13_08-30-02.png
    url =  f"{path}/media/storage/fb/{name}.{filetype}"
    filename2 = f"{name}.{filetype}"
    data = {
        'name':name,
        'size':file.size,
        'filename':filename2,
        'type':filetype,
        'data':encode,
        'url':url,
        'code':code,
    }
  
    # print(url)
    g.create(**data)
    decoded_data=base64.decodebytes(encode)
    d = os.path.exists(image_filename)
    # print(d)
    img_file = open(f"{image_filename}/{filename2}", 'wb')
    img_file.write(decoded_data)
    img_file.close()
 
    return {'name': file.name, 'len': file.size, 'code':code}



@router.get('/get-gallery-image/', response=List[GalleryOut])
def get_gallery_image(request):
    '''Get gallery image'''
    try:
        gallery = Gallery.objects.all()
        return gallery
    except Exception as e:
        return f"{e}"
  


@router.get('/get-gallery-image/{code}/', response=List[GalleryOut])
def get_gallery_image_by_code(request, code:str):
    '''Get gallery image'''
    try:
        if Gallery.objects.all().filter(code=code).exists():
            gallery = Gallery.objects.all().filter(code=code)
            return gallery
        else:
            return {'data':'Failed'}
    except Exception as e:
        return f"{e}"


@router.delete('/delete-gallery/{name}/')
def delete_image_gallery(request, name:str):
    '''
    deleting  image api....
    '''
    g = Gallery.objects.filter(name=name)
    if g.exists():
        g = Gallery.objects.filter(name=name).get()
        os.unlink(f"storage/fb/{g.filename}")
        Gallery.objects.filter(name=name).delete()
    else:{'message':'Could not locate file with name'}
    return {"message":"Deleted successfully"}
