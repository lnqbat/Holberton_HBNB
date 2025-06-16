from app.models import BaseModel

class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        """
        Users class.
        """
        super().__init__()

        if not first_name or len(first_name) > 50:
            raise ValueError("Invalid first_name")
        if not last_name or len(last_name) > 50:
            raise ValueError("Invalid last_name")
        if not email or "@" not in email:
            raise ValueError("Invalid email")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.places = []
