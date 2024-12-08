from django.urls import path
from .views import index ,viewPost,createPost,updatePost,Login,Registeration,deletePost
urlpatterns = [
    path('' , index , name='Home'),
    path('view_post/<int:post_id>/' , viewPost , name='viewPost'),
    path('update_post/<int:post_id>/' ,  updatePost, name='updatePost'),
    path('delete_post/<int:post_id>/' ,  deletePost, name='deletePost'),
    path('create_post/' , createPost , name='createPost'),
    path('Login/' , Login , name='Login'),
    path('Registeration/' , Registeration , name='Register'),
]
