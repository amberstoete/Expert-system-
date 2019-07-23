from django.urls import path

from . import views

urlpatterns = [
    path('index.html', views.get_user_input),
    path('static/style.css', views.get_user_input),
    path('static/index2.js', views.get_user_input),
    path('post2', views.post2),

    # path('page2.html', views.post2),
    # # path('', views.post2),
    # path('page2.html', views.post2),
]
