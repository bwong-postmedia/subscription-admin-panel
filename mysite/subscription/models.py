from django.db import models

from ckeditor.fields import RichTextField


class Property(models.Model):
    name = models.CharField('Property name', max_length=120)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Properties"


class PageType(models.Model):
    name = models.CharField('Name', max_length=120)
    code = models.CharField('Campaign code', max_length=30, blank=True, default="")

    def __str__(self):
        return self.name


class LandingPage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True)
    pageType = models.ForeignKey(PageType, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Page name', max_length=120)
    heading = models.CharField('Page heading', max_length=120)
    micetype = RichTextField('Mice type', blank=True, default="")
    
    def __str__(self):
        return self.name


class PaywallOffer(models.Model):
    landingPage = models.ForeignKey(LandingPage, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Offer name', max_length=120)
    offerID = models.CharField('Offer ID', max_length=10)
    monthlyStrikePrice = models.DecimalField(
        'Monthly strike price',
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=None
    )
    monthlyPrice = models.DecimalField('Monthly price', max_digits=5, decimal_places=2)
    monthlyTermID = models.CharField('Monthly term ID', max_length=10)
    annualStrikePrice = models.DecimalField(
        'Monthly strike price',
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=None
    )
    annualPrice = models.DecimalField('Annual price', max_digits=5, decimal_places=2)
    annualTermID = models.CharField('Annual term ID', max_length=10)

    def __str__(self):
        return self.name


class Offer(models.Model):
    TERM = [
        ('FW', '4 week'),
        ('MO', 'Month')
    ]

    TYPES = [
        ('DA', 'Daily'),
        ('WK', 'Weekend')
    ]

    landingPage = models.ForeignKey(LandingPage, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Offer group name', max_length=120)
    deliveryType = models.CharField('Type', max_length=2, choices=TYPES, default='DA')
    monthlyName = models.CharField('Monthly offer name', max_length=120)
    monthlyStrikePrice = models.DecimalField(
        'Monthly strike price',
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=None
    )
    monthlyPrice = models.DecimalField('Monthly price', max_digits=5, decimal_places=2)
    monthlyTerm = models.CharField('Monthly term', max_length=2, choices=TERM, default='MO')
    annualName = models.CharField('Annual offer name', max_length=120)
    annualStrikePrice = models.DecimalField(
        'Annual strike price',
        max_digits=5,
        decimal_places=2,
        blank=True,
        default=None
    )
    annualPrice = models.DecimalField('Annual price', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
