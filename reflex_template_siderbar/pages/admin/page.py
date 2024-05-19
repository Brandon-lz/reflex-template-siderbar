import reflex as rx
from reflex_template_siderbar.models.user import User
import reflex as rx
from .state import AdminState
from .update_user import update_User
from .add_user import add_customer


def show_users(user: User):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(rx.avatar(fallback="DA")),
        rx.table.cell(user.name,),
        rx.table.cell(user.worker_id),
        rx.table.cell(user.class_group),
        rx.table.cell(
            update_User(user),
        ),
        rx.table.cell(
            rx.button(
                "Delete",
                on_click=lambda: AdminState.delete_User(user.worker_id),
                bg="red",
                color="white",
            ),
        ),
    )



# def navbar():
#     return rx.hstack(
#         rx.vstack(
#             rx.heading("拧紧机用户管理", size="7", font_family="Inter"),
#             on_mount=AdminState.on_load,
#         ),
#         rx.spacer(),
#         add_customer(),
#         rx.avatar(fallback="TG", size="4"),
#         rx.color_mode.button(rx.color_mode.icon(), size="3", float="right"),
#         position="fixed",
#         width="100%",
#         top="0px",
#         z_index="1000",
#         padding_x="4em",
#         padding_top="2em",
#         padding_bottom="1em",
#         backdrop_filter="blur(10px)",
#     )


def content():
    return rx.fragment(
        rx.vstack(
            # rx.divider(),
            rx.hstack(
                rx.heading(
                    f"总计: {AdminState.num_Users} 用户",
                    size="5",
                    font_family="Inter",
                    on_mount=AdminState.on_load,
                ),
                rx.spacer(),
                rx.select(
                    ["姓名", "工号", "班组"],
                    placeholder="排序: 姓名",
                    size="3",
                    on_change=lambda sort_value: AdminState.sort_values(sort_value),
                    font_family="Inter",
                ),
                width="100%",
                padding_x="2em",
                padding_top="2em",
                padding_bottom="1em",
            ),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("头像"),
                        rx.table.column_header_cell("姓名"),
                        rx.table.column_header_cell("工号"),
                        rx.table.column_header_cell("班组"),
                        rx.table.column_header_cell("编辑"),
                        rx.table.column_header_cell("删除"),
                    ),
                ),
                rx.table.body(rx.foreach(AdminState.users, show_users)),
                # variant="surface",
                size="3",
                width="100%",
            ),
        ),
    )


from reflex_template_siderbar.template import template
from reflex_template_siderbar.navigation import navbar
from .. import style


@template
def index() -> rx.Component:
    return rx.box(
        navbar("拧紧机用户管理"),
        rx.box(
            content(),
            # margin_top="calc(50px + 2em)",
            # padding="4em",
            margin_top=f"calc(50px + {style.Siderbar.margin_top})",
            padding="2em",
        ),
        font_family="Inter",
        padding_left="250px",        # siderbar的宽度
    )


# # Create app instance and add index page.
# app = rx.App(

#     stylesheets=["https://fonts.googleapis.com/css?family=Inter"],
# )
