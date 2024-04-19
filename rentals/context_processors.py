from .models import ShopInfo, SocialHandle


# SHOP INFO CONTEXT PROCESSOR
def shop_info_context(request):
    shop_info = ShopInfo.objects.first()
    context = {
        'shop_info': shop_info,
    }
    return context


# SOCIAL HANDLES CONTEXT PROCESSOR
def social_handles_context(request):
    social_handles = {}
    social_handle = SocialHandle.objects.all()
    for handle in social_handle:
        social_handles[handle.platform] = handle.handle_url
    context = {
        'social_handles': social_handles
    }
    return context
    