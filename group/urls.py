from django.urls import path
from . import views

app_name = 'group'

urlpatterns = [
     path('', views.GroupList, name='grouplist'),
     path('groupdetail/<int:pk>/', views.GroupDetail, name = 'groupdetail'),
     path('creategroup/', views.CreateGroup, name ='creategroup'),
     path('updategroup/<int:pk>/', views.UpdateGroup, name = 'updategroup'),
     path('deletegroup/<int:pk>/', views.DeleteGroup, name = 'deletegroup'),
     path('joingroup/<int:pk>/', views.JoinGroup, name = 'joingroup'),
     path('leavegroup/<int:pk>/', views.LeaveGroup, name = 'leavegroup'),
]
