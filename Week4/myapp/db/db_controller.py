from myapp.db.models import Post

class getList:
    def getMost(cnt):
        return Post.objects.order_by('-views')[0:cnt]

    def getRecent(cnt):
        return Post.objects.order_by('-postId')[0:cnt]