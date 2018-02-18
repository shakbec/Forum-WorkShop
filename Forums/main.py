import models
import stores


def create_member():

    member1 = models.Member("Ahmed", 23)
    member2 = models.Member("Ahmed", 24)
    member3 = models.Member("Waleed", 28)
    print(member1)
    print(member2)
    print(member3)
    print("=" * 30)

    return member1, member2, member3


def adding_to_store(newmembers, member_store):

    for member in newmembers:
        member_store.add(member)


def stores_should_be_similar():

    member_store1 = stores.MembersStore()
    member_store2 = stores.MembersStore()
    if member_store1.get_all() is member_store2.get_all():
        print("Same stores elements !")


def print_all_members(member_store):
    print("=" * 30)

    for member in member_store.get_all():
        print(member)

    print("=" * 30)


def get_by_id_should_retrieve_same_object(member_store, member2):
    member2_retrieved = member_store.get_by_id(member2.id)

    if member2 is member2_retrieved:
        print("member2 and member2_retrieved are matching !")


def update_should_modify_object(member_store, member3):
    member3_copy = models.Member(member3.name, member3.age)
    member3_copy.id = 3

    if member3_copy is not member3:
        print("member3 and member3_copy are not the same !")

    print(member3_copy)
    member3_copy.name = "john"
    member_store.update(member3_copy)
    print(member_store.get_by_id(member3.id))


def filter_by_name(name):
    newlist = member_store.get_by_name(name)
    for names in newlist:
        print names

def catch_exception_when_deleting():
    try:
        member_store.delete(5)
    except ValueError:
        print("It should be an existence entity before deleting !")


newmembers = create_member()
member1, member2, member3 = newmembers

member_store = stores.MembersStore()

adding_to_store(newmembers, member_store)

stores_should_be_similar()

print_all_members(member_store)

get_by_id_should_retrieve_same_object(member_store, member2)

update_should_modify_object(member_store, member3)

catch_exception_when_deleting()

print_all_members(member_store)

filter_by_name("john")
