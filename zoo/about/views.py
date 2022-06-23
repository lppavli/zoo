from django.shortcuts import render
from django.views.generic import TemplateView


# def about_view(request):
#     print(request.method)
#     context = {}
#     context['active_page'] = '/about/'
#     return render(request, 'about/about.html', context)

class AboutTemplateView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutTemplateView, self).get_context_data()
        context['active_page'] = '/about/'
        return context
