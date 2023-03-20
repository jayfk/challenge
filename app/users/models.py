from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Model representing a user on the platform."""

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    @property
    def initials(self):
        try:
            return "".join([c[0] for c in
                            self.get_full_name().split(
                                " ")]) if self.get_full_name() else ""
        except IndexError:
            return "  "
