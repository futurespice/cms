from django.urls import path
from . import views

urlpatterns = [
    # First Page URLs
    path('api/first/', views.first_page, name='first-page'),
    path('api/first/title/', views.first_page_title, name='first-page-title'),
    path('api/first/subtitle/', views.first_page_subtitle, name='first-page-subtitle'),
    path('api/first/button/', views.first_page_button, name='first-page-button'),
    path('api/first/image/', views.first_page_image, name='first-page-image'),

    # Second Page URLs
    path('api/second/', views.second_page, name='second-page'),
    path('api/second/title/', views.second_page_title, name='second-page-title'),
    path('api/second/subtitle/', views.second_page_subtitle, name='second-page-subtitle'),
    path('api/second/button/', views.second_page_button, name='second-page-button'),
    path('api/second/image/', views.second_page_image, name='second-page-image'),

    # Third Page URLs
    path('api/third/', views.third_page, name='third-page'),
    path('api/third/title/', views.third_page_title, name='third-page-title'),
    path('api/third/subtitle/', views.third_page_subtitle, name='third-page-subtitle'),
    path('api/third/button/', views.third_page_button, name='third-page-button'),
    path('api/third/image/', views.third_page_image, name='third-page-image'),
]