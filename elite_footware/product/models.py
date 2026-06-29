# pyrefly: ignore [missing-import]
from django.db import models
# pyrefly: ignore [missing-import]
from django.contrib.auth.models import User


class Product(models.Model):
    # Category Enum
    CATEGORY_CHOICES = (
        ('Running', 'Running'),
        ('Casual', 'Casual'),
        ('Formal', 'Formal'),
        ('Sports', 'Sports'),
        ('Boots', 'Boots'),
        ('Sandals', 'Sandals'),
        ('Slippers', 'Slippers'),
    )

    # Gender Enum
    GENDER_CHOICES = (
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Kids', 'Kids'),
        ('Unisex', 'Unisex'),
    )


    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
   
    product_available = models.BooleanField(default=True)
    product_created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    product_updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    secondary_title = models.CharField(max_length=100, null=True, blank=True)
    secondary_description = models.TextField(null=True, blank=True)
    is_new = models.BooleanField(default=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product_name or f"Product {self.pk}"

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors")
    color_name = models.CharField(max_length=50)
    color_hex = models.CharField(max_length=50, help_text="HEX color code, e.g., #D84200")

    def __str__(self):
        return f"{self.color_name} ({self.product.product_name})"

class ProductSize(models.Model):
    SIZE_CHOICES = [
        ("5", "5"),
        ("5.5", "5.5"),
        ("6", "6"),
        ("6.5", "6.5"),
        ("7", "7"),
        ("7.5", "7.5"),
        ("8", "8"),
        ("8.5", "8.5"),
        ("9", "9"),
        ("9.5", "9.5"),
        ("10", "10"),
        ("10.5", "10.5"),
        ("11", "11"),
        ("11.5", "11.5"),
        ("12", "12"),
        ("12.5", "12.5"),
        ("13", "13"),
        ("14", "14"),
        ("15", "15"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.size} ({self.product.product_name})"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    color = models.ForeignKey(ProductColor, on_delete=models.SET_NULL, related_name="images", null=True, blank=True)
    image = models.ImageField(upload_to="product_images/")
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product.product_name} - {self.color.color_name if self.color else 'General'}"

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="specifications")
    specification = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.specification} ({self.product.product_name})"