# Generated by Django 5.1.2 on 2024-10-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('author', models.CharField(db_index=True, max_length=200)),
                ('isbn', models.CharField(db_index=True, max_length=13, unique=True)),
                ('published_date', models.DateField()),
                ('available_copies', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['title'],
                'permissions': [('can_borrow_books', 'Can borrow books'), ('can_manage_books', 'Can manage books')],
                'indexes': [models.Index(fields=['published_date'], name='books_book_publish_649cd8_idx')],
            },
        ),
    ]
