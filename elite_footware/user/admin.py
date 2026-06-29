# pyrefly: ignore [missing-import]
from django.contrib import admin
# pyrefly: ignore [missing-import]
from .models import UserProfile, Wishlist, Address

# Customize Admin Portal Branding
admin.site.site_header = "ELITE FOOTWEAR Admin Portal"
admin.site.site_title = "Elite Footwear Admin"
admin.site.index_title = "Manage Store, Profiles, and Catalog"

# Register models with enhanced ModelAdmin classes
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'phone', 'prefered_size')
  search_fields = ('user__username', 'user__email', 'phone')
  ordering = ('user__username',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
  list_display = ('user', 'product')
  list_filter = ('product',)
  search_fields = ('user__username', 'product__product_name')
  ordering = ('user__username',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
  list_display = ('user', 'label', 'name', 'city', 'state', 'zip_code', 'phone', 'is_default')
  list_filter = ('is_default', 'state', 'city')
  search_fields = ('user__username', 'name', 'line1', 'city', 'phone')
  ordering = ('user__username', '-is_default')
