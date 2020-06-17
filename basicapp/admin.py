from django.contrib import admin

from .models import Client, Consultant, Operation, OperationCost, OperationType, OperationStatus, Status

# Register your models here.
class OperationCostInline(admin.TabularInline):
    model = OperationCost
    extra = 1


class OperationTypeInline(admin.TabularInline):
    model = OperationType
    extra = 0


class OperationStatusInline(admin.TabularInline):
    model = OperationStatus
    extra = 0


class OperationInline(admin.StackedInline):
    model = Operation
    extra = 0


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    inlines = [
        OperationTypeInline,
        OperationCostInline,
        OperationStatusInline,
    ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [OperationInline]


@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    inlines = [OperationInline]


admin.site.register(Status)
admin.site.register(OperationCost)
admin.site.register(OperationType)
admin.site.register(OperationStatus)
