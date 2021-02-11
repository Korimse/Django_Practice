from django.db import models


class DJuser(models.Model):
    username = models.CharField(max_length=32, verbose_name="사용자명")
    password = models.CharField(max_length=64, verbose_name="비밀번호")
    useremail = models.EmailField(max_length=128, verbose_name="사용자메일")
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.username

    class Meta:
        db_table = "DJuser"
        verbose_name = "DJUSER"
        verbose_name_plural = "DJUSER"
