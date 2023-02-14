from django.contrib import admin
from .models import CustomerAccount
from .models import Employee
from .models import ReservationRecord
from .models import OrderRecord
from .models import MenuRecord
from .models import ResturantSeats
from .models import ResturantTable

# Register your models here.
admin.site.register(CustomerAccount)
admin.site.register(Employee)
admin.site.register(ReservationRecord)
admin.site.register(OrderRecord)
admin.site.register(MenuRecord)
admin.site.register(ResturantSeats)
admin.site.register(ResturantTable)