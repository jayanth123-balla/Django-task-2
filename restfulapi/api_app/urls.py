from django.urls import path
from .views import Assetviews

urlpatterns = [
    path('shapefile/',     Assetviews.as_view()),
    path('shapefile/<int:id>', Assetviews.as_view())
	
]
