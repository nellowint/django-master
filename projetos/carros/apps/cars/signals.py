
import os

from django.db.models import Sum
from django.db.models.signals import post_delete, post_save, pre_save
from django.dispatch import receiver

from .models import Car, CarInventory


def update_inventory():
    result = Car.objects.filter(is_active=True).aggregate(
        total_amount=Sum('id'),
        total_value=Sum('price')
    )

    amount = Car.objects.filter(is_active=True).count()
    value = result['total_value'] or 0
    CarInventory.objects.create(amount=amount, value=value)


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    update_inventory()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    update_inventory()
    if instance.image and instance.image.name:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_car = Car.objects.get(pk=instance.pk)
    except Car.DoesNotExist:
        return False

    old_image = old_car.image
    new_image = instance.image

    if old_image and old_image != new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)

    if not instance.desc:
        """
            Pode gerar uma função com uso de IA para descrições
        """
        instance.desc = 'Descrição gerada automaticamente...'
