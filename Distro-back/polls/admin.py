
from django.contrib import admin


from polls.models import *

class FeaturesAdmin(admin.ModelAdmin):
    list_display = ("name", "description","language")
class TranslationAdmin(admin.ModelAdmin):
    list_display = ("page_name", "key","value","language")
class linksAdmin(admin.ModelAdmin):
    list_display = ("name", "link","language")
class DistroAdmin(admin.ModelAdmin):
    list_display = ("name", "Desk","link")
# Register your models here.

admin.site.register(Translation,TranslationAdmin)
admin.site.register(links,linksAdmin)
admin.site.register(Distro,DistroAdmin)
admin.site.register(Features,FeaturesAdmin)

