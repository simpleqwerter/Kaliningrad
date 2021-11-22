from django.urls import path
from . import views

urlpatterns = [
    path('', views.Redirect.as_view(), name='home'),
    path('api/data/', views.GuideHome.as_view(), name='home'),
    path('api/data/list/<int:page>/<int:limit>', views.GuideList.as_view(), name='guide_list'),
    path('api/data/<int:pk>', views.GuideDetailView.as_view(), name='guide_list-detail'),
    path('api/data/add', views.StationFormView.as_view(), name='create_station'),
    path('api/data/delete/<int:id>/', views.DeleteStationView.as_view(), name='create_station'),
    path('api/data/search', views.SearchView.as_view(), name='search'),
    path('api/data/file_db', views.file_db, name='file_db'),



]


