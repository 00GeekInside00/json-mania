from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import (CreateView, DeleteView)
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import (Storage, Project)
from .storage_serializers import (StorageSerializer, StorageWriteSerializer)
from .project_serializers import (ProjectSerializer, ProjectWriteSerializer)



class UserStorageHandling(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, storage_url, storage_id):
        storage = Storage.objects.get(url=storage_url, storage_id=storage_id)
        request.data['creator'] = storage.creator.id
        serializer = StorageWriteSerializer(storage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, storage_url, storage_id, format=None):
        queryset = Storage.objects.get(url=storage_url, storage_id=storage_id)
        serializer_class = StorageSerializer(queryset)
        return Response(serializer_class.data)

    def put(self, request, storage_url, storage_id):
        storage = Storage.objects.get(url=storage_url, storage_id=storage_id)
        request.data['creator']=storage.creator.id
        serializer = StorageWriteSerializer(storage,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, storage_url, storage_id):
        storage = Storage.objects.get(url=storage_url, storage_id=storage_id)
        request.data['creator'] = storage.creator.id
        serializer = StorageWriteSerializer(storage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, storage_url, storage_id):
        storage = Storage.objects.get(url=storage_url, storage_id=storage_id)
        storage.data=None
        storage.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@method_decorator(login_required, name='dispatch')
class StorageCreation(CreateView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    model = Storage
    template_name = 'Create.html'
    fields = ['data','url']
    

    def post(self, request):
        try:
            if request.POST.get('url',False) and request.POST.get('project',False):
                project_id = int(request.POST['project'])
                StorageCreated = Storage(
                    data={}, creator=request.user, project=Project.objects.get(id=project_id), url=request.POST['url'])
                StorageCreated.save()
                return redirect('/storage/list/')
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@method_decorator(login_required, name='dispatch')
class StorageList(ListView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    model = Storage
    template_name='ListEndpoints.html'
    context_object_name = 'storage'

    def get_queryset(self):
        return self.model.objects.filter(creator=self.request.user.id)


@method_decorator(login_required, name='dispatch')
class StorageDeletion(DeleteView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    model=Storage
    template_name = 'DeleteEndpoint.html'
    success_url = reverse_lazy('StrorageList')


@method_decorator(login_required, name='dispatch')
class ProjectHandling(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        try:
            queryset = Project.objects.filter(creator=request.user)
            serializer_class = ProjectSerializer(queryset,many=True)
            return Response(serializer_class.data)
        except:
            return Response()

    def post(self, request, format=None):
        print(request.data)
        project = Project(creator=request.user)
        serializer = ProjectWriteSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(login_required, name='dispatch')
class ProjectDeletion(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk, format=None):
        print(request)
        project = Project.objects.get(id=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def home(request):
    return redirect('/storage/list/')