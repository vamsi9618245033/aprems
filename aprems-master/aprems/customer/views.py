from .forms import FeedbackForm
def login(request):
    return render(request,'customer/login.html')
def Home(request):
    return render(request, 'customer/Home.html', {'title': 'Home'})


from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} created Successfully')
            return redirect('customer/home')
    else:
        form = UserRegisterForm()
    return render(request, 'customer/register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'customer/profile.html')


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = FeedbackForm()
    return render(request, 'customer/feedback_form.html', {'form': form})

def thank_you(request):
    return render(request, 'customer/thank_you.html')


def product_list(request):
    product_list = Product.objects.all()
    form = ProductForm(request.POST or None)

    items_per_page = 3
    paginator = Paginator(product_list, items_per_page)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    available_pages = paginator.page_range

    return render(request, 'customer/product_list.html', {'products': products, 'form': form, 'available_pages': available_pages})


from django.contrib.auth.decorators import login_required
from .forms import ProductForm

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'customer/add_product.html', {'form': form})



from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    user = request.user
    products = Product.objects.filter(user=user)  # Filter products added by the user
    return render(request, 'customer/profile.html', {'user': user, 'products': products})

from django.contrib.auth.decorators import login_required
from .forms import CartItemForm

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user

    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
            cart_item.quantity = quantity
            cart_item.save()
            return redirect('product_list')
    else:
        form = CartItemForm()

    return render(request, 'customer/add_to_cart.html', {'form': form, 'product': product})




@login_required
def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total = 0

    if request.method == 'POST':
        item_id_to_remove = request.POST.get('remove_item')
        try:
            cart_item_to_remove = CartItem.objects.get(id=item_id_to_remove)
            cart_item_to_remove.delete()
            return redirect('view_cart')
        except CartItem.DoesNotExist:
            pass

    for item in cart_items:
        item.subtotal = item.quantity * item.product.price
        total += item.subtotal
        item.save()

    return render(request, 'customer/cart.html', {'cart_items': cart_items, 'total': total})



from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

@login_required
def user_profile(request):
    user = request.user
    products = Product.objects.filter(user=user)
    products_per_page = 3
    paginator = Paginator(products, products_per_page)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If the page is out of range (e.g., 9999), deliver the last page
        products = paginator.page(paginator.num_pages)

    return render(request, 'customer/profile.html', {'user': user, 'products': products})





import razorpay
from django.views.decorators.csrf import csrf_exempt
from .models import CartItem

razorpay_client = razorpay.Client(auth=("rzp_test_WgA54Wq6eCJ2LU", "i0EgFc151doPfV6xyZn7hUUg"))


def get_total_from_cart(user):
    cart_items = CartItem.objects.filter(user=user)
    total = 0

    for item in cart_items:
        item.subtotal = item.quantity * item.product.price
        total += item.subtotal

    return total


def payment(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    if not cart_items:
        # Cart is empty, display a message
        return render(request, 'customer/empty_cart.html')

    if 'product_id' in request.POST:
        # "Buy Now" scenario
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        quantity = int(request.POST.get('quantity', 1))
        amount_inr = product.price * quantity  # Calculate total price based on quantity
        amount_in_paise = int(amount_inr * 100)
    else:
        # Cart checkout scenario
        amount_inr = get_total_from_cart(user)
        amount_in_paise = int(amount_inr * 100)

    order = razorpay_client.order.create({
        'amount': amount_in_paise,
        'currency': 'INR',
    })

    return render(request, 'customer/payment.html', {'order': order, 'amount_inr': amount_inr})


@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        data = request.POST
        try:
            razorpay_client.utility.verify_payment_signature(data)
            status = 'success'
        except Exception as e:
            status = 'failure'

        return render(request, 'customer/payment_success.html', {'status': status})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product  # Replace 'your_app' with the actual app name

@login_required
def delete_product(request, product_id):
    try:
        product = Product.objects.get(id=product_id, user=request.user)
        product.delete()
    except Product.DoesNotExist:
        # Handle the case where the product doesn't exist or doesn't belong to the user
        pass

    return redirect('user_profile')  # Redirect back to the user's profile page


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import User, Product, Feedback
from .forms import ProductForm, FeedbackForm

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'customer/admin_dashboard.html')

@login_required
@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'customer/manage_users.html', {'users': users})

@login_required
@user_passes_test(is_admin)
def manage_products(request):
    products = Product.objects.all()
    return render(request, 'customer/manage_products.html', {'products': products})

@login_required
@user_passes_test(is_admin)
def manage_feedback(request):
    feedback = Feedback.objects.all()
    return render(request, 'customer/manage_feedback.html', {'feedback': feedback})
