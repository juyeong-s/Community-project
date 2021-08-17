from django.urls import path
from . import views

urlpatterns = [
    path('getPostlist/', views.getPostlist, name='getPostlist'),
    path('getUserlist/', views.getUserlist, name='getUserlist'),
    path('postsave/', views.postsave, name='postsave'),
    path('viewcnt_save/', views.viewcnt_save, name='viewcnt_save'),
    path('pagedpostlist/<int:id>', views.pagedpostlist, name='pagedpostlist'),
    path('postdelete/<int:id>', views.postdelete, name='postdelete'),
    
]