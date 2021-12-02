from flask import render_template
from core.model.background import Background
from core.controller.bookmarksCtrl import BookmarksCtrl


class LandingCtrl:

    current_user = None
    background = None
    bookmarks = list()

    def __init__(self, current_user):
        self.current_user = current_user

    def refresh(self):
        if self.current_user.is_authenticated:
            self.background = Background.get_by_user_id(self.current_user.id)
            self.bookmarks = BookmarksCtrl(user_id=self.current_user.id).get_list()

    def render(self):

        if self.current_user.is_authenticated:

            self.refresh()

            return render_template('index.html',
                                   name=self.current_user.name,
                                   email=self.current_user.email,
                                   profile_pic=self.current_user.profile_pic,
                                   background=getattr(self.background, 'url'),
                                   bookmarks=self.bookmarks
                                   )

        else:
            return '<a class="button" href="/login">Google Login</a>'
