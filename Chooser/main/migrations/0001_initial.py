

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
            name='Member',
            fields=[
                ('member_id', models.AutoField(primary_key=True, serialize=False)),
                ('member_email', models.EmailField(max_length=254, null=True, unique=True)),
                ('member_ban', models.BooleanField(default=False)),
                ('member_nickname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
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
