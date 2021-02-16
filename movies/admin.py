from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Shot)
admin.site.register(Movie)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Review)