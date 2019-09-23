from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Permission(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    permissionname = models.CharField(db_column='PermissionName',
                                      max_length=255,
                                      blank=True,
                                      null=True)
    permissionactive = models.TextField(db_column='PermissionActive')
    create = models.TextField(db_column='Create')
    read = models.TextField(db_column='Read')
    update = models.TextField(db_column='Update')
    delete = models.TextField(db_column='Delete')
    read_others = models.TextField(db_column='Read_others')
    update_others = models.TextField(db_column='Update_others')

    class Meta:
        managed = True
        db_table = 'Permission'


class Profile(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    profilename = models.CharField(db_column='ProfileName',
                                   max_length=255,
                                   blank=True,
                                   null=True)
    active = models.TextField(db_column='Active')
    userid = models.IntegerField(db_column='UserID')
    permission = models.ManyToManyField('Permission')

    class Meta:
        managed = True
        db_table = 'Profile'


class Organization(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    organizationname = models.CharField(db_column='OrganizationName',
                                        max_length=255,
                                        blank=True,
                                        null=True)
    organizationlocation = models.CharField(db_column='OrganizationLocation',
                                            max_length=255,
                                            blank=True,
                                            null=True)

    class Meta:
        managed = True
        db_table = 'Organization'

    def __str__(self):
        return self.organizationname


class User(AbstractUser):
    id = models.AutoField(db_column='ID', primary_key=True)

    organizationid = models.ForeignKey(Organization,
                                       models.CASCADE,
                                       null=True,
                                       db_column='OrganizationID')
    user_profile = models.ManyToManyField('Profile')
    username = models.CharField(db_column='UserName',
                                max_length=255,
                                unique=True,
                                blank=True,
                                null=True)
    useremail = models.CharField(db_column='UserEmail',
                                 max_length=255,
                                 blank=True,
                                 null=True)
    password = models.CharField(db_column='Password',
                                max_length=255,
                                blank=True,
                                null=True)
    userrole = models.CharField(db_column='UserRole',
                                max_length=255,
                                blank=True,
                                null=True)
    active = models.TextField(db_column='Active')

    class Meta:
        managed = True
        db_table = 'User'
