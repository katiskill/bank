from django.db import models
from django.urls import reverse

# Create your models here.
class Client(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'

    def get_absolute_url(self):
        return reverse('basicapp:client-list')


class Consultant(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.father_name}'

    def get_absolute_url(self):
        return reverse('basicapp:consultant-list')


class Operation(models.Model):
    client = models.ForeignKey(Client, related_name='operations', null=True, on_delete=models.SET_NULL)
    consultant = models.ForeignKey(Consultant, related_name='operations', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.id}: {self.name} by {self.client}'

    def get_absolute_url(self):
        return reverse('basicapp:operation-list')


class OperationType(models.Model):
    operation = models.OneToOneField(Operation, related_name='type', on_delete=models.CASCADE)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('basicapp:operation-type-list')


class OperationCost(models.Model):
    operation = models.OneToOneField(Operation, related_name='cost', on_delete=models.CASCADE)
    cost = models.FloatField()

    def __str__(self):
        return f'{self.cost} {self.operation}'

    def get_absolute_url(self):
        return reverse('basicapp:operation-cost-list')


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class OperationStatus(models.Model):
    operation = models.OneToOneField(Operation, related_name='status', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, related_name='operations', on_delete=models.DO_NOTHING)
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.status}, {self.start_time} - {self.end_time}'

    def get_absolute_url(self):
        return reverse('basicapp:operation-status-list')
