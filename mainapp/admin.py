from django.contrib import admin
from .models import *


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'passport_series', 'firstname', 'lastname', 'phone')


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'rent_cost')


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'cars', 'timestamp', 'from_date', 'to_date')


class Extended_ordersAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'extended_to')


admin.site.register(Clients, ClientsAdmin)
admin.site.register(Cars, CarsAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Extended_orders, Extended_ordersAdmin)



