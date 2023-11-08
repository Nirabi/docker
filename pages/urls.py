from django.urls import path


from .views import Home_Page_View


urlpatterns = [
    path('',Home_Page_View, name='home'),
]