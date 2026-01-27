from .models import Category
from follow_us.models import FollowUs

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)
def get_social_links(request):
    follow_us_links = FollowUs.objects.all()
    return dict(follow_us_links=follow_us_links)