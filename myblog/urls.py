from django.urls import path
from . import views

urlpatterns = [
    path('',views.list,name='list'),
    path('post/<int:id>',views.post,name='post'),
    path('create/',views.create,name='create'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),

    ###########################
    path('comment/<int:id>',views.comment,name='comment')
    
]