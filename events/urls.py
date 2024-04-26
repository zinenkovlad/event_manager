from django.urls import path

from .views import EventList, EventDetail, EventRegistration

urlpatterns = [
    path('<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('<int:pk>/register/', EventRegistration.as_view(), name='event_registration'),
    path('', EventList.as_view(), name='event_list')
]
