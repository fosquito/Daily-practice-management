# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activityname = models.CharField(db_column='ActivityName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    processid = models.ForeignKey('Process', models.DO_NOTHING, db_column='ProcessID')  # Field name made lowercase.
    descriçào = models.CharField(db_column='Descriçào', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activity'


class ActivityPattern(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patternid = models.ForeignKey('Pattern', models.DO_NOTHING, db_column='PatternID')  # Field name made lowercase.
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='ActivityID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activity-Pattern'


class ActivityRole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='ActivityID')  # Field name made lowercase.
    roleid = models.ForeignKey('Role', models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activity-Role'


class Group(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group'


class GroupPattern(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    patternid = models.ForeignKey('Pattern', models.DO_NOTHING, db_column='PatternID')  # Field name made lowercase.
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='GroupID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group-Pattern'


class GroupTags(models.Model):
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='GroupID', primary_key=True)  # Field name made lowercase.
    tagsid = models.ForeignKey('Tags', models.DO_NOTHING, db_column='TagsID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Group_Tags'
        unique_together = (('groupid', 'tagsid'),)


class Organization(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    organizationname = models.CharField(db_column='OrganizationName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    organizationlocation = models.CharField(db_column='OrganizationLocation', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organization'


class Pattern(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    patternname = models.CharField(db_column='PatternName', max_length=255)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    data_creation = models.DateField(db_column='Data Creation')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Pattern'


class Permission(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    permissionname = models.CharField(db_column='PermissionName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    permissionactive = models.TextField(db_column='PermissionActive')  # Field name made lowercase. This field type is a guess.
    create = models.TextField(db_column='Create')  # Field name made lowercase. This field type is a guess.
    read = models.TextField(db_column='Read')  # Field name made lowercase. This field type is a guess.
    update = models.TextField(db_column='Update')  # Field name made lowercase. This field type is a guess.
    delete = models.TextField(db_column='Delete')  # Field name made lowercase. This field type is a guess.
    read_others = models.TextField(db_column='Read_others')  # Field name made lowercase. This field type is a guess.
    update_others = models.TextField(db_column='Update_others')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Permission'


class Process(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    processname = models.CharField(db_column='ProcessName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    data_criação = models.DateField(db_column='Data Criação')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descrição = models.CharField(db_column='Descrição', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Process'


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=1)  # Field name made lowercase.
    formato = models.CharField(db_column='Formato', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class ProductActivity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activityid = models.ForeignKey(Activity, models.DO_NOTHING, db_column='ActivityID')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product-Activity'


class Profile(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    profilename = models.CharField(db_column='ProfileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.
    userid = models.IntegerField(db_column='UserID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Profile'


class ProfilePermission(models.Model):
    profileid = models.ForeignKey(Profile, models.DO_NOTHING, db_column='ProfileID', primary_key=True)  # Field name made lowercase.
    permissionid = models.ForeignKey(Permission, models.DO_NOTHING, db_column='PermissionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Profile_Permission'
        unique_together = (('profileid', 'permissionid'),)


class Role(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Role'


class RoleProduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    roleid = models.ForeignKey(Role, models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Role-Product'


class Sentence(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    sentencename = models.CharField(db_column='SentenceName', max_length=255)  # Field name made lowercase.
    datecreated = models.DateField(db_column='DateCreated')  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=255)  # Field name made lowercase.
    receiver = models.CharField(db_column='Receiver', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datarealizado = models.DateField(db_column='DataRealizado')  # Field name made lowercase.
    artefacto = models.CharField(db_column='Artefacto', max_length=255)  # Field name made lowercase.
    verbid = models.ForeignKey('Verb', models.DO_NOTHING, db_column='VerbID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sentence'


class SentenceGroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='GroupID')  # Field name made lowercase.
    sentenceid = models.ForeignKey(Sentence, models.DO_NOTHING, db_column='SentenceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sentence-Group'


class Tags(models.Model):
    name = models.IntegerField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tags'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    organizationid = models.ForeignKey(Organization, models.DO_NOTHING, db_column='OrganizationID')  # Field name made lowercase.
    profileid = models.ForeignKey(Profile, models.DO_NOTHING, db_column='ProfileID')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='UserEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userrole = models.CharField(db_column='UserRole', max_length=255, blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(db_column='Active')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'User'


class Verb(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    verbname = models.CharField(db_column='VerbName', unique=True, max_length=255)  # Field name made lowercase.
    verbtype = models.CharField(db_column='VerbType', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Verb'
