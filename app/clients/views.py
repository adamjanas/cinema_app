from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, View

from app.clients.models import Booking, Seat
from app.clients.utils import render_to_pdf
from app.structure.models import Show
from app.users.models import User


class BookingCreateView(CreateView):
    model = Booking
    fields = ["name", "surname", "ticket", "seat"]
    template_name = "app/booking_form.html"
    success_url = reverse_lazy("booking-list")

    def form_valid(self, form):
        show = get_object_or_404(Show, pk=self.kwargs["pk"])
        form.instance.user = self.request.user
        form.instance.show = show
        if form.cleaned_data["seat"] in [book.seat for book in Booking.objects.filter(show=show)]:
            form.add_error("seat", "This seat is taken")
            return self.form_invalid(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = Seat.objects.values_list("id").difference(Booking.objects.values_list("seat"))
        queryset_id = queryset.values_list("id", flat=True)
        context["seats"] = Seat.objects.filter(id__in=queryset_id)
        context["range_column_x"] = range(1, 4)
        context["range_column_y"] = range(4, 7)
        context["rows"] = ["A", "B", "C", "D", "E", "F"]
        return context


class BookingListView(ListView):
    model = Booking
    template_name = "app/booking_list.html"
    context_object_name = "bookings"
    ordering = ["-created_at"]


class UserBookingListView(ListView):
    model = Booking
    template_name = "app/booking_list.html"
    context_object_name = "bookings"
    ordering = ["-created_at"]

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Booking.objects.filter(user=user).order_by("-created_at")


class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy("booking-list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def generate_pdf(request, pk):
    template = get_template("app/pdf.html")
    booking = get_object_or_404(Booking, pk=pk)
    context = {
        "name": booking.name,
        "surname": booking.surname,
        "ticket": booking.ticket,
        "show": booking.show,
        "seat": booking.seat,
    }
    pdf = render_to_pdf("app/pdf.html", context)
    if pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        filename = f"Ticket_{booking.pk}.pdf"
        content = f"inline; filename={filename}"
        download = request.GET.get("download")
        if download:
            content = f"attachment; filename={filename}"
        response["Content-Disposition"] = content
        return response
    return HttpResponse(status=404)
