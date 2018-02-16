class MembersStore:
    members = []

    def get_all(self):
        # get all members
        return self.members

    def add(self, member):
        # append member
        self.members.append(member)
        return


class PostStore:

    posts = []

    def get_all(self):
        # get all posts
        return self.posts

    def add(self, post):
        # append member
        self.posts.append(post)
        return
