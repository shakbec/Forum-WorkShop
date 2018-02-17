#This file is used to initiate instances of members and posts


class Member:

    def __init__(self, name, age):
        self.member_id = 0
        self.name = name
        self.age = age

    def __str__(self):
        return 'Id: {}, Name: {}, Age: {}'.format(self.member_id, self.name, self.age)


class Post:

    def __init__(self, title, body):
        self.post_id = 0
        self.title = title
        self.body = body

    def __str__(self):
        return 'Id: {}, Title: {}, Body: {}'.format(self.post_id, self.title, self.body)
