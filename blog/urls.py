from . import views
from django.urls import path

urlpatterns = [
# path('', views.HomePage.as_view(), name='home'),
path('', views.index, name='index'),
path('<slug:slug>/', views.post_detail, name='post_detail'),
    path(
        '<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'),
    path(
        '<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'),
]