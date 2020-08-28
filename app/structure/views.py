from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from app.structure.models import (
    Advertisement,
    Promotion,
    Price,
    Hall,
    Seat,
    Movie,
    Show,
)
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)


class TestFuncMixin(object):

    def test_func(self):
        object = self.get_object()
        if self.request.user == object.author:
            return True
        return False


class AdvertisementCreateView(CreateView):
    model = Advertisement
    fields = ['name', 'content']
    template_name = 'app/ad_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'app/home.html'
    context_object_name = 'advertisements'
    ordering = ['-created_at']


class AdvertisementUpdateView(TestFuncMixin, UpdateView):
    model = Advertisement
    fields = ['name', 'content']
    template_name = 'app/ad_form.html'
    success_url = '/'


class AdvertisementDeleteView(TestFuncMixin, DeleteView):
    model = Advertisement
    success_url = '/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class PromotionCreateView(CreateView):
    model = Promotion
    fields = ['name', 'content']
    template_name = 'app/promo_form.html'
    success_url = reverse_lazy('promo-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PromotionListView(ListView):
    model = Promotion
    template_name = 'app/promo_list.html'
    context_object_name = 'promotions'
    ordering = ['-created_at']


class PromotionUpdateView(TestFuncMixin, UpdateView):
    model = Promotion
    fields = ['name', 'content']
    template_name = 'app/promo_form.html'
    success_url = reverse_lazy('promo-list')


class PromotionDeleteView(TestFuncMixin, DeleteView):
    model = Promotion
    success_url = reverse_lazy('promo-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class PriceCreateView(CreateView):
    model = Price
    fields = ['name', 'value']
    template_name = 'app/price_form.html'
    success_url = reverse_lazy('price-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PriceListView(ListView):
    model = Price
    template_name = 'app/price_list.html'
    context_object_name = 'prices'
    ordering = ['-created_at']


class PriceUpdateView(TestFuncMixin, UpdateView):
    model = Price
    fields = ['name', 'value']
    template_name = 'app/price_form.html'
    success_url = reverse_lazy('price-list')


class PriceDeleteView(TestFuncMixin, DeleteView):
    model = Price
    success_url = reverse_lazy('price-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class MovieCreateView(CreateView):
    model = Movie
    fields = ['name', 'content']
    template_name = 'app/movie_form.html'
    success_url = reverse_lazy('movie-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MovieListView(ListView):
    model = Movie
    template_name = 'app/movie_list.html'
    context_object_name = 'movies'
    ordering = ['-created_at']

class MovieUpdateView(TestFuncMixin, UpdateView):
    model = Movie
    fields = ['name', 'content']
    template_name = 'app/movie_form.html'
    success_url = reverse_lazy('movie-list')


class MovieDeleteView(TestFuncMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy('price-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class HallCreateView(CreateView):
    model = Hall
    fields = ['name']
    template_name = 'app/hall_form.html'
    success_url = reverse_lazy('hall-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class HallListView(ListView):
    model = Hall
    template_name = 'app/hall_list.html'
    context_object_name = 'halls'
    ordering = ['-created_at']

class HallUpdateView(TestFuncMixin, UpdateView):
    model = Hall
    fields = ['name']
    template_name = 'app/hall_form.html'
    success_url = reverse_lazy('hall-list')


class HallDeleteView(TestFuncMixin, DeleteView):
    model = Hall
    success_url = reverse_lazy('hall-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class SeatCreateView(CreateView):
    model = Seat
    fields = ['row', 'column']
    template_name = 'app/seat_form.html'
    success_url = reverse_lazy('seat-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SeatListView(ListView):
    model = Seat
    template_name = 'app/seat_list.html'
    context_object_name = 'seats'
    ordering = ['-created_at']

class SeatUpdateView(TestFuncMixin, UpdateView):
    model = Seat
    fields = ['row', 'column']
    template_name = 'app/seat_form.html'
    success_url = reverse_lazy('seat-list')


class SeatDeleteView(TestFuncMixin, DeleteView):
    model = Seat
    success_url = reverse_lazy('seat-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ShowCreateView(CreateView):
    model = Show
    fields = ['movie', 'hall', 'date']
    template_name = 'app/show_form.html'
    success_url = reverse_lazy('show-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ShowListView(ListView):
    model = Show
    template_name = 'app/show_list.html'
    context_object_name = 'shows'
    ordering = ['-created_at']


class ShowUpdateView(TestFuncMixin, UpdateView):
    model = Show
    fields = ['movie', 'hall', 'date']
    template_name = 'app/show_form.html'
    success_url = reverse_lazy('show-list')


class ShowDeleteView(TestFuncMixin, DeleteView):
    model = Show
    success_url = reverse_lazy('show-list')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

