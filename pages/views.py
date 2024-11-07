from django.views.generic import ListView, TemplateView
from accounts.models import CustomUser


class HomePageView(ListView):
    template_name = "home.html"
    model = CustomUser


class HomePageView2(TemplateView):
    template_name = "home2.html"
    model = CustomUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = CustomUser.objects.all()
        return context
