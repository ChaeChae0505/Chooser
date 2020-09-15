# Generated by Django 3.1 on 2020-09-14 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('member_ban', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', main.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('debate_id', models.AutoField(primary_key=True, serialize=False)),
                ('debate_pre_date', models.DateTimeField(auto_now_add=True)),
                ('debate_img1', models.ImageField(blank=True, upload_to='')),
                ('debate_img2', models.ImageField(blank=True, upload_to='')),
                ('debate_img1_name1', models.CharField(max_length=20)),
                ('debate_img2_name2', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_content', models.TextField()),
                ('topic_start_date', models.DateTimeField(auto_now_add=True)),
                ('topic_end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('vote_id', models.AutoField(primary_key=True, serialize=False)),
                ('vote_result_1', models.IntegerField()),
                ('vote_result_2', models.IntegerField()),
                ('vote_debate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.debate')),
                ('vote_member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prefer',
            fields=[
                ('prefer_id', models.AutoField(primary_key=True, serialize=False)),
                ('prefer_title', models.CharField(max_length=50)),
                ('prefer_date', models.DateTimeField(auto_now_add=True)),
                ('prefer_content', models.TextField()),
                ('prefer_member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_prefer',
            fields=[
                ('com_pre_id', models.AutoField(primary_key=True, serialize=False)),
                ('com_pre_content', models.TextField()),
                ('com_pre_member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('com_pre_prefer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.prefer')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_debate',
            fields=[
                ('com_deb_id', models.AutoField(primary_key=True, serialize=False)),
                ('con_deb_date', models.DateTimeField(auto_now_add=True)),
                ('com_deb_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.debate')),
                ('com_deb_member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]