# Generated by Django 3.2.7 on 2021-09-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QUIZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=50)),
                ('no_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='time to pass quiz')),
                ('required_score', models.IntegerField(help_text='you must get % to pass')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=50)),
            ],
            options={
                'verbose_name_plural': 'quizes',
            },
        ),
    ]
