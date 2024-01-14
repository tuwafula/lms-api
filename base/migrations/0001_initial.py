# Generated by Django 4.2.9 on 2024-01-14 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('stock', models.PositiveIntegerField()),
                ('rent_fee', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('outstanding_debt', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('is_returned', models.BooleanField(default=False)),
                ('rent_fee_charged', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.member')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
