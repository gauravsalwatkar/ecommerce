import operator
from django.shortcuts import render,redirect
from .models import Product, Orders, Profile
from django.views.generic import DetailView
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import SignUpForm, CreateProduct
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def Indexview(request):
    return render(request,'shop/index.html')

@login_required    
def ProductList(request):
    products= Product.objects.all()

    #search box code
    item = request.GET.get('item_name')
    if item != '' and item is not None:
        products = products.filter(Q(product_name__icontains=item)|
                                    Q(product_category__icontains=item)
                                    )
    
    # paginator code
    paginator = Paginator(products,6)
    page = request.GET.get('page')
    products= paginator.get_page(page)
    context = {
            'products' : products
        }
    return render(request,'shop/list.html',context)

@login_required
def detail_view(request, id):
    context = {}
    context["data"] = Product.objects.get(id=id)
    return render(request,"shop/details.html",context)
    
@login_required
def checkout_view(request):
    if request.method=="POST":
        item_json = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address1','') + " " + request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        total = request.POST.get('total','')
        order = Orders(item_json=item_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone, total=total)
        order.save()
        thank = True
        id = order.order_id
        return render(request,'shop/checkout.html',{'thank':thank, 'id':id})
    return render(request,'shop/checkout.html')

def registerview(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username} , Please Log In')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'registration/register.html',{'form':form})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = CreateProduct(request.POST or None,request.FILES)    
        if form.is_valid():
            form.save()
            messages.success(request,'Product Created Successfully')
            return redirect('/shop/list')
    else:
        form = CreateProduct()
    return render(request,'shop/create_product.html',{'form':form})

@login_required
def profile(request):
    users = Profile.objects.all()    
    return render(request,'shop/profile.html',{'users':users})
