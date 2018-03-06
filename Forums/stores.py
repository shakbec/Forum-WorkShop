#This file is used to initiate stores for members and posts
import itertools
import copy


class BaseStore():

    def __init__(self, data_provider, last_id):
        self._data_provider = data_provider
        self._last_id = last_id

    def get_all(self):
        return self._data_provider

    def add(self, item_instance):
        item_instance.id = self._last_id
        self._data_provider.append(item_instance)
        self._last_id += 1

    def get_by_id(self, id):
        all_instances = self.get_all()
        for e in all_instances:
            if e.id == id:
                return e
        return None

    def entity_exists(self, item_instance):
        #check if item exists or not
        result = False
        if self.get_by_id(item_instance.id) is not None:
            result = True

        return result

    def delete(self, id):
        target = self.get_by_id(id)
        self._data_provider.remove(target)

    def update(self, item_instance):
        # update
        result = item_instance
        all_instances = self.get_all()
        for index, current_instance in enumerate(all_instances):
            if current_instance.id == item_instance.id:
                all_instances[index] = item_instance

        return result

class MembersStore(BaseStore, object):
    members = []
    last_id = 1

    def __init__(self):
        super(MembersStore, self).__init__(MembersStore.members, MembersStore.last_id)

    def get_by_name(self, name):
        return (member for member in self.get_all() if member.name == name)

    def get_members_with_posts(self, post_store):
        all_members = copy.deepcopy(self.get_all())
        for member, post in itertools.product(all_members, post_store):
            if member.id == post.member_id:
                member.posts.append(post)

        return all_members

    def get_top_two(self, post_store):
        members_with_posts = list(self.get_members_with_posts(post_store))

        members_with_posts.sort(key=lambda member: len(member.posts), reverse=True)

        yield members_with_posts[0]
        yield members_with_posts[1]


class PostsStore(BaseStore, object):
    posts = []
    last_id = 1

    def __init__(self):
        super(PostsStore, self).__init__(PostsStore.posts, PostsStore.last_id)

    def get_posts_by_date(self):
        all_posts = copy.deepcopy(self.get_all())
        all_posts.sort(key=lambda post: post.date, reverse=True)
        return all_posts
