
from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from habits.tasks import check_habits
from users.models import User
from users.permissions import UserPermission
from users.serializers import UserSerializer, UserCreateSerializer, MessageSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    Служит для работы с объектом "пользователь"
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    def create(self, request):
        '''
        Создание нового пользователя.
        '''
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserSendMessage(generics.CreateAPIView):
    '''
    Запускает рассылку напоминаний о привычках
    '''
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        '''
        Запускает рассылку напоминаний о привычках
        '''
        check_habits()
