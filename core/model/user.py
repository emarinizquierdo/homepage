from flask_login import UserMixin
from google.cloud import ndb


class User(UserMixin, ndb.Model):

    name = ndb.StringProperty()
    email = ndb.StringProperty()
    profile_pic = ndb.StringProperty()

    @property
    def id(self):
        return self.key.id()

    @staticmethod
    def get( user_id):

        user = User.get_by_id(user_id)

        if user is None:
            return None

        return user

    def get_id(self):
        return str(self.id)

    @staticmethod
    def create(id_, name, email, profile_pic):

        key = ndb.Key(User, id_)
        user = User()
        user.key = key
        user.name = name
        user.email = email
        user.profile_pic = profile_pic
        user.put()