from django.shortcuts import render, get_object_or_404
from .models import Category, Brend, Product, Comments

def home(request):
    categories = Category.objects.all()
    brends = Brend.objects.all()
    products = Product.objects.all()
    return render(request, 'home.html', {
        'categories': categories,
        'brends': brends,
        'products': products
    })

def product_list(request, category_slug=None, brend_slug=None):
    category = None
    brend = None
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug)
        products = products.filter(category=category)
    
    if brend_slug:
        brend = get_object_or_404(Brend, brend_slug=brend_slug)
        products = products.filter(brend=brend)

    return render(request, 'product_list.html', {
        'category': category,
        'brend': brend,
        'products': products,
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = Comments.objects.filter(brend=product.brend)

    return render(request, 'product_detail.html', {
        'product': product,
        'comments': comments
    })

from django.shortcuts import render, redirect
from .models import Comments
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def post_comment(request):
    comments = Comments.objects.all() 
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.user  
            comment.save()
            return redirect('post_comment')
    else:
        form = CommentForm()

    return render(request, 'product_detail.html', {'comment': comments, 'form': form})
