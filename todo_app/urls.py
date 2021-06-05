from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('done/<int:taskid>/',views.delete,name='donetask'),
    path('update/<int:id>/',views.update,name='updatetask'),
    path('cbvhome/',views.tasklistview.as_view(),name="cbvhome"),
    path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name="cbvdetail"),
    path('cbvupdate/<int:pk>/',views.taskupdateview.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.taskdeleteview.as_view(),name="cbvdelete")
]