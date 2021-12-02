from google.cloud import ndb
import time


class Entity(ndb.Model):

    ndb = ndb
    timestamp = ndb.IntegerProperty()

    @property
    def id(self):
        return self.key.id()

    def _pre_put_hook(self):
        self.timestamp = int(round(time.time() * 1000))

    @classmethod
    def get(cls, id):

        return cls.get_by_id(id)
