class AuditableMixin:
    def __init__(
        self,
        created_by_id: int,
        updated_by_id: int
    ) -> None:

        self.created_by_id = created_by_id
        self.updated_by_id = updated_by_id
