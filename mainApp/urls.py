from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('coming_soon', views.coming_soon, name='coming_soon'),
    path('add_data', views.add_data, name='add_data'),
    path('download_xlsx', views.download_xlsx, name='download_xlsx'),
    path('preview_xlsx', views.preview_xlsx, name='preview_xlsx')
]