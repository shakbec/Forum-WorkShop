#This file is used to initiate stores for members and posts


class MembersStore:
    members = []
    last_id = 1

    def get_all(self):
        # get all members
        return MembersStore.members

    def add(self, member):
        # append member
        member.member_id = MembersStore.last_id
        MembersStore.members.append(member)
        MembersStore.last_id += 1


    def get_by_id(self, member_id):
        all_members = self.get_all()
        for e in all_members:
            if e.member_id == member_id:
                return e

        return False

    def entity_exists(self, member):
        #check if member exists or not
        result = self.get_by_id(member.member_id)
        if result:
            return True

        return False

    def delete(self, member_id):
        target = self.get_by_id(member_id)
        MembersStore.members.remove(target)


class PostsStore:

    posts = []
    last_id = 1

    def get_all(self):
        # get all posts
        return PostsStore.posts

    def add(self, post):
        # append post
        post.post_id = PostsStore.last_id
        PostsStore.posts.append(post)
        PostsStore.last_id += 1


    def get_by_id(self, post_id):
        all_posts = self.get_all()
        for e in all_posts:
            if e.post_id == post_id:
                return e
            else:
                return False

    def entity_exists(self, post):
        #check if post exists or not
        result = self.get_by_id(post.post_id)
        if result:
            return True

        return False

    def delete(self, post_id):
        target = self.get_by_id(post_id)
        PostsStore.posts.remove(target)

