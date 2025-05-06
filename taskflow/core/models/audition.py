from django.db import models
import uuid


class AuditableModel(models.Model):
    uuid = models.UUIDField(
        editable=False,
        unique=True,
        default=uuid.uuid4
    )
    created_by_id = models.IntegerField(
        editable=False,
        null=True,
        blank=True
    )
    updated_by_id = models.IntegerField(
        editable=False,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True

    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True
