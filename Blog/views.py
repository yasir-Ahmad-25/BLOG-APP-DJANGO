from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html' , {})


def createPost(request):
    if request.method == "POST":
        # get the posted data
        title = request.POST.get('post_Title') 
        content = request.POST.get('post_content')
        image = request.POST.get('post_image')

        return HttpResponse(f'POSTED DATA: \nTITLE: {title}\nCONTENT: {content}\nIMAGE: {image}')
    return render(request, 'create_post.html', {})

def viewPost(request, post_id):
    manual_id = post_id
    context = {
        'id': manual_id
    }
    return render(request, 'view_post.html' , context)

def updatePost(request, post_id):
    manual_id = post_id
    context = {
        'id': manual_id
    }
    return render(request, 'update_post.html' , context)


def Login(request):
    return render(request, 'Login.html' , {})

def Registeration(request):
    return render(request, 'Registeration.html' , {})