from django.contrib import admin

# Register your models here.
from customer.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','phone','is_actived','verify_code','created','updated']
    def has_add_permission(self, request):
        return False
    def get_actions(self, request):
        # 在actions中去掉‘删除’操作
        actions = super(CustomerAdmin, self).get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions