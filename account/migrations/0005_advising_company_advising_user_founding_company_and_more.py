# Generated by Django 4.2.7 on 2024-07-05 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publicapp', '0002_client_country_client_description_client_industry_and_more'),
        ('account', '0004_remove_founding_company_delete_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advising',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='advisor', to='publicapp.client'),
        ),
        migrations.AddField(
            model_name='advising',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='advisor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='founding',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='founder', to='publicapp.client'),
        ),
        migrations.AddField(
            model_name='investing',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='investor', to='publicapp.client'),
        ),
        migrations.AddField(
            model_name='investing',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='investor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='founding',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='founder', to=settings.AUTH_USER_MODEL),
        ),
    ]