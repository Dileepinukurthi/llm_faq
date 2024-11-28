from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path('api/faqs/', views.list_faqs, name='list_faqs'),
    path('api/query/', views.QueryFAQ.as_view(), name='query_faq'),

]
