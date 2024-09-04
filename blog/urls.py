from django.urls import path
from .views import blog,post,post_comment,search_view,get_category

urlpatterns = [
    path('', blog, name='blog'),
    path('post/<str:title>/', post, name='post'),
    path('comment/',post_comment,name='comment'),
    path('search/',search_view,name='search'),
    path('category/<str:cat>/',get_category,name='category'),
]