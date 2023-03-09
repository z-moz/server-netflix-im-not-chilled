from django.db import models

# Create your models here.

class SpoilerTopic(models.Model):
    id = models.BigAutoField(primary_key=True)
    topic_title = models.CharField(max_length=100)
    netflix_id = models.IntegerField(blank=False)
    yes_vote = models.IntegerField(default=0)
    no_vote = models.IntegerField(default=0)

    def __str__(self):
        return self.topic_title
