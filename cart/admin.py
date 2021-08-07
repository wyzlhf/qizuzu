from django.contrib import admin

# Register your models here.
from cart.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['short_customer','customer','product_amount','start_date','status','created','updated']
    def has_add_permission(self, request):
        return False

    def get_actions(self, request):
        # 在actions中去掉‘删除’操作
        actions = super(CartAdmin, self).get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions