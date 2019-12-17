from django.contrib import admin
from django.urls import path, include
from basicapp import views

urlpatterns = [
	path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('basicapp/', include('basicapp.urls'))
]