from django.db import models
from django.utils.formats import number_format
from django.core.exceptions import ValidationError


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='Marca',
        error_messages={
            'unique': 'Esta marca já está cadastrada no sistema.'
        }
    )

    def __str__(self):
        return self.name

    def clean(self):
        if Brand.objects.filter(name__iexact=self.name).exists():
            raise ValidationError({'name': 'Esta marca já está cadastrada no sistema.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        self.name = self.name.title()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Car(models.Model):
    model = models.CharField(
        max_length=200,
        verbose_name='Modelo'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='car_brand',
        verbose_name='Marca'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Preço'
    )
    year_fabrication = models.IntegerField(
        verbose_name='Ano de Fabricação'
    )
    year_model = models.IntegerField(
        verbose_name='Ano do Modelo'
    )
    plate = models.CharField(
        max_length=10,
        verbose_name='Placa'
    )
    potency = models.IntegerField(
        verbose_name='Potência (CV)',
    )
    color = models.CharField(
        max_length=200,
        verbose_name='Cor',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )
    image = models.ImageField(
        upload_to='cars/',
        blank=True,
        null=True,
        verbose_name='Imagem'
    )

    def __str__(self):
        return self.model

    def formatted_price(self):
        return f"R$ {number_format(self.price, decimal_pos=2, use_l10n=True, force_grouping=True)}"

    def save(self, *args, **kwargs):
        self.plate = self.plate.upper()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'


class CarInventory(models.Model):
    cars_count = models.IntegerField(
        verbose_name='Quantidade de Carros'
    )
    cars_value = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Valor Total'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação'
    )

    def __str__(self):
        return f"{self.cars_count} - {self.cars_value}"

    class Meta:
        verbose_name = 'Inventário'
        verbose_name_plural = 'Inventários'
        ordering = ['-created_at']
