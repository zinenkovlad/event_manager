from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer
from .permissions import IsAuthorOrReadOnly


class EventList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        username = self.request.query_params.get('organizer')
        if username is not None:
            queryset = queryset.filter(organizer__username=username)
        return queryset


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventRegistration(APIView):
    def post(self, request, pk):
        event = Event.objects.get(pk=pk)
        user = request.user
        event.attendees.add(user)
        return Response(status=status.HTTP_201_CREATED)
