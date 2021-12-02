from core.model.entity import Entity


class Background(Entity):

    url = Entity.ndb.StringProperty()
    user_id = Entity.ndb.StringProperty()

    @classmethod
    def get_by_user_id(cls, user_id):
        query = cls.query(cls.user_id == user_id)
        return query.get()
