# Generated by Django 4.1.5 on 2023-01-23 06:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.SlugField(primary_key=True, serialize=False, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='electronics.category')),
            ],
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=88)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.PositiveIntegerField(default=10)),
                ('status', models.CharField(choices=[('on_sale', 'on sale'), ('out_of_stock', 'out of stock')], default='on_sale', max_length=50)),
                ('orders_count', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electronics', to='electronics.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='electronics', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParsedElectronic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField()),
                ('electronic_recommend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='electronics.parsedelectronic')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('electronic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='electronics.electronic')),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thickness', models.CharField(blank=True, max_length=128, null=True)),
                ('display', models.CharField(blank=True, max_length=128, null=True)),
                ('processor', models.CharField(blank=True, max_length=128, null=True)),
                ('video', models.CharField(blank=True, max_length=10, null=True)),
                ('memory', models.CharField(blank=True, max_length=120, null=True)),
                ('size', models.CharField(blank=True, max_length=128, null=True)),
                ('weight', models.CharField(blank=True, max_length=128, null=True)),
                ('electronic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='electronics', to='electronics.electronic')),
            ],
        ),
    ]
