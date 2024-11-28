from django.contrib import admin
from .models import FAQ, Keyword

class KeywordInline(admin.TabularInline):
    model = Keyword
    extra = 1

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    inlines = [KeywordInline]
