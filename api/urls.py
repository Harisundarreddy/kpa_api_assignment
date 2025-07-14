from django.urls import path
from api.views import FormDataView

urlpatterns = [
    path('form_data/', FormDataView.as_view(), name='form-data'),
    path('form_data/<int:pk>/', FormDataView.as_view(), name='get-form-data'),
]
