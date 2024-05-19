import reflex as rx
from reflex.components import lucide
from .state import AppState

FONT_FAMILY = "Share Tech Mono"

def sidebar_link(text: str, href: str, icon: str):
    return rx.link(
        rx.flex(
            rx.icon_button(
                rx.icon(tag=icon, weight=16, height=16),
                variant="soft",
            ),
            text,
            py="2",
            px="4",
            spacing="3",
            align="baseline",
            direction="row",
            font_family="Share Tech Mono",
        ),
        href=href,
        width="100%",
        border_radius="8px",
        _hover={
            "background": "rgba(255, 255, 255, 0.1)",
            "backdrop_filter": "blur(10px)",
        },
    )

from reflex_template_siderbar.pages import style

def sidebar(
    *sidebar_links,
    **props,
) -> rx.Component:
    logo_src = props.get("logo_src", "/logo.jpg")
    heading = props.get("heading", "NOT SET")
    return rx.vstack(
        rx.hstack(
            rx.image(src=logo_src, height="28px", border_radius="8px"),
            rx.heading(
                heading,
                font_family=FONT_FAMILY,
                size="7",
            ),
            width="100%",
            spacing="7",
        ),
        rx.divider(margin_y="3"),
        rx.vstack(
            *sidebar_links,
            padding_y="1em",
        ),
        width="250px",
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        align_items="left",
        z_index="10",
        backdrop_filter="blur(10px)",
        padding=style.Siderbar.margin_top,
    )


dashboard_sidebar = sidebar(
    sidebar_link(text="数据看板", href="/dashboard", icon="bar_chart_3"),
    sidebar_link(text="用户管理", href="/admin", icon="users"),
    sidebar_link(text="侧边栏模板页", href="/siderbar", icon="settings"),
    logo_src="/logo.jpg",
    heading="REFLEX",
)

from reflex_template_siderbar.pages import style


def navbar(heading: str) -> rx.Component:
    return rx.hstack(
        # rx.spacer(max_width="2em"),
        rx.heading(heading, font_family=FONT_FAMILY, size="7"),
        rx.spacer(),
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    "设置",
                    lucide.icon(tag="chevron_down", weight=16, height=16),
                    font_family=FONT_FAMILY,
                    variant="soft",
                ),
            ),
            rx.menu.content(
                rx.menu.item("用户管理",on_click=lambda:rx.redirect("/admin")),
                rx.menu.item("Profile"),
                rx.menu.item("Logout",on_click=AppState.logout),
                font_family=FONT_FAMILY,
                variant="soft",
            ),
            variant="soft",
            font_family=FONT_FAMILY,
        ),
        position="fixed",
        width="calc(100% - 250px)",
        top="0px",
        z_index="1000",
        padding_x="2em",
        padding_top=style.Siderbar.margin_top,
        padding_bottom="1em",
        backdrop_filter="blur(10px)",       # 毛玻璃效果
    )
