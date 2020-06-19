from django.contrib import admin

from .models import LandingPage, Offer, PageType, PaywallOffer, Property
import nested_admin

class PaywallOfferInline(nested_admin.NestedStackedInline):
    model = PaywallOffer
    max_num = 1


class OfferInline(nested_admin.NestedStackedInline):
    model = Offer
    max_num = 2


class PageTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ('name',)
    search_fields = ['name']


class LandingPageAdmin(nested_admin.NestedModelAdmin):
    list_display = ('name', 'property', 'pageType')
    list_filter = ('name', 'property', 'pageType')
    inlines = [PaywallOfferInline, OfferInline]
    autocomplete_fields = ['pageType']
   

# Register your models here.
admin.site.register(Property)
admin.site.register(PageType, PageTypeAdmin)
admin.site.register(LandingPage, LandingPageAdmin)
