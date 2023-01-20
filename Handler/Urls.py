from django.urls import path
from . views import Home,Login,Register,Profile,Logout
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    
    path('', Home.as_view(),name="defult"),
    path('Login', Login.as_view(),name="login",),
    path('Register', Register.as_view()),
    path('Profile', Profile.as_view()),
    path('Logout', Logout.as_view()),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)