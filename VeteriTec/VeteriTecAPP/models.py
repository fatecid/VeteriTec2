# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agenda(models.Model):
    idvet = models.IntegerField()
    cliente = models.CharField(max_length=30, blank=True, null=True)
    idanimal = models.IntegerField()
    tipo = models.CharField(max_length=20, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    termino = models.TimeField(blank=True, null=True)
    comparecimento = models.IntegerField()
    obs = models.CharField(max_length=1000, blank=True, null=True)
    descricao = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agenda'


class Animal(models.Model):
    idanimal = models.AutoField(primary_key=True)
    idclie = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=30, blank=True, null=True)
    especie = models.CharField(max_length=30, blank=True, null=True)
    raca = models.CharField(max_length=30, blank=True, null=True)
    sexo = models.CharField(max_length=18, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    castrado = models.CharField(max_length=20, blank=True, null=True)
    cor = models.CharField(max_length=40, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    obs = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animal'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


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
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Cliente(models.Model):
    data = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    sexo = models.CharField(max_length=9, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    rua = models.CharField(max_length=60, blank=True, null=True)
    numero = models.CharField(max_length=6, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    celular = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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


class Ficha(models.Model):
    idficha = models.AutoField(primary_key=True)
    idanimal = models.IntegerField()
    idvacina = models.IntegerField()
    idfunc = models.IntegerField()
    data = models.DateField(blank=True, null=True)
    peso = models.FloatField(blank=True, null=True)
    diagnostico = models.CharField(max_length=5000, blank=True, null=True)
    historico = models.CharField(max_length=9000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha'


class Fornecedor(models.Model):
    data = models.DateField(blank=True, null=True)
    nome = models.CharField(max_length=50, blank=True, null=True)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    contato = models.CharField(max_length=30, blank=True, null=True)
    telefone = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fornecedor'


class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(unique=True, max_length=18, blank=True, null=True)
    funcao = models.CharField(max_length=30, blank=True, null=True)
    crmv = models.CharField(max_length=30, blank=True, null=True)
    validade = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=10, blank=True, null=True)
    nascimento = models.DateField(blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    rua = models.CharField(max_length=60, blank=True, null=True)
    numero = models.IntegerField(blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funcionario'


class Pessoas(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pessoas'


class Receita(models.Model):
    texto = models.CharField(max_length=300, blank=True, null=True)
    pat = models.CharField(max_length=50, blank=True, null=True)
    vet = models.CharField(max_length=50, blank=True, null=True)
    retorno = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'receita'


class Vacina(models.Model):
    idvacina = models.AutoField(primary_key=True)
    idanimal = models.IntegerField(blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    vacina = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacina'
