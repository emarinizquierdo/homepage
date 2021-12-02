from core.model.bookmark import Bookmark


class BookmarksCtrl:

    user_id = None

    def __init__(self, user_id=None):
        self.user_id = user_id

    def get_list(self):
        return Bookmark.get_list(user_id=self.user_id)
