from django.urls import path
from .views import SpoilerTopicAPIView, SpoilerTopicDetailAPIView, SpoilerTopicAPIViewByNetflixId

urlpatterns = [
    path('<int:pk>/', SpoilerTopicDetailAPIView.as_view(), name='spoiler_topic_by_id'),
    path('netflix_id/<int:id>/', SpoilerTopicAPIViewByNetflixId.as_view(),
         name='spoiler_topic_by_netflix_id'),
    path('api/', SpoilerTopicAPIView.as_view(), name="spoiler_topic_api"),

]