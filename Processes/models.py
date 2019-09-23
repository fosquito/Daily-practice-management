from django.db import models

# Create your models here.


class Role(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    rolename = models.CharField(db_column='RoleName',
                                max_length=255,
                                blank=True,
                                null=True)
    product = models.ManyToManyField('Product')

    class Meta:
        managed = True
        db_table = 'Role'


class Activity(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    activityname = models.CharField(db_column='ActivityName',
                                    max_length=255,
                                    blank=True,
                                    null=True)
    processid = models.ForeignKey('Process',
                                  models.DO_NOTHING,
                                  db_column='ProcessID')
    descriçào = models.CharField(db_column='Descriçào',
                                 max_length=255,
                                 blank=True,
                                 null=True)
    pattern = models.ManyToManyField('Activities.Pattern')
    role = models.ManyToManyField('Role')
    data_creation = models.DateField(db_column='Data Creation', null=True)

    class Meta:
        managed = True
        db_table = 'Activity'


class Process(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    processname = models.CharField(db_column='ProcessName',
                                   max_length=255,
                                   blank=True,
                                   null=True)
    userid = models.ForeignKey('Users.User',
                               models.DO_NOTHING,
                               db_column='UserID')
    data_criação = models.DateField(db_column='Data Criação')
    descrição = models.CharField(db_column='Descrição',
                                 max_length=255)

    class Meta:
        managed = True
        db_table = 'Process'


class Product(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    productname = models.CharField(db_column='ProductName',
                                   max_length=255,
                                   blank=True,
                                   null=True)
    tipo = models.CharField(db_column='Tipo',
                            max_length=1)
    formato = models.CharField(db_column='Formato',
                               max_length=255)
    activity = models.ManyToManyField(Activity)

    class Meta:
        managed = True
        db_table = 'Product'
