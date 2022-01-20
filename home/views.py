from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from .models import *
from .forms import SearchForm
from Cart.models import CartForm

def home(request,id=None):
    category = Category.objects.all()
    product = Product.objects.all()
    search = SearchForm()
    if id:
        data = Category.objects.get(id=id)
        product = product.filter(category=data)
    return render(request,'home.html',{'category':category,'product':product,'search':search})

def all_product(request,id=None):
    products = Product.objects.all()
    category = Category.objects.all()
    search = SearchForm()
    if id:
        data = Category.objects.get(id=id)
        products = products.filter(category=data)
    return render(request,'products.html',{'category':category,'product':products,'search':search})

def detail(request,id):
    product = get_object_or_404(Product,id=id)
    image = Image_pro.objects.filter(product_img_id=id)
    is_favourite = False
    cart_form = CartForm()
    comment_form = CommentForm()
    comment = Comment.objects.filter(is_reply=False,product_id=id)
    if product.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    if product.status == 'Color':
        if request.method == 'POST':
            variants = Variant.objects.filter(product_varient_id=id)
            var_id = request.POST.get('select')
            variant = Variant.objects.get(id=var_id)
        else:
            variants= Variant.objects.filter(product_varient_id=id)
            variant = Variant.objects.get(id=variants[0].id)
        return render(request,'detail.html',{'product':product,'variant':variant,'variants':variants})
    elif product.status == 'Size':
        if request.method == 'POST':
            variants = Variant.objects.filter(product_varient_id=id)
            var_id = request.POST.get('select')
            variant = Variant.objects.get(id=var_id)
        else:
            variants = Variant.objects.filter(product_varient_id=id)
            variant = Variant.objects.get(id=variants[0].id)
        return render(request,'detail.html',{'variants':variants,'product':product,'variant':variant,'is_favourite':is_favourite})
    else:

        return render(request,'detail.html',{'pro':product,'is_favourite':is_favourite,'comment':comment,'comment_form':comment_form,'image':image,'cart_form':cart_form})


def favourite(request,id):
    url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product,id=id)
    is_favourite = False
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
        is_favourite = False
    else:
        product.favourite.add(request.user)
        is_favourite = True
    return redirect(url)


def comment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(comment=data['comment'],user_id=request.user.id,product_id=id,rate=data['rate'])
        return redirect(url)



def search(request):
    product = Product.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']
            if data.isdigit():
                product = product.filter(Q(discount__exact=data)|Q(unit_price__exact=data))
            else:
                product = product.filter(Q(name__icontains=data))
        return render(request,'products.html',{'product':product,'form':form})