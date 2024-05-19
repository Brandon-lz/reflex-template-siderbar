import reflex as rx
from reflex_template_siderbar.models.user import User


class AppState(rx.State):
    user: User | None = None

    def logout(self):
        self.user = None
        return rx.redirect("/login")
