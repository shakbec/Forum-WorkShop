import models
import stores


post_store = stores.PostsStore()
post_store.add(models.Post("Life", "Life is alawys great", 1))
post_store.add(models.Post("Sunshine", "Sunshine is amazing", 1))
