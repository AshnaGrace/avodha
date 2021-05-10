from django.urls import path
from .import views
urlpatterns=[

    path('',views.fun,name="fun"),
    path('vlog/', views.test, name="test"),
    # path('add',views.addition,name="add")
]
