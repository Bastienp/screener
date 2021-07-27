from django.contrib import admin

from .models import Kline
from .models import Pair
from .models import Interval

admin.site.register(Pair)
admin.site.register(Interval)
admin.site.register(Kline)