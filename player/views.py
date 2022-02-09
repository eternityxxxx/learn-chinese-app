from django.views.generic import TemplateView, View

from .models import Song


class SongView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["song"] = Song.objects.filter(pk=self.kwargs["pk"]).get()

        return context
