from datetime import datetime, date
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.views import generic

from .models import *
from .models import Calendar


# Create your views here.
class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/create_event.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        d = get_date(self.request.GET.get('day', None))

        cal = Calendar(d.year, d.month)

        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def index(request):
    return render(request, "cal/create_event.html", {})
