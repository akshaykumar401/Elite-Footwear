import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from product.views import PRODUCTS, RECOMMENDED_PRODUCTS

def cart_page(request):
    cart = request.session.get('cart', {})
    cart_items = []
    subtotal = 0.0
    
    for key, item in list(cart.items()):
        pid = item['product_id']
        color_name = item['color']
        size = item['size']
        quantity = item['quantity']
        
        product = PRODUCTS.get(pid)
        if not product:
            del cart[key]
            request.session.modified = True
            continue
            
        color_info = None
        for c in product['colors']:
            if c['name'].lower() == color_name.lower():
                color_info = c
                break
        if not color_info:
            color_info = product['colors'][0]
            
        price_val = float(product['price'].replace('$', '').strip())
        item_total = price_val * quantity
        subtotal += item_total
        
        cart_items.append({
            'item_key': key,
            'product': product,
            'color': color_name,
            'size': size,
            'quantity': quantity,
            'price': price_val,
            'price_str': product['price'],
            'total_price': item_total,
            'total_price_str': f"${item_total:.2f}",
            'image': color_info['image']
        })
        
    shipping = 0.0 if (subtotal > 300.0 or subtotal == 0) else 15.0
    tax = 0.08 * subtotal
    total = subtotal + shipping + tax
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'subtotal_str': f"${subtotal:.2f}",
        'shipping': shipping,
        'shipping_str': f"${shipping:.2f}" if shipping > 0 else "Free",
        'tax': tax,
        'tax_str': f"${tax:.2f}",
        'total': total,
        'total_str': f"${total:.2f}",
        'recommended_products': RECOMMENDED_PRODUCTS
    }
    
    return render(request, 'cart/cart_page.html', context)

@require_POST
def cart_add(request):
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST
            
        product_id = int(data.get('product_id'))
        color = data.get('color')
        size = data.get('size')
        quantity = int(data.get('quantity', 1))
        
        if not product_id or not color or not size:
            return JsonResponse({'success': False, 'error': 'Missing product parameters'}, status=400)
            
        if product_id not in PRODUCTS:
            return JsonResponse({'success': False, 'error': 'Product not found'}, status=404)
            
        cart = request.session.setdefault('cart', {})
        item_key = f"{product_id}_{color}_{size}"
        
        if item_key in cart:
            cart[item_key]['quantity'] += quantity
        else:
            cart[item_key] = {
                'product_id': product_id,
                'color': color,
                'size': size,
                'quantity': quantity
            }
            
        request.session.modified = True
        total_count = sum(item['quantity'] for item in cart.values())
        
        return JsonResponse({
            'success': True,
            'message': 'Item added to cart',
            'cart_count': total_count
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@require_POST
def cart_update(request):
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST
            
        item_key = data.get('item_key')
        quantity = int(data.get('quantity', 1))
        
        cart = request.session.get('cart', {})
        if item_key in cart:
            if quantity > 0:
                cart[item_key]['quantity'] = quantity
                request.session.modified = True
                success = True
                message = 'Quantity updated'
            else:
                del cart[item_key]
                request.session.modified = True
                success = True
                message = 'Item removed'
        else:
            return JsonResponse({'success': False, 'error': 'Item not found in cart'}, status=404)
            
        total_count = 0
        subtotal = 0.0
        item_total = 0.0
        
        for key, item in cart.items():
            pid = item['product_id']
            qty = item['quantity']
            prod = PRODUCTS.get(pid)
            if prod:
                price = float(prod['price'].replace('$', '').strip())
                subtotal += price * qty
                total_count += qty
                if key == item_key:
                    item_total = price * qty
                    
        shipping = 0.0 if (subtotal > 300.0 or subtotal == 0) else 15.0
        tax = 0.08 * subtotal
        total = subtotal + shipping + tax
        
        return JsonResponse({
            'success': success,
            'message': message,
            'cart_count': total_count,
            'subtotal': f"${subtotal:.2f}",
            'shipping': f"${shipping:.2f}" if shipping > 0 else "Free",
            'tax': f"${tax:.2f}",
            'total': f"${total:.2f}",
            'item_total': f"${item_total:.2f}"
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)

@require_POST
def cart_remove(request):
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST
            
        item_key = data.get('item_key')
        
        cart = request.session.get('cart', {})
        if item_key in cart:
            del cart[item_key]
            request.session.modified = True
            success = True
            message = 'Item removed'
        else:
            return JsonResponse({'success': False, 'error': 'Item not found in cart'}, status=404)
            
        total_count = 0
        subtotal = 0.0
        for key, item in cart.items():
            pid = item['product_id']
            qty = item['quantity']
            prod = PRODUCTS.get(pid)
            if prod:
                price = float(prod['price'].replace('$', '').strip())
                subtotal += price * qty
                total_count += qty
                
        shipping = 0.0 if (subtotal > 300.0 or subtotal == 0) else 15.0
        tax = 0.08 * subtotal
        total = subtotal + shipping + tax
        
        return JsonResponse({
            'success': success,
            'message': message,
            'cart_count': total_count,
            'subtotal': f"${subtotal:.2f}",
            'shipping': f"${shipping:.2f}" if shipping > 0 else "Free",
            'tax': f"${tax:.2f}",
            'total': f"${total:.2f}"
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=400)