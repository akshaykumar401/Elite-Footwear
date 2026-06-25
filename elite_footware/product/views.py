import os
from django.shortcuts import render
from django.conf import settings
from .models import Product

def get_image_url(image_field):
    if not image_field:
        return ""
    
    filename = os.path.basename(image_field.name)
    
    # Check if the file physically exists in MEDIA_ROOT
    media_path = os.path.join(settings.MEDIA_ROOT, image_field.name)
    if os.path.exists(media_path):
        return f"{settings.MEDIA_URL.rstrip('/')}/{image_field.name.lstrip('/')}"
        
    # Fallback to static folder if it's one of the pre-existing mock images
    static_fallback_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'products', filename)
    if os.path.exists(static_fallback_path):
        return f"{settings.STATIC_URL.rstrip('/')}/images/products/{filename}"
        
    try:
        return image_field.url
    except ValueError:
        return ""

def get_product_dict(product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return None

    # Colors mapping
    colors_list = []
    for color in product.colors.all():
        # Find the main image for this color
        main_img = ""
        main_img_obj = color.images.filter(is_main=True).first()
        if main_img_obj:
            main_img = get_image_url(main_img_obj.image)
        else:
            first_img = color.images.first()
            if first_img:
                main_img = get_image_url(first_img.image)
        
        # Thumbnails: all images associated with this color
        thumbnails = [get_image_url(img.image) for img in color.images.all()]
        
        colors_list.append({
            'name': color.color_name,
            'hex': color.color_hex,
            'image': main_img,
            'thumbnails': thumbnails
        })
        
    # Sizes mapping
    sizes_list = []
    for size in product.sizes.all().order_by('size'):
        sizes_list.append({
            'val': size.size,
            'available': size.available
        })
        
    # Specifications mapping
    specs_list = [spec.specification for spec in product.specifications.all()]
    
    # Main image mapping (fallback to first color's main image)
    main_image = ""
    if product.product_image:
        main_image = get_image_url(product.product_image)
    elif colors_list:
        main_image = colors_list[0]['image']
        
    # Badge mapping
    badge = ""
    if product.is_new:
        if product.id == 5:
            badge = "LIMITED"
        elif product.id == 2:
            badge = "NEW ARRIVAL"
        else:
            badge = "NEW"
            
    # Sub-title / Category styling fallback
    sub_title_mapping = {
        1: 'Performance Running',
        2: 'Elite Marathon / Performance',
        3: 'Elite Track & Racing',
        4: 'Trail & Rugged Terrain',
        5: 'Archive Concept / Lifestyle',
        6: 'Daily Training & Gym'
    }
    sub_title = sub_title_mapping.get(product.id, f"{product.gender or ''} {product.category or 'Performance'}")

    return {
        'id': product.id,
        'name': product.product_name,
        'sub_title': sub_title,
        'price': f"${product.product_price:.2f}" if product.product_price else "$0.00",
        'description': product.product_description,
        'badge': badge,
        'colors': colors_list,
        'sizes': sizes_list,
        'specs': specs_list,
        'category': product.category or '',
        'gender': product.gender or '',
        'showcase_title': product.secondary_title or '',
        'showcase_desc': product.secondary_description or '',
        'main_image': main_image
    }

class DatabaseProductsMapping:
    def get(self, product_id, default=None):
        p_dict = get_product_dict(product_id)
        return p_dict if p_dict is not None else default

    def __getitem__(self, product_id):
        p_dict = get_product_dict(product_id)
        if p_dict is None:
            raise KeyError(product_id)
        return p_dict

    def __contains__(self, product_id):
        return get_product_dict(product_id) is not None

class DatabaseRecommendedProductsList:
    def _get_list(self):
        recommended_ids = [2, 3, 4, 1]
        products = []
        for r_id in recommended_ids:
            p_dict = get_product_dict(r_id)
            if p_dict:
                products.append({
                    'id': p_dict['id'],
                    'name': p_dict['name'],
                    'price': p_dict['price'],
                    'image': p_dict['main_image']
                })
        if not products:
            for p in Product.objects.all()[:4]:
                p_dict = get_product_dict(p.id)
                if p_dict:
                    products.append({
                        'id': p_dict['id'],
                        'name': p_dict['name'],
                        'price': p_dict['price'],
                        'image': p_dict['main_image']
                    })
        return products

    def __iter__(self):
        return iter(self._get_list())

    def __getitem__(self, index):
        return self._get_list()[index]

    def __len__(self):
        return len(self._get_list())

PRODUCTS = DatabaseProductsMapping()
RECOMMENDED_PRODUCTS = DatabaseRecommendedProductsList()

def product_page(request):
    all_products = []
    for p in Product.objects.all().order_by('id'):
        p_dict = get_product_dict(p.id)
        if p_dict:
            all_products.append(p_dict)
            
    context = {
        'products': all_products
    }
    return render(request, 'product/product_page.html', context)

def product_detail(request, product_id: int):
    # Try to retrieve product by id, otherwise fallback to product 2
    product = PRODUCTS.get(product_id)
    if not product:
        product = PRODUCTS.get(2)
    
    context = {
        'product': product,
        'recommended_products': RECOMMENDED_PRODUCTS
    }
    return render(request, 'product/product_detail.html', context)