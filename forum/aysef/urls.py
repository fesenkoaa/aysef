from django.urls import path
from .views import *

urlpatterns = [
    path('main/', MainPage.as_view(), name='main'),
    path('about/', AboutPage.as_view(), name='about'),
    path('support/', SendMessagePage.as_view(), name='support'),

    path('forum/', Forum.as_view(), name='forum'),
    path('forum/themes/', Themes.as_view(), name='themes'),
    path('forum/unique_number/<slug:unique_number>/', TheTheme.as_view(), name='theme'),  # -
    path('forum/add-theme/', AddTheme.as_view(), name='add_theme'),  # admin
    path('forum/delete-theme/tun/<int:unique_number>/', DeleteTheme.as_view(), name='delete_theme'),  # admin  # -
    path('forum/<int:unique_number>', TheArticle.as_view(), name='article'),  # -
    path('forum/add-article/', AddArticle.as_view(), name='add_article'),
    path('forum/edit-article/<int:unique_number>', EditArticle.as_view(), name='edit_article'),  # -
    path('forum/delete-article/<int:unique_number>', DeleteArticle.as_view(),  # -
         name='delete_article'),

    path('registration/', Reg.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('reset-password/', ResetPassword.as_view(), name='reset_password'),
    path('change-password/', ChangePassword.as_view(), name='change_password')
]

