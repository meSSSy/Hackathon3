from . import views
from django.urls import path

urlpatterns = [
# path('', views.HomePage.as_view(), name='home'),
path('', views.PostList.as_view(), name='index'),
path('featured/', views.featuredpost, name='featured'),
path('post/<slug:slug>/', views.post_detail, name='post_detail'),
path('post/<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
path('post/<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
path('backend/', views.backend_view, name='backend'),
path('ai/', views.ai_view, name='ai'),
path('cybersecurity/', views.cybersecurity_view, name='cybersecurity'),
path('design/', views.design_view, name='design'),
path('frontend/', views.frontend_view, name='frontend'),
]