# Generated by Django 2.0.4 on 2018-04-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oderascrumy', '0008_auto_20180428_0100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrumyuser',
            name='role',
        ),
        migrations.AddField(
            model_name='scrumyuser',
            name='roles',
            field=models.CharField(choices=[('OWNER', 'OWNER'), ('ADMIN', 'ADMIN'), ('QA', 'QUALITY ANALYST'), ('DEV', 'DEVELOPER')], default='OWNER', max_length=5),
        ),
        migrations.AlterField(
            model_name='goalstatus',
            name='status',
            field=models.CharField(choices=[('DT', 'Daily Task'), ('WT', 'Weekly Task'), ('V', 'Verified'), ('D', 'Done')], default='DT', max_length=2),
        ),
        migrations.AlterField(
            model_name='scrumygoals',
            name='goal_status',
            field=models.CharField(choices=[('C', 'Completed'), ('O', 'Ongoing'), ('P', 'Pending')], default='C', max_length=1),
        ),
    ]
