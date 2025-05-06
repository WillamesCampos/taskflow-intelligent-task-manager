from core.dtos.audition_dto import AuditableDTO


class UserAccountDTO(AuditableDTO):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        is_active: bool,
        is_admin: bool,
    ) -> None:

        super().__init__()

        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active
        self.is_admin = is_admin
