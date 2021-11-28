from flask_login import UserMixin

from google.cloud import datastore

datastore_client = datastore.Client()

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

    @staticmethod
    def get(user_id):

        key = datastore_client.key('User', user_id)
        datastore_user = datastore_client.get(key)

        if datastore_user is None:
            return None

        user = User(
            id_=user_id, name=datastore_user["name"], email=datastore_user["email"], profile_pic=datastore_user["profile_pic"]
        )

        return user

    @staticmethod
    def create(id_, name, email, profile_pic):

        entity = datastore.Entity(key=datastore_client.key('User', id_))
        entity.update({
            'name': name,
            'email': email,
            'profile_pic': profile_pic
        })

        datastore_client.put(entity)