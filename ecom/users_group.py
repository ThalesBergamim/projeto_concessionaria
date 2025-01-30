from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from ecom.models import Car, Brand

def create_groups(apps, schema_editor):
    # Criar grupo de usuários
    user_group, created = Group.objects.get_or_create(name='Usuario')
    
    # Criar grupo de gerentes
    manager_group, created = Group.objects.get_or_create(name='Gerente')
    
    # Obter content types
    car_content_type = ContentType.objects.get_for_model(Car)
    brand_content_type = ContentType.objects.get_for_model(Brand)
    
    # Definir permissões para usuários normais
    view_car = Permission.objects.get(content_type=car_content_type, codename='view_car')
    user_group.permissions.add(view_car)
    
    # Definir permissões para gerentes (todas as permissões)
    manager_permissions = Permission.objects.filter(
        content_type__in=[car_content_type, brand_content_type]
    )
    manager_group.permissions.set(manager_permissions)

class Migration(migrations.Migration):
    dependencies = [
        ('ecom', 'sua_ultima_migration'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]