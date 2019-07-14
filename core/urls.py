from django.conf.urls import url
from core import views


# app_name="core"

index_path=[
    url('index$', views.index),
    url('video',views.video,name="video"),
    url('layer',views.layer),
    url('case',views.Case)
]

urlpatterns = index_path
