from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainPage.as_view(), name='main'),
    path('about/', AboutPage.as_view(), name='about'),
    path('support/', SendMessagePage.as_view(), name='support'),

    path('forum/', Forum.as_view(), name='forum'),
    path('themes/', Themes.as_view(), name='themes'),
    path('theme/<int:pk>/', TheTheme.as_view(), name='theme'),
    path('article/<int:pk>/', TheArticle.as_view(), name='article'),
    path('my-articles/<int:pk>/', MyArticles.as_view(), name='my'),
    path('add-article/', AddArticle.as_view(), name='add_article'),
    path('edit-article/<int:pk>/', EditArticle.as_view(), name='edit_article'),
    path('delete-article/<int:pk>/', DeleteArticle.as_view(),
         name='delete_article'),

    path('registration/', Reg.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('reset-password/', ResetPassword.as_view(), name='reset_password'),
    path('change-password/', ChangePassword.as_view(), name='change_password')
]

