# Generated by Django 5.0.4 on 2024-05-22 13:16

import django.core.validators
import django.db.models.deletion
import listing.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(choices=[('top', 'Top'), ('bottom', 'Bottom'), ('footwear', 'Footwear')], max_length=255, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Main Category Cover Image')),
            ],
            options={
                'verbose_name': 'Main Category',
                'verbose_name_plural': 'Main Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategoryClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('uploaded_image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('sub_category', models.CharField(blank=True, default='', max_length=155, null=True)),
                ('score', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('gender', models.CharField(blank=True, choices=[('men', 'Men'), ('women', 'Women')], max_length=25, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('condition', models.CharField(choices=[('Heavily Used', 'Heavily Used'), ('Well Used', 'Well Used'), ('Lightly Used', 'Lightly Used'), ('Like New', 'Like New'), ('Brand New', 'Brand New')], max_length=100)),
                ('color', models.CharField(choices=[('White', 'White'), ('Black', 'Black'), ('Beige', 'Beige'), ('Red', 'Red'), ('Blue', 'Blue'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Orange', 'Orange'), ('Purple', 'Purple'), ('Pink', 'Pink'), ('Brown', 'Brown'), ('Grey', 'Grey'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Multi', 'Multi')], max_length=100)),
                ('is_sold', models.BooleanField(default=False)),
                ('is_manual', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('review', models.TextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.listing')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
            },
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/', verbose_name='image')),
                ('is_cover', models.BooleanField(default=False)),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listing_image', to='listing.listing')),
            ],
            options={
                'verbose_name': 'Listing Image',
                'verbose_name_plural': 'Listing Images',
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('size', models.CharField(max_length=50)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listing.category')),
            ],
            options={
                'unique_together': {('category', 'size')},
            },
        ),
        migrations.CreateModel(
            name='PreferredSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preferred_sizes', to='listing.preference')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.size')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='listing',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.size'),
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=155, verbose_name='Sub-category Name')),
                ('slug', models.SlugField(blank=True, max_length=155, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=listing.models.subcat_image_upload_path, verbose_name='Category Cover Image')),
                ('gender', models.CharField(blank=True, choices=[('men', 'Men'), ('women', 'Women'), ('others', 'Others')], max_length=25, null=True)),
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listing.category')),
            ],
            options={
                'verbose_name': 'Sub-category',
                'verbose_name_plural': 'Sub-categories',
            },
        ),
        migrations.CreateModel(
            name='PreferredSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preferred_subcategories', to='listing.preference')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listing.subcategory')),
            ],
            options={
                'verbose_name': 'Preferred Sub-Category',
                'verbose_name_plural': 'Preferred Sub-Categories',
            },
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listing.subcategory'),
        ),
    ]
