from django.contrib import admin
from django.urls import path, include
from krishisahay import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('auth/', include("authentication.urls"))
]
