from django.urls import path
from happ.views import *

urlpatterns=[
    path('adhome/',adhome),
    path('addisplay/',addisplay),
    path('adproduct/',addproduct),
    path('update/<id>',update),
    path('delete/<id>',delete),
    path('adregister/',adregister),
    path('main/',main),
    path('uregister/',uregister),
    path('uhome/',uhome),
    path('uorders/',uorders),
    path('uitem/',uitem),
    path('user/<id>',user),
    path('udelete/<id>',udelete),
    path('uorderitem/',uorderitem),
    path('ureview/',ureview),
    path('adreview/',adreview),
    path('addelete/<id>',addelete),
    path('ulogin/',ulogin),
    path('',Product.as_view())
    

]