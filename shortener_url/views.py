from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import redirect

from shortener_url.models import Link
from shortener_url.serializers import LinkSerializer

# Create your views here.


@api_view(['POST'])
def short(request):
    if request.method == 'POST':
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def short_details(request, alias):
    if request.method == 'GET':
        try:
            link = Link.objects.get(alias=alias)
        except Link.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LinkSerializer(link)
        return Response(serializer.data)


def link_to(request, alias):
    try:
        link = Link.objects.get(alias=alias)
    except Link.DoesNotExist:
        raise Http404("Link does not exist")
    return redirect(link.link_to)
