from ecom.models import Car, Brand, CarInventory
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from ecom.forms import CarForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    ordering = ['model']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated and self.request.user.groups.filter(name='Gerente').exists():
            latest_inventory = CarInventory.objects.first()  # Assumindo que está ordenado por -created_at
            context['latest_inventory'] = latest_inventory
        return context

    def get_queryset(self):
        cars = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NewCarView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NewbrandView(CreateView):
    model = Brand
    template_name = 'new_brand.html'
    fields = '__all__'
    success_url = '/new_car/'

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            for field, errors in e.message_dict.items():
                for error in errors:
                    messages.error(self.request, error)
            return self.form_invalid(form)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'


class CarDeleteView(DeleteView):
    model = Car

    template_name = 'car_delete.html'
    success_url = '/cars/'
