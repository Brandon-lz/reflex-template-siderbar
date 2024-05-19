import reflex as rx
from sqlmodel import select
from reflex_template_siderbar.models.user import User
from reflex_template_siderbar.state import AppState

class AdminState(rx.State):
    """The app state."""

    id: int
    name: str = ""
    worker_id: str = ""
    class_group: str = ""
    password: str = ""
    users: list[User] = []
    sort_value: str = ""
    num_Users: int

    # @rx.var
    async def is_admin(self) -> bool:
        appstate :AppState = await self.get_state(AppState)
        if appstate:
            return appstate.user.is_superuser
        return False

    def load_entries(self):
        """Get all users from the database."""
        with rx.session() as session:
            self.users = session.exec(select(User)).all()
            self.num_Users = len(self.users)
            if self.sort_value:
                self.users = sorted(
                    self.users, key=lambda user: getattr(user, self.sort_value).lower()
                )

    def sort_values(self, sort_value: str):
        item_map = {
            "姓名": "name",
            "工号": "worker_id",
            "班组": "class_group",
        }
        self.sort_value = item_map[sort_value]
        self.load_entries()

    def set_user_vars(self, user: User):
        self.id = user["id"]
        self.name = user["name"]
        self.worker_id = user["worker_id"]

    def add_User(self):
        """Add a User to the database."""
        with rx.session() as session:
            if session.exec(
                select(User).where(User.worker_id == self.worker_id)
            ).first():
                return rx.window_alert("不可重复添加用户")
            session.add(
                User(
                    name=self.name,
                    password=self.password,
                    worker_id=self.worker_id,
                    class_group=self.class_group,
                )
            )
            session.commit()
        self.load_entries()
        return rx.window_alert(f"User {self.name}:{self.worker_id} has been added.")

    def update_User(self):
        """Update a User in the database."""
        with rx.session() as session:
            user = session.exec(select(User).where(User.id == self.id)).first()
            user.name = self.name
            user.worker_id = self.worker_id
            user.class_group = self.class_group
            session.add(user)
            session.commit()
        self.load_entries()

    def delete_User(self, worker_id: str):
        """Delete a User from the database."""
        with rx.session() as session:
            user = session.exec(select(User).where(User.worker_id == worker_id)).first()
            session.delete(user)
            session.commit()
        self.load_entries()

    def on_load(self):
        self.load_entries()
