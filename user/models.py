from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Test(models.Model):
    town_name = models.CharField(unique=True, max_length=20)
    class Meta:
        ordering = ["town_name"]
    def __str__(self):
        return self.town_name
class Town(models.Model):
    town_name = models.CharField(unique=True, max_length=20)
    class Meta:
        ordering = ["town_name"]
    def __str__(self):
        return self.town_name
class Street(models.Model):
    street_name = models.CharField(unique=True, max_length=50)
    town = models.ForeignKey(Town, on_delete = models.CASCADE, to_field = "town_name", related_name='+')
    class Meta:
        ordering = ["street_name"]
    def __str__(self):
        return self.street_name
class House(models.Model):
    number = models.CharField(unique=True, max_length=5)
    street = models.ForeignKey(Street, on_delete = models.CASCADE, to_field = "street_name", related_name='+')
    class Meta:
        ordering = ["number"]
    def __str__(self):
        return self.number

class Privelege(models.Model):
    privelege = models.CharField(max_length=20, verbose_name='Пільга')
    limit = models.IntegerField(verbose_name='Ліміт пільг.споживання')
    limit_price = models.FloatField(verbose_name = "пільгова ціна")
    price = models.FloatField(verbose_name = "ціна")
    class Meta:
        ordering = ["id"]
    def __str__(self):
        template = '{0.privelege}'
        return template.format(self)

class Private_abonent(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE, to_field = "username", primary_key=True, verbose_name='О/Р')
    first_name = models.CharField(max_length=20, verbose_name='Ім\'я')
    last_name = models.CharField(max_length=20, verbose_name='Побатькові')
    sur_name = models.CharField(max_length=30, verbose_name='Прізвище')
    house_number = models.ForeignKey(House, on_delete = models.CASCADE, related_name='+', to_field = "number", verbose_name='Будинок')
    apartament = models.IntegerField(null=True, default=0, verbose_name='Квартира')
    meter_sn = models.CharField(max_length=20, null=True, blank = True, verbose_name='Лічильник №:')
    phone_num = models.CharField(max_length=13, null=True, blank = True, verbose_name='Ном.телефону')
    email = models.EmailField(max_length=100, null=True, blank = True, verbose_name='Ел. поштова скринька')
    tariff = models.ForeignKey(Privelege, on_delete=models.CASCADE, default=1, verbose_name='Тариф')
    class Meta:
        ordering = ["account"]
    def __str__(self):
        template = '{0.account} {0.sur_name} {0.house_number.street} {0.house_number.number}'
        return template.format(self)


class Comercial(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE)
    contract=models.CharField(max_length=100, verbose_name='О/Р', primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Споживач')
    ipn = models.CharField(max_length=20, verbose_name='ІПН', null=True)
    meter_sn = models.CharField(max_length=20, null=True, blank = True, verbose_name='Лічильник №:')
    phone_num = models.CharField(max_length=13, null=True, blank = True, verbose_name='Ном.телефону')
    email = models.EmailField(max_length=100, null=True, blank = True, verbose_name='Ел. поштова скринька')
    class Meta:
        ordering = ["account"]
    def __str__(self):
        template = '{0.account} {0.contract} {0.name} {0.ipn} {0.meter_sn} {0.phone_num} {0.email}'
        return template.format(self)
        # return str(self.account), str(self.sur_name), str(self.house_number.street), str(self.house_number.number)

class balans(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, to_field = "username")
    saldo = models.FloatField(verbose_name = "saldo", default=0)
    comment = models.CharField(max_length=100, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    class Meta:
        ordering = ["-date"]
    def __str__(self):
        template = '{0.account} {0.saldo} {0.date} {0.comment}'
        return template.format(self)

class spozHistory(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, to_field = "username")
    date = models.DateField(verbose_name = "місяць", auto_now=False, auto_now_add=False)
    pokaz1 = models.FloatField(verbose_name = "поч.показник", default=0)
    pokaz2 = models.FloatField(verbose_name = "кін.показник", default=0)
    different = models.FloatField(verbose_name = "спожито кВт", default=0)
    uah = models.FloatField(verbose_name = "грн", default=0)

    class Meta:
        ordering = ["-date"]
    def __str__(self):
        template = '{0.account} {0.date} {0.pokaz1} {0.pokaz2} {0.different} {0.uah}'
        return template.format(self)
        # return self.account, self.saldo, self.date, self.comment
class meterDataPrivate(models.Model):
    account = models.ForeignKey(Private_abonent, on_delete=models.CASCADE)
    pokazT0 = models.FloatField(verbose_name = "показник", default='0.0')
    pokazT1 = models.FloatField(verbose_name = "показник", default='0.0')
    pokazT2 = models.FloatField(verbose_name = "показник", default='0.0')
    pokazT3 = models.FloatField(verbose_name = "показник", default='0.0')
    date = models.DateField(verbose_name = "Дата", auto_now=False, auto_now_add=False)
    comment = models.CharField(max_length=100, null=True, verbose_name='Джерело')
    class Meta:
        ordering = ["-date"]
    def __str__(self):
        template = '{0.date} {0.pokaz}'
        return template.format(self)
        # return self.account, self.saldo, self.date, self.comment

class gadget_hw(models.Model):
    contract = models.ForeignKey(Comercial, on_delete=models.CASCADE, to_field = "contract")
    model = models.CharField(max_length=50, null=True)
    class Meta:
        ordering = ["id"]
    def __str__(self):
        template = '{0.id} {0.model}'
        return template.format(self)

class gadget_HW_meter(models.Model):
    kWh = models.FloatField(verbose_name = "кВт", default=0)
    kVArh_p = models.FloatField(verbose_name = "кВар поз.", default=0)
    kVArh_n = models.FloatField(verbose_name = "кВар нег.", default=0)
    kVAh = models.FloatField(verbose_name = "кВА", default=0)
    cur_sum_V = models.FloatField(verbose_name = "В", default=0)
    cur_L1_V = models.FloatField(verbose_name = "В Ф1", default=0)
    cur_L2_V = models.FloatField(verbose_name = "В Ф2", default=0)
    cur_L3_V = models.FloatField(verbose_name = "В Ф3", default=0)
    cur_F = models.FloatField(verbose_name = "Частота", default=0)
    meterDate = models.BigIntegerField(verbose_name = "Дата", default=0)
    gadget_HW_id = models.ForeignKey(gadget_hw, on_delete=models.CASCADE, verbose_name = "№ пристрою")
    class Meta:
        ordering = ["meterDate"]
    def __str__(self):
        template = '{0.kWh} {0.kVArh_p} {0.kVArh_n} {0.kVAh} {0.cur_sum_V} {0.cur_L1_V} {0.cur_L2_V} {0.cur_L3_V} {0.cur_F} {0.meterDate}'
        return template.format(self)

class gadget_HW_meter_max_dem_h(models.Model):
    kW = models.FloatField(verbose_name = "макс.кВт", default=0)
    meterDate = models.BigIntegerField(verbose_name = "Дата", default=0)
    gadget_HW_id = models.ForeignKey(gadget_hw, on_delete=models.CASCADE, verbose_name = "№ пристрою")
    class Meta:
        ordering = ["meterDate"]
    def __str__(self):
        template = '{0.kW} {0.meterDate}'
        return template.format(self)
