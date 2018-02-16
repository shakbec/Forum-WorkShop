import models, stores

mems = stores.MembersStore()
psts = stores.PostsStore()

member1 = models.Member("ahmed", 24)
member2 = models.Member("khalid", 24)

post1 = models.Post("First Post", "This is the first post ever.")
post2 = models.Post("Python Programming", "Python programming is fun.")
post3 = models.Post("Models and Instances", "This part of coding is very interesting!")

mems.add(member1)
mems.add(member2)

print mems.get_all()
print mems.get_by_id(2)
print mems.entity_exists(member1)
mems.delete(1)
print mems.get_all()
print 40*"#"

psts.add(post1)
psts.add(post2)
print psts.get_all()
print psts.get_by_id(1)
print psts.entity_exists(post3)
psts.delete(1)
print psts.get_all()

