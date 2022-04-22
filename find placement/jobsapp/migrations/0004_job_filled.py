
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0003_job_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='filled',
            field=models.BooleanField(default=False),
        ),
    ]
