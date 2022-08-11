# Generated by Django 4.0.6 on 2022-08-10 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='이미지')),
                ('title', models.CharField(max_length=35, verbose_name='제목')),
                ('content', models.TextField(verbose_name='내용')),
                ('check_count', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='커뮤니티 등록 일자')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='커뮤니티 수정 일자')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(choices=[('community', '커뮤니티'), ('market', '나눔마켓')], default='community', max_length=10, verbose_name='태그')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='댓글')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='커뮤니티 댓글 생성시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='커뮤니티 댓글 수정시간')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.article', verbose_name='게시글')),
            ],
        ),
    ]
