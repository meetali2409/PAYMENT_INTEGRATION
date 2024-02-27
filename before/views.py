from django.shortcuts import render
from django.http import HttpResponse
import razorpay
from .models import Apple

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    if request.method == "POST":
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))*100
        client=razorpay.Client(auth=("rzp_test_0FmUf2hOFOAgiu","drJ4ANL9czW9EY9e8lVvkcDj"))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        apple=Apple(name=name,amount=amount,paymentid=payment['id'])
        apple.save()
        return render(request,"index.html",{'payment':payment})
    return render(request,"index.html")

@csrf_exempt
def success(request):
    if request.method=='POST':
        a=request.POST
        order_id=""
        for key,val in a.items():
            if key=="razorpay_order_id":
                order_id=val
                break
        user=Apple.objects.filter(paymentid=order_id).first()
        user.paid=True
    return render(request,"success.html")