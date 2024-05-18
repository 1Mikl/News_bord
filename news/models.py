from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAutor = models.SmallIntegerField(default=0)

    def update_rating(self):
        posRat = self.post_set.all().aggregate(postRat=Sum('rating'))
        pRat = 0
        pRat += posRat.get('postRat') if posRat.get('postRat') else 0

        commentRat = self.authorUser.comment_set.all().aggregate(commRat=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commRat') if commentRat.get('commRat') else 0

        self.ratingAuthor = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)


article = "AR"
news = "NS"

POSITIONS = (
    (article, "Статья"),
    (news, "Новость"),
)

class Post(models.Model):
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    position = models.CharField(max_length=2, choices=POSITIONS, default=news)
    dataCreate = models.DateTimeField(auto_now_add=True)
    postCategory = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.title.title()}: {self.text[:20]}'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:124] + "..."


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    commentTime = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()
