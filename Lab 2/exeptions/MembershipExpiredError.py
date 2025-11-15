class MembershipExpiredError(MuseumException):
    """Исключение когда членство истекло."""
    
    def __init__(self, message="Членство истекло"):
        super().__init__(message)
        self.expiry_date = None
