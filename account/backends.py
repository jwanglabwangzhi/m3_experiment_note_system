from .models import Profile

class CustomUserAuth(object):

    def authenticate(self, username=None, password=None):
        self.username = username
        self.password = password
        try:
            user = Profile.objects.get(email=self.username)
            if user.password ==self.password:
                return user
        except Profile.DoesNotExist:
            return None


    def get_user(self, user_id):
        try:
            user = Profile.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except Profile.DoesNotExist:
            return None