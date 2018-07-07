from content import views
from django.urls import path
urlpatterns =[
    path('', views.homepage),
    path('about/', views.about),
    path('program/', views.program),
    path('testimonials/', views.testimonials),
    path('resources/', views.resources),
    path('acknowledgement/', views.acknowledgement)
]