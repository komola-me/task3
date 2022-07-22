from django.db import models
from author.models import Author
from helpers.models import BaseModel

# Create your models here.
CREATED = 'created'
MODERATED = 'moderated'
PUBLISHED = 'published'

POST_STATUS = (
    (CREATED, 'created'),
    (MODERATED, 'moderated'),
    (PUBLISHED, 'published')
)

class Tag(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

class Post(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=256)
    content = models.TextField()
    image = models.ImageField(upload_to = 'post/')

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='post')
    tag = models.ManyToManyField(Tag, related_name='post')

    published_date = models.DateField(auto_now=True)
    view_count = models.IntegerField(default=0)
    is_popular = models.BooleanField(default=False)

