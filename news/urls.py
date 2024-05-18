from django.urls import path
from .views import PostList, PostDetal

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetal.as_view())
]