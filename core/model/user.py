from flask_login import UserMixin
from google.cloud import ndb

from core.model.entity import Entity


class User(UserMixin, Entity):

    name = ndb.StringProperty()
    email = ndb.StringProperty()
    profile_pic = ndb.StringProperty()

    def get_id(self):
        return str(self.id)