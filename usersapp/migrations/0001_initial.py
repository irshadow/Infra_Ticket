# Generated by Django 5.1.2 on 2024-10-30 18:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('servicesapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(1, 'Man'), (2, 'Woman')])),
                ('role', models.IntegerField(choices=[(1, 'Department manager'), (2, 'Head of special team'), (3, 'Expert employee')])),
                ('ip', models.GenericIPAddressField(blank=True, editable=False, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='servicesapp.departmentmodel')),
                ('team', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='servicesapp.servicemodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
