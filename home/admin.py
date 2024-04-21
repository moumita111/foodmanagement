from django.contrib import admin
from .models import Ngo
from .models import Donation

admin.site.register([Ngo])
admin.site.register([Donation])