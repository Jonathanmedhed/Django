from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    #to displayinfo
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') 
    #to make them clickable
    list_display_links = ('id', 'title') 
    #To add filters
    list_filter = ('realtor',) 
    #Make a field editable
    list_editable= ('is_published',)
    #Add search field
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    #amount per page
    list_per_page= 25

admin.site.register(Listing, ListingAdmin)
