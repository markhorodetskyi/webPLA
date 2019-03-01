from django.contrib import admin
from .models import Town, Street, House, Private_abonent, balans, Privelege, spozHistory, Comercial, gadget_hw, gadget_HW_meter, gadget_HW_meter_max_dem_h

# Register your models here.
# admin.site.register(Town)
class Town_Model(admin.ModelAdmin):
     list_display = ('town_name', 'id')
admin.site.register(Town, Town_Model)
admin.site.register(Street)
admin.site.register(House)

class Private_abonent_Model(admin.ModelAdmin):
     list_display = ('account', 'first_name', 'last_name',  'sur_name',  'house_number',  'meter_sn',  'phone_num',  'email', 'tariff')
     search_fields = ['account_id']
admin.site.register(Private_abonent, Private_abonent_Model)
admin.site.register(balans)

class Privelege_Model(admin.ModelAdmin):
     list_display = ('id', 'privelege', 'limit', 'limit_price',  'price')
admin.site.register(Privelege, Privelege_Model)

class spozHistory_Model(admin.ModelAdmin):
     list_display = ('account', 'date', 'pokaz1',  'pokaz2',  'different',  'uah')
     search_fields = ['account']
admin.site.register(spozHistory, spozHistory_Model)

class comercial_Model(admin.ModelAdmin):
     list_display = ('contract', 'name', 'ipn',  'meter_sn',  'phone_num',  'email')
     search_fields = ['contract']
admin.site.register(Comercial, comercial_Model)

class gadget_hw_Model(admin.ModelAdmin):
     list_display = ('id', 'contract', 'model')
     search_fields = ['contract']
admin.site.register(gadget_hw, gadget_hw_Model)

class gadget_HW_meter_Model(admin.ModelAdmin):
     list_display = ('kWh', 'kVArh_p', 'kVArh_n', 'kVAh', 'cur_sum_V', 'cur_L1_V', 'cur_L2_V', 'cur_L3_V', 'cur_F', 'meterDate', 'gadget_HW_id')
     search_fields = ['gadget_HW_id']
admin.site.register(gadget_HW_meter, gadget_HW_meter_Model)

class gadget_HW_meter_max_dem_h_Model(admin.ModelAdmin):
     list_display = ('kW', 'meterDate', "gadget_HW_id")
     search_fields = ['gadget_HW_id']
admin.site.register(gadget_HW_meter_max_dem_h, gadget_HW_meter_max_dem_h_Model)
