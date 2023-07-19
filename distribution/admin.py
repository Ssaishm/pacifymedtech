from django.contrib import admin
from .models import disContact

#############################
@admin.register(disContact)
class disContactAdmin(admin.ModelAdmin):
    list_display =( 'id','personalname','personalemail','personalphone','companyname','companyemail','companyurl','companycity','companystate','companyzipcode','companyaddress','designation','industry','years','question','speciality')