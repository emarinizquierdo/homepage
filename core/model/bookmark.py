from core.model.entity import Entity


class Bookmark(Entity):

    name = Entity.ndb.StringProperty()
    url = Entity.ndb.StringProperty()
    user_id = Entity.ndb.StringProperty()

    @classmethod
    def get_list(cls, user_id):
        query = cls.query(cls.user_id == user_id)
        return query.fetch()