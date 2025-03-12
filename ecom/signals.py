from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from ecom.models import Car, CarInventory
from django.db.models import Sum
from gemini_api.client import get_gemini_client


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('price')
    )['total_value'] or 0

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )


@receiver(post_save, sender=Car)
def car_post_save(instance, sender, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(instance, sender, **kwargs):
    car_inventory_update()


@receiver(pre_save, sender=Car)
def car_pre_save(instance, sender, **kwargs):
    if not instance.description:
        description = get_gemini_client(
            instance.model,
            instance.brand,
            instance.year_model
        )
        if description:
            instance.description = description

