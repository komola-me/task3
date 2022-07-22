from django.db import models
from helpers.models import BaseModel

class Author(BaseModel):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)