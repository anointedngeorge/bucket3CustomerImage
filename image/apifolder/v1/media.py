from ninja import Router


router = Router(tags=['media'])


@router.post('register-media/')
def post_mediafile(request):
    ''' Get all media files '''

    return {'id':12}

@router.get('get-media-token/{token}/')
def get_mediafile_token(request, token:str):
    ''' Get media files by token'''

    return {'id':12}

@router.get('get-all-media/')
def get_mediafile(request):
    ''' Get all media files'''

    return {'id':12}


@router.delete('/')
def delete_mediafile(request):
    ''' Delete all media files'''

    return {'id':12}