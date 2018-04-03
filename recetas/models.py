# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class CategoriaIngrediente(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORIA_INGREDIENTE'

    def __str__(self):
        return self.tnombre


class Alimento(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=50)  # Field name made lowercase.
    csabor = models.ForeignKey('Sabor', models.DO_NOTHING, db_column='cSabor', blank=True, null=True)  # Field name made lowercase.
    ctextura = models.ForeignKey('Textura', models.DO_NOTHING, db_column='cTextura', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALIMENTOS'
        ordering = ('tnombre', )
        
    def __str__(self):
        return self.tnombre



class IngredientesRecetas(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    cingredienteinfo = models.ForeignKey('IngredienteInfo', models.CASCADE, db_column='cIngredienteInfo')  # Field name made lowercase.
    crecetaparcial = models.ForeignKey('RecetasParciales', models.CASCADE, db_column='cRecetaParcial')  # Field name made lowercase.
    #cingredienteinfo = models.ManyToManyField('IngredienteInfo')
    #crecetaparcial = models.ManyToManyField('RecetasParciales')

    class Meta:
        managed = False
        db_table = 'INGREDIENTES_RECETAS'


class IngredienteInfo(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    calimento = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='cAlimento')  # Field name made lowercase.
    ctecnica = models.ForeignKey('Tecnica', models.DO_NOTHING, db_column='cTecnica')  # Field name made lowercase.
    ccorte = models.ForeignKey('TiposCorte', models.DO_NOTHING, db_column='cCorte')  # Field name made lowercase.
    ctipo = models.ForeignKey('TipoIngrediente', models.DO_NOTHING, db_column='cTipo')  # Field name made lowercase.
    ccategoria = models.ForeignKey(CategoriaIngrediente, models.DO_NOTHING, db_column='cCategoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INGREDIENTE_INFO'

    def __str__(self):
        ingrediente = (self.calimento, self.ctecnica, self.ccorte, self.ctipo, self.ccategoria)
        return ' '.join(str(part) for part in ingrediente if part is not None)

class RecetasParciales(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=45)  # Field name made lowercase.
    tdetalle = models.TextField(db_column='tDetalle', blank=True, null=True)  # Field name made lowercase.
    csabor = models.ForeignKey('Sabor', models.DO_NOTHING, db_column='cSabor', blank=True, null=True)  # Field name made lowercase.
    ctextura = models.ForeignKey('Textura', models.DO_NOTHING, db_column='cTextura', blank=True, null=True)  # Field name made lowercase.
    cingrediente = models.ManyToManyField(IngredienteInfo, through='IngredientesRecetas', blank=True)
    lacomp = models.IntegerField(db_column='lAcomp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECETAS_PARCIALES'

    def __str__(self):
        return self.tnombre

class RecetasCompuestas(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=45)  # Field name made lowercase.
    tdetalle = models.TextField(db_column='tDetalle', blank=True, null=True)  # Field name made lowercase.
    csabor = models.ForeignKey('Sabor', models.DO_NOTHING, db_column='cSabor', blank=True, null=True)  # Field name made lowercase.
    ctextura = models.ForeignKey('Textura', models.DO_NOTHING, db_column='cTextura', blank=True, null=True)  # Field name made lowercase.
    crecetasparciales = models.ManyToManyField(RecetasParciales, through='RparcialesRcompuestas', blank=True)

    class Meta:
        managed = False
        db_table = 'RECETAS_COMPUESTAS'

class RparcialesRcompuestas(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    crecetaparcial = models.ForeignKey(RecetasParciales, models.CASCADE, db_column='cRecetaParcial')  # Field name made lowercase.
    crecetacompuesta = models.ForeignKey(RecetasCompuestas, models.CASCADE, db_column='cRecetaCompuesta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RPARCIALES_RCOMPUESTAS'


class Sabor(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SABORES'
        verbose_name_plural = 'sabores'
        ordering = ('tnombre', )
        
    def __str__(self):
        return self.tnombre


class Tecnica(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TECNICAS'
        verbose_name = 'técnica'
        verbose_name_plural = 'técnicas'
        ordering = ('tnombre', )

    def __str__(self):
        return self.tnombre


class Textura(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TEXTURAS'
        ordering = ('tnombre', )
        
    def __str__(self):
        return self.tnombre


class TiposCorte(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPOS_CORTE'
        ordering = ('tnombre', )
        
    def __str__(self):
        return self.tnombre


class TipoIngrediente(models.Model):
    cid = models.AutoField(db_column='cId', primary_key=True)  # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_INGREDIENTE'
        ordering = ('tnombre', )
        
    def __str__(self):
        return self.tnombre


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
