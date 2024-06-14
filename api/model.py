from pydantic import BaseModel


class BlogPost(BaseModel):
    id : int
    title : str
    content : str

    def __str__(self) -> str:
        return f'{self.id} - {self.title} - {self.content}'
    
    def toJson(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}