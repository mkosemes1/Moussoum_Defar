from django.contrib import admin
from .models import Client, Subscription


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'company_name', 'plan', 'monthly_evaluations',
        'max_evaluations', 'is_verified', 'created_at'
    ]
    list_filter = ['plan', 'is_verified']
    search_fields = ['user__username', 'user__email', 'company_name']
    readonly_fields = ['monthly_evaluations']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        'client', 'plan', 'status', 'monthly_price',
        'max_evaluations', 'starts_at', 'ends_at'
    ]
    list_filter = ['plan', 'status']
    search_fields = ['client__company_name']
    readonly_fields = ['starts_at']
