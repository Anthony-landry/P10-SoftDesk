# Generated by Django 4.2.5 on 2023-09-27 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('projet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='project_contributors',
                                    related_query_name='project_contributors',
                                    to='projet.project'),
        ),
        migrations.AddField(
            model_name='contributor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='user',
                                    related_query_name='user',
                                    to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True,
                                         help_text='The groups this user belongs to. A user will get all permissions '
                                                   'granted to each of their groups.',
                                         related_name='user_set',
                                         related_query_name='user',
                                         to='auth.group',
                                         verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True,
                                         help_text='Specific permissions for this user.',
                                         related_name='user_set',
                                         related_query_name='user',
                                         to='auth.permission',
                                         verbose_name='user permissions'),
        ),
    ]