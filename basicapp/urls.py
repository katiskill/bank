from django.urls import path

from . import views


app_name = 'basicapp'
urlpatterns = [
    # Basic View
    path('', views.index, name='index'),
    # ListViews
    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('consultants/', views.ConsultantListView.as_view(), name='consultant-list'),
    path('operations/', views.OperationListView.as_view(), name='operation-list'),
    path('operation_types/', views.OperationTypeListView.as_view(), name='operation-type-list'),
    path('operation_costs/', views.OperationCostListView.as_view(), name='operation-cost-list'),
    path('operation_statuses/', views.OperationStatusListView.as_view(), name='operation-status-list'),
    # CreateViews
    path('clients/create/', views.ClientCreateView.as_view(), name='client-create'),
    path('consultants/create/', views.ConsultantCreateView.as_view(), name='consultant-create'),
    path('operations/create/', views.OperationCreateView.as_view(), name='operation-create'),
    path('operation_types/create/', views.OperationTypeCreateView.as_view(), name='operation-type-create'),
    path('operation_costs/create/', views.OperationCostCreateView.as_view(), name='operation-cost-create'),
    path('operation_statuses/create/', views.OperationStatusCreateView.as_view(), name='operation-status-create'),
    # UpdateViews
    path('clients/update/<int:pk>/', views.ClientUpdateView.as_view(), name='client-update'),
    path('consultants/update/<int:pk>/', views.ConsultantUpdateView.as_view(), name='consultant-update'),
    path('operations/update/<int:pk>/', views.OperationUpdateView.as_view(), name='operation-update'),
    path('operation_types/update/<int:pk>/', views.OperationTypeUpdateView.as_view(), name='operation-type-update'),
    path('operation_costs/update/<int:pk>/', views.OperationCostUpdateView.as_view(), name='operation-cost-update'),
    path('operation_statuses/update/<int:pk>/', views.OperationStatusUpdateView.as_view(), name='operation-status-update'),
    # DeleteViews
    path('clients/delete/<int:pk>/', views.ClientDeleteView.as_view(), name='client-delete'),
    path('consultants/delete/<int:pk>/', views.ConsultantDeleteView.as_view(), name='consultant-delete'),
    path('operations/delete/<int:pk>/', views.OperationDeleteView.as_view(), name='operation-delete'),
    path('operation_types/delete/<int:pk>/', views.OperationTypeDeleteView.as_view(), name='operation-type-delete'),
    path('operation_costs/delete/<int:pk>/', views.OperationCostDeleteView.as_view(), name='operation-cost-delete'),
    path('operation_statuses/delete/<int:pk>/', views.OperationStatusDeleteView.as_view(), name='operation-status-delete'),
]
