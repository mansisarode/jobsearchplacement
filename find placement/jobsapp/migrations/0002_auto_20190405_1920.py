
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('1', 'Full time'), ('2', 'Part time'), ('3', 'Internship')], max_length=10),
        ),
    ]
