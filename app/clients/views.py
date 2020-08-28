from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import View
from django.http import HttpResponse
from app.clients.utils import render_to_pdf
from django.template.loader import get_template
from app.structure.models import Show
from app.users.models import User
from app.clients.models import (
Booking,
Seat
)
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)


class BookingCreateView(CreateView):
    model = Booking
    fields = ['name', 'surname', 'ticket', 'seat']
    template_name = 'app/booking_form.html'
    success_message = 'Show was booked.'
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.show = get_object_or_404(Show, pk=self.kwargs['pk'])
        if form.cleaned_data['seat'] in [obj.seat for obj in Booking.objects.all()]:
            form.add_error('seat', 'This seat is taken')
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Seat.objects.values_list('id').difference(Booking.objects.values_list('seat'))
        queryset_id = queryset.values_list('id', flat=True)
        context['seats'] = Seat.objects.filter(id__in=queryset_id)
        return context


class BookingListView(ListView):
    model = Booking
    template_name = 'app/booking_list.html'
    context_object_name = 'bookings'
    ordering = ['-created_at']


class UserBookingListView(ListView):
    model = Booking
    template_name = 'app/booking_list.html'
    context_object_name = 'bookings'
    ordering = ['-created_at']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Booking.objects.filter(user=user).order_by('-created_at')


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def generate_pdf(request, pk):
    template = get_template('app/pdf.html')
    booking = get_object_or_404(Booking, pk=pk)
    context = {
                'name':booking.name,
               'surname': booking.surname,
               'ticket': booking.ticket,
               'show': booking.show,
               'seat': booking.seat,
               }
    html = template.render(context)
    pdf = render_to_pdf('app/pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Ticket_%s.pdf" %("12341231")
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

