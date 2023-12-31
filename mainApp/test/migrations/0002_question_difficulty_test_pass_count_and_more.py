# Generated by Django 4.2.4 on 2023-09-01 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='test',
            name='pass_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='test',
            name='pass_percentage',
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='test.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='test.test'),
        ),
    ]
