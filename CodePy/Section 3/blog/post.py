class Post:
    def __init__ ( self, title, content):
        self.title = title
        self.content = content
#Does it depends on itself or others? If it depends only on itself, move to unit folder
    def __repr__(self):
        pass
    def json(self):
        return{
            'title': self.title,
            'content': self.content,
        }
