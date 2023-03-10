from flask import Flask
from flask_restful import Api, Resource, reqparse
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker


app = Flask(__name__)
api = Api(app)

Base = declarative_base()

engine = create_engine('mysql+pymysql://f49g9a0xaxsdqh45i6m6:pscale_pw_gUnuTFqy1temlcCWcNasRblkvYnuYTLZpLaGhz6WPEs@us-east.connect.psdb.cloud/shedflow?sslaccept=strict', echo=True)

Session = sessionmaker(bind=engine)

fake = Faker()


# Define the blog model
class Blog(Base):
    __tablename__ = 'Blog'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(String(2048), nullable=False)
    author = Column(String(255), nullable=False)
    timeStamp = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"<Blog(id={self.id}, title='{self.title}', content='{self.content}', author='{self.author}', timeStamp='{self.timeStamp}')>"


Base.metadata.create_all(engine)


# Create a new Flask-RESTful Resource for blogs
class Blog(Resource):
    def get(self):
        try:
            session = Session()
            blogs = session.query(Blog).all()
            result = []
            for blog_post in blogs:
                result.append({
                    'id': blog_post.id,
                    'title': blog_post.title,
                    'content': blog_post.content,
                    'author': blog_post.author,
                    'timeStamp': str(blog_post.timeStamp)
                })
            return {'status': 'success', 'data': result}
        except Exception as e:
            return {'error': str(e)}

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, help='Title of the blog post', required=True)
            parser.add_argument('content', type=str, help='Content of the blog post', required=True)
            parser.add_argument('author', type=str, help='Author of the blog post', required=True)
            args = parser.parse_args()
            session = Session()
            blog_post = Blog(title=args['title'], content=args['content'], author=args['author'])
            session.add(blog_post)
            session.commit()
            return {'status': 'success'}
        except Exception as e:
            return {'error': str(e)}


api.add_resource(Blog, '/api/blog')


def generate_fake_blogs(num_blogs=10):
    fake = Faker()
    for _ in range(num_blogs):
        title = fake.sentence()
        content = fake.text(max_nb_chars=2048)
        author = fake.name()
        timeStamp = fake.date_time_this_year()
        session = Session()
        blog = Blog(title=title, content=content, author=author, timeStamp=timeStamp)
        session.add(blog)
        session.commit()


generate_fake_blogs()


if __name__ == '__main__':
    app.run(debug=True)
