from rest_framework import generics
from .serializers import SpoilerTopicSerializer
from .models import SpoilerTopic

# Create your views here.

class SpoilerTopicAPIView(generics.ListCreateAPIView):
    queryset = SpoilerTopic.objects.all()
    serializer_class = SpoilerTopicSerializer

class SpoilerTopicDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpoilerTopic.objects.all()
    serializer_class = SpoilerTopicSerializer


class SpoilerTopicAPIViewByNetflixId(generics.ListAPIView):

    def get_queryset(self):
        """
        This view returns a list of all spoiler topics related to a specific netflix film as determined by the id portion of the URL.
        """
        id = self.kwargs['id']
        return SpoilerTopic.objects.filter(netflix_id=id)

    serializer_class = SpoilerTopicSerializer


