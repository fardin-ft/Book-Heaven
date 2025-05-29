from django.shortcuts import render, redirect
from django.http import HttpResponse as httpResponse, JsonResponse
from math import ceil 
from .models import Product,Contact,Order,OrderUpdate
import json

# Create your views here.
def home(request):
    allProds = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact= Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        return JsonResponse({'status': 'success'})
    return render(request, "shop/contact.html")
def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                # Get order details
                order_details = order[0]
                items = json.loads(order_details.item_json)
                
                # Get order updates
                updates = OrderUpdate.objects.filter(order_id=orderId)
                response_data = {
                    'status': 'success',
                    'items': items,
                    'updates': [{'text': item.update_desc, 'time': item.timestamp.strftime("%d/%m/%Y %H:%M:%S")} for item in updates],
                    'order': {
                        'total': order_details.price,
                        'name': order_details.name,
                        'address': order_details.address,
                        'city': order_details.city,
                        'state': order_details.state,
                        'zip_code': order_details.zip_code
                    }
                }
                return JsonResponse(response_data)
            else:
                return JsonResponse({'status': 'error', 'message': 'No order found with these details'})
        except Exception as e:
            print(f"Error in tracker: {str(e)}")  # Log the error
            return JsonResponse({'status': 'error', 'message': 'Failed to fetch order details'})
    return render(request, 'shop/tracker.html')
def cart(request):
    return httpResponse("This is the cart page")


def checkout(request):
    if request.method == "POST":
        import json
        try:
            item_json = request.POST.get('itemJson', '')            
            cart_items = json.loads(item_json) if item_json else [] 
            price = 0
            validated_items = []
            for item in cart_items:
                try:
                    name = str(item.get('name', ''))
                    qty = max(1, int(item.get('qty', 1)))  
                    item_price = max(0, int(item.get('price', 0))) 
                    
                    # Add validated item to list
                    validated_items.append({
                        'name': name,
                        'qty': qty,
                        'price': item_price
                    })
                    price += qty * item_price # Calculate total price
                except (TypeError, ValueError) as e:
                    continue
            
            # Update cart_items with validated data
            cart_items = validated_items            
            # Get other form fields
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            address = request.POST.get('address', '') + ', ' + request.POST.get('address2', '')
            city = request.POST.get('city', '')
            state = request.POST.get('state', '')
            zip_code = request.POST.get('zip_code', '')

            # Create and save order
            order = Order(
                item_json=json.dumps(cart_items),  # Save the list directly
                price=price,
                name=name,
                email=email,
                phone=phone,
                address=address,
                city=city,
                state=state,
                zip_code=zip_code
            )
            order.save()
            update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
            update.save()
            return redirect(f'/shop/checkout/?order_success={order.order_id}')
        except Exception as e:
            print(f"Error processing order: {e}")
            return render(request, 'shop/checkout.html', {'error': str(e)})
            
    return render(request, 'shop/checkout.html')

def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                # Get order details
                order_details = order[0]
                items = json.loads(order_details.item_json)
                
                # Get order updates
                updates = OrderUpdate.objects.filter(order_id=orderId)
                response_data = {
                    'status': 'success',
                    'items': items,
                    'updates': [{'text': item.update_desc, 'time': item.timestamp.strftime("%d/%m/%Y %H:%M:%S")} for item in updates],
                    'order': {
                        'total': order_details.price,
                        'name': order_details.name,
                        'address': order_details.address,
                        'city': order_details.city,
                        'state': order_details.state,
                        'zip_code': order_details.zip_code
                    }
                }
                return JsonResponse(response_data)
            else:
                return JsonResponse({'status': 'error', 'message': 'No order found with these details'})
        except Exception as e:
            print(f"Error in tracker: {str(e)}")  # Log the error
            return JsonResponse({'status': 'error', 'message': 'Failed to fetch order details'})
    return render(request, 'shop/tracker.html')


def productView(request, myid):
    # Fetch the product using the product_id
    product = Product.objects.filter(product_id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})
def search(request):
    return render(request, 'shop/search.html')