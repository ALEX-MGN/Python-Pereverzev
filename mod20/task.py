from sqlalchemy import Table, MetaData, create_engine, Column, Integer, String, Date, DateTime, Float, Boolean
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime, timedelta
from flask import Flask, jsonify, request

app = Flask(__name__)
engine = create_engine("sqlite:///python.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, default="1")
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_students_live_dormitory(cls):
        return session.query(Student).filter(Student.scholarship == True).all()

    @classmethod
    def get_students_average_score_more(cls, avg_score):
        return session.query(Student).filter(Student.average_score > avg_score).all()

class Receiving_book(Base):
    __tablename__ = 'receiving_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def count_date_with_book(self):
        if self.date_of_return is None:
            return datetime.now - self.date_of_issue
        else:
            return self.date_of_return - self.date_of_issue

@app.before_request
def before_request_func():
    Base.metadata.create_all(bind=engine)


@app.route('/')
def hello():
    return "Hello World"

@app.route('/get_all_books')
def get_all_books():
    books = session.query(Book).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200

@app.route('/get_debtor')
def get_debtor():
    books = session.query(Receiving_book).filter(Receiving_book.date_of_issue < datetime.now() - timedelta(days=14)).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200


@app.route('/issue_book', methods=['POST'])
def issue_book():
    book_id = request.form.get('book_id', type=int)
    student_id = request.form.get('student_id', type=int)
    new_issue = Receiving_book(book_id=book_id,
                               student_id=student_id,
                               date_of_issue=datetime.strptime(datetime.now, '%Y-%m-%d %H:%M:%S:%f'))
    session.add(new_issue)
    session.commit()
    return "Книга выдана", 201


@app.route('/pass_book', methods=['POST'])
def pass_book():
    try:
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        book = session.query(Receiving_book).filter(Receiving_book.book_id == book_id).filter((Receiving_book.student_id == student_id)).one()
        book.date_of_return = datetime.now
        session.commit()
        return "Книга сдана"
    except NoResultFound:
        return "Введены некорректные значения"


@app.route('/get_books_by_name/<string:name>')
def get_books_by_name(name):
    books = session.query(Book).filter(Book.name.like(f"%{name}%")).all()
    books_list = []
    for book in books:
        books_list.append(book.to_json())
    return jsonify(books_list=books_list), 200

if __name__ == "__main__":
    app.run()

