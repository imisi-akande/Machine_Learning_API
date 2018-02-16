from django.db.models import Q
from django.shortcuts import render
# detector/views.py
from rest_framework import generics
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from . import models
from . import serializers

# Create your views here.
class DetectorList(generics.ListAPIView):
    # queryset = models.News.objects.all()
    serializer_class = serializers.DetectorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['fakeness',]
    def get_queryset(self):
        queryset = models.News.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            queryset= queryset.filter(Q(headline__icontains=query) 
            | Q(body__icontains=query)).distinct()
        return queryset
    
class DetectorDetail(generics.RetrieveAPIView):
    queryset = models.News.objects.all()
    serializer_class = serializers.DetectorSerializer

from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    """
      Get the view for the home page
      :param request: The request object
      :return: Returns the default homepage view
    """
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('index.html', context_dict, context)