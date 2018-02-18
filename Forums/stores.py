#This file is used to initiate stores for members and posts


class MembersStore:
    members = []
    last_id = 1

    def get_by_name(self, name):
        all_members = self.get_all()
        similar = []
        for member in all_members:
            if name == member.name:
                similar.append(member)

        return similar



    def get_all(self):
        # get all members
        return MembersStore.members

    def add(self, member):
        # append member
        member.id = MembersStore.last_id
        MembersStore.members.append(member)
        MembersStore.last_id += 1


    def get_by_id(self, id):
        all_members = self.get_all()
        for e in all_members:
            if e.id == id:
                return e

        return None

    def entity_exists(self, member):
        #check if member exists or not
        result = False
        if self.get_by_id(member.id) is not None:
            result = True
            return result

        return result

    def delete(self, id):
        target = self.get_by_id(id)
        MembersStore.members.remove(target)

    def update(self, member):
        # update member
        all_members = self.get_all()
        for object in all_members:
            if object.id == member.id:
                object.name = member.name
                object.age = member.age


class PostsStore:

    posts = []
    last_id = 1

    def get_all(self):
        # get all posts
        return PostsStore.posts

    def add(self, post):
        # append post
        post.id = PostsStore.last_id
        PostsStore.posts.append(post)
        PostsStore.last_id += 1


    def get_by_id(self, id):
        all_posts = self.get_all()
        for e in all_posts:
            if e.id == id:
                return e

            return None

    def entity_exists(self, post):
        #check if post exists or not
        result = False
        if self.get_by_id(post.id) is not None:
            result = True
            return result

        return result

    def delete(self, id):
        target = self.get_by_id(id)
        PostsStore.posts.remove(target)

