from django.shortcuts import render

# Create your views here.
def user_page(request):
    user_context = {
        'profile': {
            'name': 'Alex Carter',
            'email': 'alex.carter@elite.com',
            'phone': '+1 (555) 019-2834',
            'member_since': 'March 2024',
            'tier': 'Elite Black Member',
            'preferred_size': '10.5',
            'stats': {
                'total_orders': 8,
                'wishlist_count': 3,
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
                        'image': 'images/products/architect-low.png',
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
                        'image': 'images/products/kinetic-v2.png',
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
                        'image': 'images/products/carbon-zero.png',
                        'size': '10.5'
                    }
                ]
            }
        ],
        'wishlist': [
            {
                'id': 2,
                'name': 'ARCHITECT V.1 PERFORMANCE',
                'price': '$260.00',
                'image': 'images/products/orange-element.png'
            },
            {
                'id': 3,
                'name': 'APEX TRAIL RUNNER',
                'price': '$220.00',
                'image': 'images/products/void-elite.png'
            },
            {
                'id': 1,
                'name': 'COURT CLASSIC LUX',
                'price': '$180.00',
                'image': 'images/products/kinetic-v2.png'
            }
        ],
        'addresses': [
            {
                'label': 'Primary Shipping',
                'name': 'Alex Carter',
                'line1': '1428 Architecture Way, Suite 400',
                'city_state_zip': 'San Francisco, CA 94103',
                'phone': '+1 (555) 019-2834'
            },
            {
                'label': 'Office Address',
                'name': 'Alex Carter',
                'line1': '100 Tech Plaza, Floor 12',
                'city_state_zip': 'San Francisco, CA 94105',
                'phone': '+1 (555) 019-9988'
            }
        ],
    }
    return render(request, 'user/user_page.html', user_context)