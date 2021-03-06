# Generated by Django 2.1.7 on 2019-04-10 17:38

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('organizationname', models.CharField(blank=True, db_column='OrganizationName', max_length=255, null=True)),
                ('organizationlocation', models.CharField(blank=True, db_column='OrganizationLocation', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Organization',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('permissionname', models.CharField(blank=True, db_column='PermissionName', max_length=255, null=True)),
                ('permissionactive', models.TextField(db_column='PermissionActive')),
                ('create', models.TextField(db_column='Create')),
                ('read', models.TextField(db_column='Read')),
                ('update', models.TextField(db_column='Update')),
                ('delete', models.TextField(db_column='Delete')),
                ('read_others', models.TextField(db_column='Read_others')),
                ('update_others', models.TextField(db_column='Update_others')),
            ],
            options={
                'db_table': 'Permission',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('profilename', models.CharField(blank=True, db_column='ProfileName', max_length=255, null=True)),
                ('active', models.TextField(db_column='Active')),
                ('userid', models.IntegerField(db_column='UserID')),
                ('permission', models.ManyToManyField(to='Users.Permission')),
            ],
            options={
                'db_table': 'Profile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='UserName', max_length=255, null=True, unique=True)),
                ('useremail', models.CharField(blank=True, db_column='UserEmail', max_length=255, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
                ('userrole', models.CharField(blank=True, db_column='UserRole', max_length=255, null=True)),
                ('active', models.TextField(db_column='Active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('organizationid', models.ForeignKey(db_column='OrganizationID', null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Organization')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
                ('user_profile', models.ManyToManyField(to='Users.Profile')),
            ],
            options={
                'db_table': 'User',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
