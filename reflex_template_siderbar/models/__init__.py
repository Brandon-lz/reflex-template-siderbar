import reflex as rx
from .user import User


def init_db():
    try:
        with rx.session() as sess:
            user = sess.exec(User.select().where(User.name == "admin")).first()
            if user:
                pass
            else:
                sess.expire_on_commit = False  # Make sure the user object is accessible. https://sqlalche.me/e/14/bhk3
                user = User(name="admin", password="123456",worker_id="10000",class_group="0",is_superuser=True)
                sess.add(user)
                sess.commit()
    except:
        print("db not init, please run reflex db init first")