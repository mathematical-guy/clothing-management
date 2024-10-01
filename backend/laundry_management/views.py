from rest_framework import viewsets, decorators, response, status
from laundry_management.models import LaundryCloth, LaundryEvent
from laundry_management.serializers import LaundryEventClothListSerializer, AddLaundryClothSerializer, \
    LaundryEventSerializer, MarkClothReadySerializer


class LaundryEventViewSet(viewsets.ModelViewSet):
    queryset = LaundryEvent.objects.all()
    serializer_class = LaundryEventSerializer
    http_method_names = ["get", "post", "patch", "put"]

    @decorators.action(methods=["GET", "POST"], detail=True)
    def clothes(self, request, *args, **kwargs):
        event: LaundryEvent = self.get_object()
        if request.method.upper() == "GET":
            laundry_clothes = event.laundry_event_clothes.all()
            return response.Response(
                data=LaundryEventClothListSerializer(instance=laundry_clothes, many=True).data,
                status=status.HTTP_200_OK,
            )

        else:
            data: dict = request.data
            data.update({"laundry": event.id})
            serializer = AddLaundryClothSerializer(data=data)
            if not serializer.is_valid():
                return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return response.Response(data=serializer.data, status=status.HTTP_200_OK)


class LaundryClothViewSet(viewsets.ModelViewSet):
    queryset = LaundryCloth.objects.all()
    serializer_class = LaundryEventClothListSerializer
    http_method_names = ["get", "post", "patch", "put"]

    def get_serializer_class(self):
        if self.action == 'create':
            return AddLaundryClothSerializer
        return self.serializer_class

    @decorators.action(methods=["PATCH"], detail=True)
    def mark_ready(self, request, *args, **kwargs):
        cloth: LaundryCloth = self.get_object()
        serializer = MarkClothReadySerializer(instance=cloth, data=request.data)
        if not serializer.is_valid():
            return response.Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

