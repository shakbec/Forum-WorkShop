#This file is used to initiate instances of members and posts
import datetime


class Member:

    def __init__(self, name, age):
        self.id = 0
        self.name = name
        self.age = age
        self.posts = []

    def __str__(self):
        return 'Id: {}, Name: {}, Age: {}'.format(self.id, self.name, self.age)

    def __repr__(self):
        return 'Id: {}, Name: {}, Age: {}'.format(self.id, self.name, self.age)


class Post:

    def __init__(self, title, body, member_id):
        self.id = 0
        self.title = title
        self.body = body
        self.member_id = member_id
        self.date = datetime.datetime.now()

    def __str__(self):
        return 'Id: {}, Title: {}, Body: {}, Member Id: {}, Date&Time: {}'.format(self.id, self.title, self.body, self.member_id, self.date)

    def __repr__(self):
        return 'Id: {}, Title: {}, Body: {}, Member Id: {}, Date&Time: {}'.format(self.id, self.title, self.body, self.member_id, self.date)
