from base_service import BaseService
from users.models import Users


class UserService(BaseService):
    model = Users
