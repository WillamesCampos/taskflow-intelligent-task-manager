from django.db import models
import uuid


class AuditableModel(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4()
    )
    created_by_id = models.IntegerField(
        editable=False
    )
    updated_by_id = models.IntegerField(
        editable=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True

    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True
