# Generated by Django 4.2 on 2023-05-28 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_alter_reviews_created_at'),
        ('cart', '0002_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_rel', to='courses.courses'),
        ),
    ]