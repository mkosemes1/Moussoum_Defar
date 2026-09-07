# Generated manually

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_annotationtask_annotationresult_notification_payment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasubmission',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='submissions/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='datacollection',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_collections', to=settings.AUTH_USER_MODEL),
        ),
    ]
