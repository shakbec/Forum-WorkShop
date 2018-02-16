#This file is used to initiate instances of members and posts

class Member:

    def __init__(self, id, name, age):
        self.member_id = id
        self.name = name
        self.age = age


class Post:

    def __init__(self, id, title, body):
        self.post_id = id
        self.title = title
        self.body = body

