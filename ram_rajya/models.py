from django.db import models

# Create your models here.
class UserCard(models.Model):
    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profiles/')
    banner_image = models.ImageField(upload_to='banners/')

    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('chief', 'Chief'),
        ('high_court', 'High Court'),
        ('member', 'Member'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='member'
    )

    # Tags as checkboxes
    friendly = models.BooleanField(default=False)
    active_voice_channel = models.BooleanField(default=False)
    active_message = models.BooleanField(default=False)
    moderator = models.BooleanField(default=False)
    ticket_manager = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'User_Card'
        
# HEAD SATFF

class HeadStaff(models.Model):
    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profiles/')  #
    banner_image = models.ImageField(upload_to='banners/')    

    
    ROLE_CHOICES = [
        ('headstaff', 'HeadStaff'),
        ('girlowner', 'GirlOwner'),
        ('member', 'Member'),  
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

    friendly = models.BooleanField(default=False)
    active_voice_channel = models.BooleanField(default=False)
    active_message = models.BooleanField(default=False)
    moderator = models.BooleanField(default=False)
    ticket_manager = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Head_Staff'
        
class HeadStaff(models.Model):

    ROLE_CHOICES = [
        ('headstaff', 'Head Staff'),
        ('girlowner', 'Girl Owner'),
        ('girlmanager', 'Girl Manager'),
        ('member', 'Member'),
    ]

    name = models.CharField(max_length=200)

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    banner_image = models.ImageField(
        upload_to='banners/',
        blank=True,
        null=True
    )

    role = models.CharField(
        max_length=15,
        choices=ROLE_CHOICES,
        default='member'
    )

    # Tags / Permissions
    friendly = models.BooleanField(default=False)
    active_voice_channel = models.BooleanField(default=False)
    active_message = models.BooleanField(default=False)
    moderator = models.BooleanField(default=False)
    ticket_manager = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Head_Staff'
        
# ARTISTS

class ArtistCard(models.Model):
    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profiles/')
    banner_image = models.ImageField(upload_to='banners/')

    # Artist Tag
    artist_tag = models.CharField(max_length=100, blank=True, null=True)  # NEW

    # Tags as checkboxes
    friendly = models.BooleanField(default=False)
    active_voice_channel = models.BooleanField(default=False)
    active_message = models.BooleanField(default=False)
    moderator = models.BooleanField(default=False)
    ticket_manager = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Artist_Card'

#STAFF
class Staff(models.Model):
    name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profiles/')
    banner_image = models.ImageField(upload_to='banners/')

    # Tags as checkboxes
    staff = models.BooleanField(default=False)  # ✅ NEW Staff checkbox
    friendly = models.BooleanField(default=False)
    active_voice_channel = models.BooleanField(default=False)
    active_message = models.BooleanField(default=False)
    moderator = models.BooleanField(default=False)
    ticket_manager = models.BooleanField(default=False)
    manager = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Staff'
        
        # FREE FIRE GAMING SECTION
    
from django.db import models

class FreeFireTeam(models.Model):
    admin_head = models.CharField(max_length=200)
    team_elders = models.TextField(
        help_text="Separate names using · or commas"
    )
    team_members = models.TextField(
        help_text="Separate names using · or commas"
    )

    guild_id = models.CharField(
        max_length=20,
        default="923838382",
        editable=False
    )

    class Meta:
        verbose_name = "Free Fire Team"
        verbose_name_plural = "Free Fire Team"
        db_table = "free_fire_team"

    def __str__(self):
        return "Free Fire Team Details"
