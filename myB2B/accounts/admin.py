from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import User,UserProfile, Profile, BusinessProfile, FullSale, PartialStakeSale, FSImages,PSSImages,FSDoc,PSSDoc,FSBusiProof,PSSBusiProof
from .models import SellOrLeaseAssets,SLImages,SLDoc,SLBusiProof,StripeCustomer,plan

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'full_name', 'login_count', 'is_active', 'is_staff')
    list_display_links = ('username', 'email',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    def full_name(self, obj):
        return obj.get_full_name()


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Profile)
# admin.site.register(BusinessProfile)
admin.site.register(FullSale)
admin.site.register(PartialStakeSale)
admin.site.register(FSImages)
admin.site.register(PSSImages)
admin.site.register(FSDoc)
admin.site.register(PSSDoc)
admin.site.register(FSBusiProof)
admin.site.register(PSSBusiProof)
admin.site.register(SellOrLeaseAssets)
admin.site.register(SLImages)
admin.site.register(SLDoc)
admin.site.register(SLBusiProof)
admin.site.register(StripeCustomer)
admin.site.register(plan)