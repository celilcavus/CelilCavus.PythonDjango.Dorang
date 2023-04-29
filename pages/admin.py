from django.contrib import admin
from .models import Cards,Journal,ContactUs

# Register your models here.

#======== Card

class CardAdmin(admin.ModelAdmin):
    list_display = ('id','Title')

admin.site.register(Cards,CardAdmin)

#======== Journal
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id','Title')

admin.site.register(Journal,JournalAdmin)

#======== ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','description')

admin.site.register(ContactUs,ContactUsAdmin)