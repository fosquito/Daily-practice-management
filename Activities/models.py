from django.db import models

# Create your models here.


class Tags(models.Model):
    name = models.IntegerField(db_column='Name',
                               blank=True,
                               null=True)
    id = models.AutoField(db_column='ID',
                          primary_key=True)

    class Meta:
        managed = True
        db_table = 'Tags'


class Pattern(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    userid = models.ForeignKey('Users.User',
                               models.DO_NOTHING,
                               db_column='UserID')
    patternname = models.CharField(db_column='PatternName',
                                   max_length=255,
                                   verbose_name='Padrão')
    image = models.TextField(db_column='Image',
                             blank=True,
                             null=True)
    description = models.CharField(db_column='Description',
                                   max_length=255)
    data_creation = models.DateField(db_column='Data Creation', null=True)
    groups = models.ManyToManyField('Group')

    class Meta:
        managed = True
        db_table = 'Pattern'


class Group(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    userid = models.ForeignKey('Users.User',
                               models.DO_NOTHING,
                               null=True,
                               db_column='UserID')
    groupname = models.CharField(db_column='GroupName',
                                 unique=True,
                                 max_length=255,
                                 verbose_name='Agrupamento')
    creationdate = models.DateField(db_column='CreationDate',
                                    blank=True,
                                    null=True)
    name = models.CharField(db_column='Name',
                            max_length=255)
    description = models.CharField(db_column='Description',
                                   max_length=255)

    tags = models.ManyToManyField('Tags')

    sentences = models.ManyToManyField('Sentence')

    class Meta:
        managed = True
        db_table = 'Group'
    def __str__(self):
        return self.groupname


class Sentence(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    userid = models.ForeignKey('Users.User',
                               models.DO_NOTHING,
                               db_column='UserID')
    sentencename = models.CharField(db_column='SentenceName',
                                    max_length=255,
                                    verbose_name="Frase")
    datecreated = models.DateField(db_column='DateCreated', null=True)
    subject = models.CharField(db_column='Subject',
                               max_length=255,
                               verbose_name="Sujeito")
    receiver = models.CharField(db_column='Receiver',
                                max_length=255,
                                blank=True,
                                null=False,
                                verbose_name="Recetor")
    datarealizado = models.DateField(db_column='DataRealizado',blank=True, null=True)
    verbid = models.ForeignKey('Verb',
                               models.DO_NOTHING,
                               db_column='VerbID',
                               verbose_name="Verbo")
    resourceid = models.ForeignKey('Resource',
                               models.DO_NOTHING,
                               db_column='ResourceID',
                               verbose_name="Recurso",
                               null=True, blank=True)
    artefactid = models.ForeignKey('Artefact',
                               models.DO_NOTHING,
                               db_column='ArtefactID',
                               verbose_name="Artefacto",
                               null=True, blank=True) 


    class Meta:
        managed = True
        db_table = 'Sentence'
    def __str__(self):
        return self.sentencename


class Verb(models.Model):
    verb_type_choices = (('Produtivo','Produtivo'),
                         ('Comunicativo','Comunicativo'))
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    verbname = models.CharField(db_column='VerbName',
                                unique=True,
                                max_length=255,
                                verbose_name='Verbo')
    verbtype = models.CharField(db_column='VerbType',
                                max_length=255,
                                choices=verb_type_choices,
                                verbose_name='Tipo')

    class Meta:
        managed = True
        db_table = 'Verb'
    def __str__(self):
        return self.verbname
        
        
        
class Resource(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    resourcename = models.CharField(db_column='ResourceName',
                                unique=True,
                                max_length=255,
                                verbose_name='Recurso')
    datecreated = models.DateField(db_column='DateCreated')

    class Meta:
        managed = True
        db_table = 'Resource'
    def __str__(self):
        return self.resourcename
 
 
class Artefact(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True)
    artefactname = models.CharField(db_column='ArtefactName',
                                unique=True,
                                max_length=255,
                                verbose_name='Artefacto')
    datecreated = models.DateField(db_column='DateCreated')

    class Meta:
        managed = True
        db_table = 'Artefacto'
    def __str__(self):
        return self.artefactname
       
