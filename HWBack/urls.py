from django.contrib import admin
from concert import views
from django.urls import include, path
from rest_framework import routers


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetMenu, name='main_url'),
    path('artist/<int:pk>', views.GetArtist, name='artist_url'),
    path('artistsconcerts', views.GetAllArtistAllConcerts),
    path('all_artists', views.GetAllArtists, name='all_artists_url'),
    path('concert/<int:pk>', views.GetExactConcert, name='concerts_url'),
]
