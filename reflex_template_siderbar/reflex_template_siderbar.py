"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from reflex_template_siderbar.pages import (
    index,
    login,
    register,
    admin,
    control,
    test,
    test_sidebar,
    custom_sidebar,
)

from reflex_template_siderbar.components import dashboard


from reflex_template_siderbar.models import init_db

init_db()


app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="grass"
    ),
    stylesheets=[
    "custom_button2_fast.css",
    "custom_button2_low.css",
    "custom_jog_forward_button.css",
    "custom_jog_backward_button.css",
    "custom_button2_stop.css",
    "googlefont.css",
])


# app.add_page(index)
app.add_page(index.index)
app.add_page(login.index,route="/login")
app.add_page(register.index,route="/register")
app.add_page(admin.index,route="/admin")
app.add_page(control.index,route="/control")
app.add_page(dashboard.index,route="/dashboard")
app.add_page(test.index,route="/test")
app.add_page(test_sidebar.index,route="/siderbar")
app.add_page(custom_sidebar.index,route="/custom_siderbar")
