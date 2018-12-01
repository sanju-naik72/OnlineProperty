from django.contrib import admin

from .models import State
from .models import City
from .models import Locality
from .models import Sales
from .models import Suggestion
from .models import Property_name

admin.site.register(State)
admin.site.register(City)
admin.site.register(Locality)
admin.site.register(Sales)
admin.site.register(Suggestion)
admin.site.register(Property_name)
