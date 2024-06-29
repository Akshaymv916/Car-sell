from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Brand)
admin.site.register(Fueltype)
admin.site.register(Color)
admin.site.register(Car_details)
admin.site.register(call_request)
admin.site.register(Car_sell)
