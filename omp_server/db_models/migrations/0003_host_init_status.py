# Generated by Django 3.1.4 on 2021-12-02 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_models', '0002_auto_20211202_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='init_status',
            field=models.CharField(choices=[(0, '未执行'), (1, '成功'), (
                2, '失败')], default=0, help_text='主机初始化状态', max_length=16, verbose_name='主机初始化状态'),
        ),
    ]
