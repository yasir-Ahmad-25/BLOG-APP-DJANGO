from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()

    context = {
        'posts' : posts
    }

    return render(request, 'index.html' , context)


def createPost(request):
    if request.method == "POST":
        # get the posted data
        title = request.POST.get('post_Title') 
        content = request.POST.get('post_content')
        image = request.POST.get('post_image')

        # save data to the database
        post = Post()
        post.title = title
        post.content = content 
        post.banner = image
        post.save()
        return redirect('createPost')
    return render(request, 'create_post.html', {})

def viewPost(request, post_id):
    post = Post.objects.get(id=post_id)
    
    context = {
        'post': post
    }
    return render(request, 'view_post.html' , context)

from django.shortcuts import get_object_or_404, redirect, render
from .models import Post

def updatePost(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    context = {
        'post': post
    }

    if request.method == 'POST':
        # Get posted data for title and content
        title = request.POST.get('post_Title')
        content = request.POST.get('post_content')
        
        # Check if a new image is uploaded
        new_image = request.FILES.get('post_image')  # Use request.FILES for image files
        
        # Update the post object
        post.title = title
        post.content = content
        
        # Only update the banner if a new image was uploaded
        if new_image:
            post.banner = new_image
        
        post.save()  # Save the updated post

        return redirect('Home')  # Redirect to the home page after update

    return render(request, 'update_post.html', context)



def Login(request):
    return render(request, 'Login.html' , {})

def Registeration(request):
    return render(request, 'Registeration.html' , {})
