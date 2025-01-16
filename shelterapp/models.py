from django.db import models
from django.contrib.auth.models import User

class Shelter(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='shelter_photos/', blank=True, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shelters')

    def __str__(self):
        return self.name
    
class UserShelter(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
        
        class Meta:
            unique_together = ('user', 'shelter')