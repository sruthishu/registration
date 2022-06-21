from  django.urls  import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('form/',form_view,name='form')
]
