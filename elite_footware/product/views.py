from django.shortcuts import render, redirect
from django.http import Http404

# Mock Database of products with rich details matching the mockup and website catalog
PRODUCTS = {
    1: {
        'id': 1,
        'name': 'KINETIC FLUX',
        'sub_title': 'Performance Running',
        'price': '$310.00',
        'description': 'Designed for high-intensity training and marathon running. Featuring advanced kinetic cushioning and lightweight upper mesh to maximize performance, stability, and everyday style.',
        'badge': 'NEW',
        'colors': [
            {
                'name': 'Kinetic Orange',
                'hex': '#D84200',
                'image': 'images/products/kinetic-v2.png',
                'thumbnails': ['images/products/kinetic-v2.png', 'images/products/void-elite.png', 'images/products/struct-scape.png']
            },
            {
                'name': 'Stealth Slate',
                'hex': '#2A2C2E',
                'image': 'images/products/void-elite.png',
                'thumbnails': ['images/products/void-elite.png', 'images/products/kinetic-v2.png', 'images/products/struct-scape.png']
            },
            {
                'name': 'Pure White',
                'hex': '#E5E5E5',
                'image': 'images/products/carbon-zero.png',
                'thumbnails': ['images/products/carbon-zero.png', 'images/products/kinetic-v2.png', 'images/products/void-elite.png']
            }
        ],
        'sizes': [
            {'val': '7', 'available': True},
            {'val': '8', 'available': True},
            {'val': '9', 'available': True},
            {'val': '10', 'available': True},
            {'val': '11', 'available': True},
            {'val': '12', 'available': True},
            {'val': '13', 'available': True},
            {'val': '14', 'available': False}
        ],
        'specs': [
            'Proprietary Kinetic-V2 cushioning midsole',
            'Breathable high-tensile engineered knit upper',
            'TPU heel support counter for stability',
            'High-traction rubber outsole with flex grooves'
        ],
        'showcase_title': 'RESPONSIVE PROPULSION',
        'showcase_desc': 'The Kinetic-V2 midsole structure adapts dynamically to your foot strike, transferring energy directly to the toe-off phase for explosive speed and smooth transitions.',
        'main_image': 'images/products/kinetic-v2.png'
    },
    2: {
        'id': 2,
        'name': 'ARCHITECT V.1 PERFORMANCE',
        'sub_title': 'Elite Marathon / Performance',
        'price': '$245.00',
        'description': 'Engineered for elite marathoners and aesthetic purists alike. The V.1 features our proprietary Carbon-Flow plate and high-rebound Safety Orange foam for unparalleled energy return. Designed with an architectural silhouette that transitions seamlessly from performance to lifestyle.',
        'badge': 'NEW ARRIVAL',
        'colors': [
            {
                'name': 'Safety Orange',
                'hex': '#D84200',
                'image': 'images/products/orange-element.png',
                'thumbnails': ['images/products/orange-element.png', 'images/products/void-elite.png', 'images/products/struct-scape.png']
            },
            {
                'name': 'Stealth Black',
                'hex': '#1A1A1A',
                'image': 'images/products/void-elite.png',
                'thumbnails': ['images/products/void-elite.png', 'images/products/orange-element.png', 'images/products/struct-scape.png']
            },
            {
                'name': 'Concrete Grey',
                'hex': '#ADABAA',
                'image': 'images/products/struct-scape.png',
                'thumbnails': ['images/products/struct-scape.png', 'images/products/orange-element.png', 'images/products/void-elite.png']
            }
        ],
        'sizes': [
            {'val': '7', 'available': True},
            {'val': '8', 'available': True},
            {'val': '9', 'available': True},
            {'val': '10', 'available': True},
            {'val': '11', 'available': True},
            {'val': '12', 'available': True},
            {'val': '13', 'available': True},
            {'val': '14', 'available': False}
        ],
        'specs': [
            'Carbon-Flow propulsion plate for optimal bending stiffness',
            'Safety Orange high-rebound cushioning foam',
            'Seamless engineered mesh upper for breathable lock-down fit',
            'Architectural silhouette styling for performance and lifestyle integration'
        ],
        'showcase_title': 'ENGINEERED FOR SUPREMACY',
        'showcase_desc': 'The Carbon-Flow™ plate is strategically placed within the midsole to provide explosive propulsion, reducing fatigue on long-distance runs while maintaining surgical precision in movement.',
        'main_image': 'images/products/orange-element.png'
    },
    3: {
        'id': 3,
        'name': 'VOID ELITE',
        'sub_title': 'Elite Track & Racing',
        'price': '$320.00',
        'description': 'A minimalist powerhouse for track and speed. Built with ultra-thin engineered mesh and specialized responsive foam to deliver elite energy return and a feather-light feel.',
        'badge': 'NEW',
        'colors': [
            {
                'name': 'Stealth Black',
                'hex': '#1A1A1A',
                'image': 'images/products/void-elite.png',
                'thumbnails': ['images/products/void-elite.png', 'images/products/carbon-zero.png', 'images/products/struct-scape.png']
            },
            {
                'name': 'Carbon White',
                'hex': '#FFFFFF',
                'image': 'images/products/carbon-zero.png',
                'thumbnails': ['images/products/carbon-zero.png', 'images/products/void-elite.png', 'images/products/struct-scape.png']
            }
        ],
        'sizes': [
            {'val': '7', 'available': True},
            {'val': '8', 'available': True},
            {'val': '9', 'available': True},
            {'val': '10', 'available': True},
            {'val': '11', 'available': True},
            {'val': '12', 'available': True},
            {'val': '13', 'available': False},
            {'val': '14', 'available': False}
        ],
        'specs': [
            'Ultra-thin lightweight speed mesh upper',
            'Carbon composite spike plate support',
            'High-density responsive foam core',
            'Streamlined racing fit design'
        ],
        'showcase_title': 'STREAMLINED EFFICIENCY',
        'showcase_desc': 'Every millimeter is engineered to shed weight. The minimal silhouette and carbon composite core offer unparalleled stability and speed during explosive sprints.',
        'main_image': 'images/products/void-elite.png'
    },
    4: {
        'id': 4,
        'name': 'STRUCT SCAPE',
        'sub_title': 'Trail & Rugged Terrain',
        'price': '$265.00',
        'description': 'Conquer the trails with stability and traction. Features a rugged tread design, reinforced toe guard, and responsive foam to absorb impact on rough, rocky terrains.',
        'badge': '',
        'colors': [
            {
                'name': 'Trail Beige',
                'hex': '#D4C5B9',
                'image': 'images/products/struct-scape.png',
                'thumbnails': ['images/products/struct-scape.png', 'images/products/orange-element.png', 'images/products/void-elite.png']
            },
            {
                'name': 'Forest Orange',
                'hex': '#D84200',
                'image': 'images/products/orange-element.png',
                'thumbnails': ['images/products/orange-element.png', 'images/products/struct-scape.png', 'images/products/void-elite.png']
            }
        ],
        'sizes': [
            {'val': '7', 'available': True},
            {'val': '8', 'available': True},
            {'val': '9', 'available': True},
            {'val': '10', 'available': True},
            {'val': '11', 'available': True},
            {'val': '12', 'available': True},
            {'val': '13', 'available': True},
            {'val': '14', 'available': True}
        ],
        'specs': [
            'All-terrain traction outsole with 5mm lugs',
            'TPU heel stabilizer frame',
            'Impact-absorbing trail foam midsole',
            'Reinforced protective toe cap'
        ],
        'showcase_title': 'ALL-WEATHER TRACTION',
        'showcase_desc': 'The deeply lugged outsole and stabilized heel frame work together to keep you grounded on loose dirt, wet mud, and sharp rock surfaces.',
        'main_image': 'images/products/struct-scape.png'
    },
    5: {
        'id': 5,
        'name': 'CARBON ZERO',
        'sub_title': 'Archive Concept / Lifestyle',
        'price': '$450.00',
        'description': 'An archive concept shoe merging luxury materials with futuristic architecture. Handcrafted details, unique decoupled sole, and lightweight support make this a collector\'s masterpiece.',
        'badge': 'LIMITED',
        'colors': [
            {
                'name': 'Pure White',
                'hex': '#FFFFFF',
                'image': 'images/products/carbon-zero.png',
                'thumbnails': ['images/products/carbon-zero.png', 'images/products/architect-low.png', 'images/products/void-elite.png']
            },
            {
                'name': 'Onyx Black',
                'hex': '#1A1A1A',
                'image': 'images/products/architect-low.png',
                'thumbnails': ['images/products/architect-low.png', 'images/products/carbon-zero.png', 'images/products/void-elite.png']
            }
        ],
        'sizes': [
            {'val': '7', 'available': True},
            {'val': '8', 'available': True},
            {'val': '9', 'available': True},
            {'val': '10', 'available': True},
            {'val': '11', 'available': True},
            {'val': '12', 'available': True},
            {'val': '13', 'available': False},
            {'val': '14', 'available': False}
        ],
        'specs': [
            'Decoupled futuristic sole architecture',
            'Luxury knit upper with handcrafted stitching',
            'Carbon fiber support shank',
            'Limited edition custom serial numbering'
        ],
        'showcase_title': 'FUTURISTIC ENGINEERING',
        'showcase_desc': 'The decoupled sole design distributes weight evenly across structural pressure points, creating a feeling of weightlessness and unparalleled comfort.',
        'main_image': 'images/products/carbon-zero.png'
    },
    6: {
        'id': 6,
        'name': 'ORANGE ELEMENT',
        'sub_title': 'Daily Training & Gym',
        'price': '$190.00',
        'description': 'Lightweight and versatile training shoe designed for daily workouts and gym sessions. The highly flexible design ensures comfort during lateral movements and weightlifting.',
        'badge': '',
        'colors': [
            {
                'name': 'Training Orange',
                'hex': '#D84200',
                'image': 'images/products/orange-element.png',
                'thumbnails': ['images/products/orange-element.png', 'images/products/struct-scape.png', 'images/products/void-elite.png']
            },
            {
                'name': 'Charcoal Slate',
                'hex': '#333538',
                'image': 'images/products/void-elite.png',
                'thumbnails': ['images/products/void-elite.png', 'images/products/orange-element.png', 'images/products/struct-scape.png']
            }
        ],
        'sizes': [
            {'val': '7', 'available': True},
            {'val': '8', 'available': True},
            {'val': '9', 'available': True},
            {'val': '10', 'available': True},
            {'val': '11', 'available': True},
            {'val': '12', 'available': True},
            {'val': '13', 'available': True},
            {'val': '14', 'available': True}
        ],
        'specs': [
            'Multi-directional flex groove outsole',
            'Flat, wide heel design for lifting stability',
            'Breathable lightweight knit mesh',
            'Comfort-fit padded collar'
        ],
        'showcase_title': 'DYNAMIC STABILITY',
        'showcase_desc': 'The low-profile flat heel provides a secure foundation for squats and deadlifts, while flexible forefoot grooves allow natural foot flex during sprints and jumps.',
        'main_image': 'images/products/orange-element.png'
    }
}

# 4 specific products for the "YOU MAY ALSO LIKE" recommendations
RECOMMENDED_PRODUCTS = [
    {
        'id': 2,
        'name': 'ARCHITECT V.1 GHOST',
        'price': '$245.00',
        'image': 'images/products/architect-low.png'
    },
    {
        'id': 3,
        'name': 'MONOLITH RACER',
        'price': '$280.00',
        'image': 'images/products/void-elite.png'
    },
    {
        'id': 4,
        'name': 'URBAN STRUCTURE LOW',
        'price': '$190.00',
        'image': 'images/products/struct-scape.png'
    },
    {
        'id': 1,
        'name': 'KINETIC FLUX',
        'price': '$310.00',
        'image': 'images/products/kinetic-v2.png'
    }
]

def product_page(request):
  return render(request, 'product/product_page.html')

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