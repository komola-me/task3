# Generated by Django 4.0.6 on 2022-07-22 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='post/')),
                ('published_date', models.DateField(auto_now=True)),
                ('view_count', models.IntegerField(default=0)),
                ('is_popular', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='author.author')),
                ('tag', models.ManyToManyField(related_name='post', to='post.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]