from django.db import models


class Asset(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    parent = models.ForeignKey("self", null=True, related_name="children")

    class Meta:
        ordering = ('created',)