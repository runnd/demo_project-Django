# Generated by Django 3.1 on 2024-05-25 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('name_kh', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tbl_room_type',
            },
        ),
    ]
