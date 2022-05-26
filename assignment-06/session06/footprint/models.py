from django.db import models


class Footprint(models.Model):
    footprint_id = models.AutoField(primary_key=True)
    receiver = models.TextField(null=False)
    # 문자열(TextField), 받는 사람 이름이 꼭 있어야 된다는 뜻! (null=False-> 정보가 빈칸이면 안된다는 뜻)
    message = models.TextField(null=False)
    sent_at = models.DateTimeField(auto_now_add=True, blank=False)
    # 날짜기 때문에 DateTimeField. 너가 알아서 시간 넣어줘~, blank=False->비어 있을 수 없어!