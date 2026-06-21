def cart(request):
    total_count = 0
    if hasattr(request, 'session'):
        cart_data = request.session.get('cart', {})
        for item in cart_data.values():
            total_count += item.get('quantity', 0)
    return {'cart_count': total_count}
