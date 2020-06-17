from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from .models import Client, Consultant, Operation, OperationCost, OperationType, OperationStatus
from .forms import OperationStatusModelForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


# ListViews
class ClientListView(ListView):
    model = Client

    def get_queryset(self):
        id = self.request.GET.get('id')
        ln = self.request.GET.get('ln')
        fn = self.request.GET.get('fn')
        ftn = self.request.GET.get('ftn')
        ph = self.request.GET.get('ph')
        o_id = self.request.GET.get('o_id')
        o_ln = self.request.GET.get('o_ln')
        o_fn = self.request.GET.get('o_fn')
        o_ftn = self.request.GET.get('o_ftn')
        o_ph = self.request.GET.get('o_ph')
        ordering = []
        object_list = self.model.objects.all()

        if id:
            object_list = object_list.filter(id__iexact=id)
        if ln:
            object_list = object_list.filter(last_name__icontains=ln)
        if fn:
            object_list = object_list.filter(first_name__icontains=fn)
        if ftn:
            object_list = object_list.filter(father_name__icontains=ftn)
        if ph:
            object_list = object_list.filter(phone__icontains=ph)

        if o_id == '1':
            ordering.append('id')
        elif o_id == '2':
            ordering.append('-id')
        if o_ln == '1':
            ordering.append('last_name')
        elif o_ln == '2':
            ordering.append('-last_name')
        if o_fn == '1':
            ordering.append('first_name')
        elif o_fn == '2':
            ordering.append('-first_name')
        if o_ftn == '1':
            ordering.append('father_name')
        elif o_ftn == '2':
            ordering.append('-father_name')
        if o_ph == '1':
            ordering.append('phone')
        elif o_ph == '2':
            ordering.append('-phone')
        object_list = object_list.order_by(*ordering)

        return object_list


class ConsultantListView(ListView):
    model = Consultant

    def get_queryset(self):
        id = self.request.GET.get('id')
        ln = self.request.GET.get('ln')
        fn = self.request.GET.get('fn')
        ftn = self.request.GET.get('ftn')
        o_id = self.request.GET.get('o_id')
        o_ln = self.request.GET.get('o_ln')
        o_fn = self.request.GET.get('o_fn')
        o_ftn = self.request.GET.get('o_ftn')
        ordering = []
        object_list = self.model.objects.all()

        if id:
            object_list = object_list.filter(id__iexact=id)
        if ln:
            object_list = object_list.filter(last_name__icontains=ln)
        if fn:
            object_list = object_list.filter(first_name__icontains=fn)
        if ftn:
            object_list = object_list.filter(father_name__icontains=ftn)

        if o_id == '1':
            ordering.append('id')
        elif o_id == '2':
            ordering.append('-id')
        if o_ln == '1':
            ordering.append('last_name')
        elif o_ln == '2':
            ordering.append('-last_name')
        if o_fn == '1':
            ordering.append('first_name')
        elif o_fn == '2':
            ordering.append('-first_name')
        if o_ftn == '1':
            ordering.append('father_name')
        elif o_ftn == '2':
            ordering.append('-father_name')
        object_list = object_list.order_by(*ordering)

        return object_list


class OperationListView(ListView):
    model = Operation

    def get_queryset(self):
        id = self.request.GET.get('id')
        cl = self.request.GET.get('cl')
        co = self.request.GET.get('co')
        nm = self.request.GET.get('nm')
        o_id = self.request.GET.get('o_id')
        o_cl = self.request.GET.get('o_cl')
        o_co = self.request.GET.get('o_co')
        o_nm = self.request.GET.get('o_nm')
        ordering = []
        object_list = self.model.objects.all()

        if id:
            object_list = object_list.filter(id__iexact=id)
        if cl:
            object_list = object_list.filter(client__id__iexact=cl)
        if co:
            object_list = object_list.filter(consultant__id__iexact=co)
        if nm:
            object_list = object_list.filter(name__icontains=nm)

        if o_id == '1':
            ordering.append('id')
        elif o_id == '2':
            ordering.append('-id')
        if o_cl == '1':
            ordering.append('client__id')
        elif o_cl == '2':
            ordering.append('-client__id')
        if o_co == '1':
            ordering.append('consultant__id')
        elif o_co == '2':
            ordering.append('-consultant__id')
        if o_nm == '1':
            ordering.append('name')
        elif o_nm == '2':
            ordering.append('-name')
        object_list = object_list.order_by(*ordering)

        return object_list


class OperationTypeListView(ListView):
    model = OperationType

    def get_queryset(self):
        op_id = self.request.GET.get('op_id')
        tp = self.request.GET.get('tp')
        o_op_id = self.request.GET.get('o_op_id')
        o_tp = self.request.GET.get('o_tp')
        ordering = []
        object_list = self.model.objects.all()

        if op_id:
            object_list = object_list.filter(operation__id__iexact=op_id)
        if tp:
            object_list = object_list.filter(type__icontains=tp)

        if o_op_id == '1':
            ordering.append('operation__id')
        elif o_op_id == '2':
            ordering.append('-operation__id')
        if o_tp == '1':
            ordering.append('type')
        elif o_tp == '2':
            ordering.append('-type')
        object_list = object_list.order_by(*ordering)

        return object_list


class OperationCostListView(ListView):
    model = OperationCost

    def get_queryset(self):
        op_id = self.request.GET.get('op_id')
        c = self.request.GET.get('c')
        o_op_id = self.request.GET.get('o_op_id')
        o_c = self.request.GET.get('o_c')
        ordering = []
        object_list = self.model.objects.all()

        if op_id:
            object_list = object_list.filter(operation__id__iexact=op_id)
        if c:
            object_list = object_list.filter(cost__icontains=c)

        if o_op_id == '1':
            ordering.append('operation__id')
        elif o_op_id == '2':
            ordering.append('-operation__id')
        if o_c == '1':
            ordering.append('cost')
        elif o_c == '2':
            ordering.append('-cost')
        object_list = object_list.order_by(*ordering)

        return object_list


class OperationStatusListView(ListView):
    model = OperationStatus

    def get_queryset(self):
        op_id = self.request.GET.get('op_id')
        s = self.request.GET.get('s')
        st_t = self.request.GET.get('st_t')
        e_t = self.request.GET.get('e_t')
        o_op_id = self.request.GET.get('o_op_id')
        o_s = self.request.GET.get('o_s')
        o_st_t = self.request.GET.get('o_st_t')
        o_e_t = self.request.GET.get('o_e_t')
        ordering = []
        object_list = self.model.objects.all()

        if op_id:
            object_list = object_list.filter(operation__id__iexact=op_id)
        if s:
            object_list = object_list.filter(status__icontains=s)
        if st_t:
            object_list = object_list.filter(start_time__icontains=st_t)
        if e_t:
            object_list = object_list.filter(end_time__icontains=e_t)

        if o_op_id == '1':
            ordering.append('operation__id')
        elif o_op_id == '2':
            ordering.append('-operation__id')
        if o_s == '1':
            ordering.append('status')
        elif o_s == '2':
            ordering.append('-status')
        if o_st_t == '1':
            ordering.append('start_time')
        elif o_st_t == '2':
            ordering.append('-start_time')
        if o_e_t == '1':
            ordering.append('end_time')
        elif o_e_t == '2':
            ordering.append('-end_time')
        object_list = object_list.order_by(*ordering)

        return object_list


# CreateViews
class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'


class ConsultantCreateView(CreateView):
    model = Consultant
    fields = '__all__'


class OperationCreateView(CreateView):
    model = Operation
    fields = '__all__'


class OperationTypeCreateView(CreateView):
    model = OperationType
    fields = '__all__'


class OperationCostCreateView(CreateView):
    model = OperationCost
    fields = '__all__'


class OperationStatusCreateView(CreateView):
    model = OperationStatus
    form_class = OperationStatusModelForm


# UpdateViews
class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'


class ConsultantUpdateView(UpdateView):
    model = Consultant
    fields = '__all__'


class OperationUpdateView(UpdateView):
    model = Operation
    fields = '__all__'


class OperationTypeUpdateView(UpdateView):
    model = OperationType
    fields = '__all__'


class OperationCostUpdateView(UpdateView):
    model = OperationCost
    fields = '__all__'


class OperationStatusUpdateView(UpdateView):
    model = OperationStatus
    form_class = OperationStatusModelForm


# DeleteViews
class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('basicapp:client-list')


class ConsultantDeleteView(DeleteView):
    model = Consultant
    success_url = reverse_lazy('basicapp:consultant-list')


class OperationDeleteView(DeleteView):
    model = Operation
    success_url = reverse_lazy('basicapp:operation-list')


class OperationTypeDeleteView(DeleteView):
    model = OperationType
    success_url = reverse_lazy('basicapp:operation-type-list')


class OperationCostDeleteView(DeleteView):
    model = OperationCost
    success_url = reverse_lazy('basicapp:operation-cost-list')


class OperationStatusDeleteView(DeleteView):
    model = OperationStatus
    success_url = reverse_lazy('basicapp:operation-status-list')
