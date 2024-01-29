from django.urls import path, include
from watchlist_app.api.views  import ( WatchListView,
                                      StreamPlatformListCreateView,StreamPlatformDetailView,WatchListDetailView)

urlpatterns =[
    path('list/',WatchListView.as_view(),name = 'arun '),
    path('stream/', StreamPlatformListCreateView.as_view(), name='streamplatform-list-create'),
 path('stream/<int:pk>/', StreamPlatformDetailView.as_view(), name='streamplatform-detail'),
 path('list/<int:pk>/',WatchListDetailView.as_view(),name='movielist-detail')
]
  
   
   
 


