# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect
# pyrefly: ignore [missing-import]
from .forms import UserRegistrationForm
# pyrefly: ignore [missing-import]
from django.contrib.auth import login
# pyrefly: ignore [missing-import]
from django.contrib.auth.decorators import login_required
# pyrefly: ignore [missing-import]
from .models import UserProfile, Wishlist, Address
from product.models import Product
from product.views import get_product_dict


# Create your views here.
def user_page_data(request):
    user = request.user
    profile_obj, created = UserProfile.objects.get_or_create(user=user)
    
    # Wishlist items List
    wishlist_items = []
    for item in Wishlist.objects.filter(user=user):
        p_dict = get_product_dict(item.product.id)
        if p_dict:
            wishlist_items.append({
                'id': p_dict['id'],
                'name': p_dict['name'],
                'price': p_dict['price'],
                'image': p_dict['main_image']
            })
    
    # Address list
    addresses = Address.objects.filter(user=user)
    address_list = []
    for address in addresses:
        address_list.append({
            'label': f'{address.label} Address',
            'name': address.name,
            'line1': address.line1,
            'city_state_zip': f'{address.city}, {address.state} {address.zip_code}',
            'phone': address.phone,
            'is_default': address.is_default,
        })

    return {
    'profile': {
        'name': f"{user.first_name} {user.last_name}",
        'email': user.email,
        'phone': profile_obj.phone or "Not provided",
        'member_since': user.date_joined.strftime('%B %Y'),
        'tier': 'Elite Black Member',
        'preferred_size': str(profile_obj.prefered_size) if profile_obj.prefered_size else "Not specified",
        'stats': {
            'total_orders': 8,
            'wishlist_count': len(wishlist_items),
            'rewards': 850
        }
    },
    'orders': [
        {
            'id': '#EF-2026-9812',
            'date': 'June 14, 2026',
            'total': '$260.00',
            'status': 'Delivered',
            'status_class': 'delivered',
            'items': [
                {
                    'name': 'ARCHITECT V.1 PERFORMANCE',
                    'color': 'Stealth Black',
                    'image': '/static/images/products/architect-low.png',
                    'size': '10.5'
                }
            ]
        },
        {
            'id': '#EF-2026-9402',
            'date': 'April 30, 2026',
            'total': '$220.00',
            'status': 'Delivered',
            'status_class': 'delivered',
            'items': [
                {
                    'name': 'APEX TRAIL RUNNER',
                    'color': 'Orange Burst',
                    'image': '/static/images/products/kinetic-v2.png',
                    'size': '10.0'
                }
            ]
        },
        {
            'id': '#EF-2026-8819',
            'date': 'Feb 12, 2026',
            'total': '$180.00',
            'status': 'Delivered',
            'status_class': 'delivered',
            'items': [
                {
                    'name': 'COURT CLASSIC LUX',
                    'color': 'Sandy Beige',
                    'image': '/static/images/products/carbon-zero.png',
                    'size': '10.5'
                }
            ]
        }
    ],
    'wishlist': wishlist_items,
    'addresses': address_list,
}

@login_required
def user_page(request):
    data = user_page_data(request)
    return render(request, 'user/user_page.html', data)

# Register Functionality
def register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password1'])
      user.save()
      UserProfile.objects.create(
        user=user,
        phone=form.cleaned_data['phone'],
        prefered_size=form.cleaned_data['prefered_size']
      )
      # Login the user
      login(request, user)
      return redirect('product_page')
  else:
    form = UserRegistrationForm()

  return render(request, 'registration/register.html', {
    'form': form,
  })