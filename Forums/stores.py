#This file is used to initiate stores for members and posts
import itertools


class MembersStore:
    members = []
    last_id = 1

    def get_by_name(self, name):
        return (member for member in self.get_all() if member.name == name)



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

    def delete(self, id):
        target = self.get_by_id(id)
        MembersStore.members.remove(target)

    def update(self, member):
        # update member
        result = member
        all_members = self.get_all()
        for index, current_member in enumerate(all_members):
            if current_member.id == member.id:
                all_members[index] = member

        return result

    def get_members_with_posts(self, post_store):
        for member, post in itertools.product(MembersStore.members, post_store):
            if member.id == post.member_id:
                member.posts.append(post)

        for member in MembersStore.members:
            yield member

    def get_top_two(self, post_store):
        membersposts = self.get_members_with_posts(post_store)
        membersposts = sorted(membersposts, key=lambda x: len(x.posts), reverse=True)
        return membersposts[:2]


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

