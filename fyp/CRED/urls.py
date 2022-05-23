
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerPage,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name='logout'),
    path('',views.home,name="home"), 
    path('click/',views.click,name="click"),
    path('category/',views.category,name="category"),
    path('contentvideo/<str:cat>',views.video_content,name="content"),
    path('contentaudios/<str:cat>',views.contentaudios,name="contentaudios"),
    path('contentbooks/<str:cat>',views.contentbooks,name="contentbooks"),
    path('contentquotes/<str:cat>',views.contentquotes,name="contentquotes"),
    path('playlist/',views.playlist,name="playlist"),
    path('history/',views.history,name="history"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('save_video/<int:id>',views.bookmark_video),
    path('save_audio/<int:id>',views.bookmark_audio),
    path('save_book/<int:id>',views.bookmark_book),
    path('save_qoute/<int:id>',views.bookmark_quote),
    path('approch_video/<int:id>',views.videos_history),
    path('approch_audio/<int:id>',views.audios_history),
    path('approch_book/<int:id>',views.books_history),
    path('approch_qoute/<int:id>',views.quotes_history),
   
]
