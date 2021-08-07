from cart.models import Cart
from customer.models import Customer


def cart(request):
    phone=request.session.get('phone')
    if phone:
        customer=Customer.objects.filter(phone=phone)[0]
        carts=customer.customers.all()
        product_num=0
        for cart in carts:
            cart_product_amount=cart.product_amount
            product_num+=cart_product_amount
        return {'cart_num': product_num}
    else:
        return {'cart_num':-1}
