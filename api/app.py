
from fastapi import FastAPI, HTTPException
import uvicorn
from model import BlogPost
from logger import LogWriter

app = FastAPI()
writer = LogWriter("log")

blog_posts = []

@app.post('/blog')
def create_blog_post(blogPost: BlogPost,status_code=201):
    try:
        
        blog_posts.append(blogPost)
        return {'status':'sucess'}   
    except KeyError:
        writer.log_error("invalid request")
        return HTTPException(400,'Invalid request')
    except Exception as e:
        writer.log_error(str(e))
        return HTTPException(500,f'{e}')


@app.get('/blog')
def get_blog_posts():
    return {'posts': [blog.toJson() for blog in blog_posts]}


@app.get('/blog/{id}')
def get_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            return {'post': post.__dict__}
    writer.log_error("post not found")
    return HTTPException(404,"Post not found")

@app.delete('/blog/{id}')
def delete_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            return {'status':'sucess'}
    writer.log_error("post not found")
    return HTTPException(404,"Post not found")

@app.put('/blog/{id}')
def update_blog_post(id: int,blogPost : BlogPost):
    try:
        for post in blog_posts:
            if post.id == id:
                post.title = blogPost.title
                post.content = blogPost.content
                return {'status':'sucess'}
        writer.log_error("post not found")
        return HTTPException(404,"Post not found")
    except KeyError:
        writer.log_error("invalid request")
        return HTTPException(400,'Invalid request')
    except Exception as e:
        writer.log_error(str(e))
        return HTTPException(500,f'{e}')

if __name__ == '__main__':
    uvicorn.run(app,port=5001,host="0.0.0.0")