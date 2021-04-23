from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('edit/<int:pk>/', views.UpdatePostView.as_view(), name='update_post'),
    path('delete/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_Category'),
    path('category/<str:cats>/', views.category_view, name='category'),
    path('category_list/', views.category_list_view, name='category_list'),
]