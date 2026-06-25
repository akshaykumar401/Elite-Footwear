from django.contrib import admin
from .models import Product, ProductColor, ProductSize, ProductImage, ProductSpecification

class ProductColorInline(admin.TabularInline):
  model = ProductColor
  extra = 1

class ProductSizeInline(admin.TabularInline):
  model = ProductSize
  extra = 1

class ProductImageInline(admin.TabularInline):
  model = ProductImage
  extra = 1

class ProductSpecificationInline(admin.TabularInline):
  model = ProductSpecification
  extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('product_name', 'product_price', 'category', 'gender', 'product_available')
  list_filter = ('category', 'gender', 'product_available')
  search_fields = ('product_name', 'product_description')
  inlines = [ProductColorInline, ProductSizeInline, ProductImageInline, ProductSpecificationInline]

  def save_model(self, request, obj, form, change):
    if not obj.user_id:
      obj.user = request.user
    super().save_model(request, obj, form, change)

@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
  list_display = ('color_name', 'color_hex', 'product')
  search_fields = ('color_name', 'product__product_name')

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
  list_display = ('size', 'available', 'product')
  list_filter = ('available', 'size')
  search_fields = ('product__product_name',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
  list_display = ('product', 'color', 'is_main')
  list_filter = ('is_main',)

@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
  list_display = ('specification', 'product')
  search_fields = ('specification', 'product__product_name')
