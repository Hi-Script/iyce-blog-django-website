# Generated by Django 4.1.2 on 2023-01-02 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iycee', '0012_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=b'I01\n', max_length=150, null=True)),
                ('body', models.TextField(blank=b'I01\n', null=b'I01\n')),
                ('post_pic', models.ImageField(blank=b'I01\n', null=b'I01\n', upload_to='feature/')),
                ('created', models.DateTimeField(auto_now_add=True, null=b'I01\n')),
                ('updated', models.DateTimeField(auto_now=True, null=b'I01\n')),
                ('author', models.ForeignKey(null=b'I01\n', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]