from django.contrib import admin
from .models import UserCard,HeadStaff,ArtistCard,Staff,FreeFireTeam

# Register your models here.
class UserCardAdmin(admin.ModelAdmin):
    list_display = ['name', 'friendly', 'active_voice_channel', 'active_message', 'moderator', 'ticket_manager', 'manager']
    list_filter = ['friendly', 'active_voice_channel', 'active_message', 'moderator', 'ticket_manager', 'manager']
    search_fields = ['name']
    
admin.site.register(UserCard)

class HeadStaffAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'role',
        'friendly',
        'active_voice_channel',
        'active_message',
        'moderator',
        'ticket_manager',
        'manager',
        'created_at',
    )

    list_filter = (
        'role',
        'friendly',
        'active_voice_channel',
        'active_message',
        'moderator',
        'ticket_manager',
        'manager',
    )

    search_fields = ('name',)
    ordering = ('-created_at',)

    
admin.site.register(HeadStaff)

from django.contrib import admin
from .models import ArtistCard

class ArtistCardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'artist_tag',  # NEW: show Artist Tag
        'friendly',
        'active_voice_channel',
        'active_message',
        'moderator',
        'ticket_manager',
        'manager',
        'created_at',
    )

    list_filter = (
        'artist_tag',  # NEW: filter by Artist Tag
        'friendly',
        'active_voice_channel',
        'active_message',
        'moderator',
        'ticket_manager',
        'manager',
    )

    search_fields = ('name', 'artist_tag')  # NEW: search by Artist Tag
    ordering = ('-created_at',)

admin.site.register(ArtistCard, ArtistCardAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'staff',  
        'friendly',
        'active_voice_channel',
        'active_message',
        'moderator',
        'ticket_manager',
        'manager',
        'created_at',
    )

    list_filter = (
        'staff',  
        'friendly',
        'active_voice_channel',
        'active_message',
        'moderator',
        'ticket_manager',
        'manager',
    )

    search_fields = ('name',)
    ordering = ('-created_at',)

# Register the admin
admin.site.register(Staff, StaffAdmin)
class FreeFireTeamAdmin(admin.ModelAdmin):
    list_display = ("admin_head", "guild_id")
    readonly_fields = ("guild_id",)

    fieldsets = (
        ("Leadership", {
            "fields": ("admin_head", "team_elders", "team_members")
        }),
        ("Guild Info", {
            "fields": ("guild_id",)
        }),
    )


admin.site.register(FreeFireTeam, FreeFireTeamAdmin)