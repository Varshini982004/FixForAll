from django.contrib import admin
from .models import Complaint


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'user',
        'issue_type',
        'location',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'issue_type',
        'created_at',
    )

    search_fields = (
        'title',
        'description',
        'location',
        'user__username',
    )

    list_editable = (
        'status',
    )

    ordering = (
        '-created_at',
    )
