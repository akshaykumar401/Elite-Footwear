from django.shortcuts import render
from product.models import Product


# Create your views here.
def get_product_dict(product):
  """
  Returns a dictionary of product details.
  """
  return {
    'name': product.product_name,
    'price': f"${product.product_price}",
    'image': product.product_image,
    'description': product.product_description,
    'secondary_title': product.secondary_title,
    'secondary_description': product.secondary_description,
    'id': product.id,
    'category': product.category,
    'gender': product.gender,
    'is_new': product.is_new,
    'available': product.product_available
  }

def home(request):
  # retriving top 6 new products
  # Product is arranged in as latest to old
  new_products = Product.objects.filter(is_new=True).order_by('-id')[:6]
  new_products_list = []
  for p in new_products:
    p_dict = get_product_dict(p)
    if p_dict:
      new_products_list.append(p_dict)
  
  context = {
    'all_products': new_products_list
  }
  return render(request, 'elite_footware/index.html', context)