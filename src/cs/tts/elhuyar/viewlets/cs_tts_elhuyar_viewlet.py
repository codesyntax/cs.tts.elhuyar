from plone.app.layout.viewlets import ViewletBase


class CSTTSElhuyarViewlet(ViewletBase):

    def update(self):
        self.message = self.get_message()

    def get_message(self):
        return 'My message'

    def index(self):
        return super().render()
