import reflex as rx
from .. import style

# from ninjinji.components import plotly_component
from reflex_template_siderbar.components import custom_button
from reflex_template_siderbar.components import dashboard


def index() -> rx.Component:
    return rx.vstack(
        # plotly_component.create(),
        # dashboard.create(
        #     pin_angle=dashboard.State.pin_angle_sytle,
        #     color=dashboard.State.color,
        #     # style=dict(position="absolute",bottom="20em")
        # ),
        rx.hstack(
            dashboard.create(
                radius=10,
                border_width=0.7,
                pin_lenth=6,
                pin_angle=dashboard.DashboardState.pin_angle_sytle,
                color=dashboard.DashboardState.color,
                board_num=dashboard.DashboardState.board_num,
            ),
            id="dashboard-id",
            min_height="50vh",
        ),
        # rx.box(height="5em"),
        rx.hstack(
            custom_button.create_start_button(),
            custom_button.create_stop_button(),
            custom_button.create_jog_forward_button(),
            custom_button.create_jog_backward_button(),
        ),
        
        # rx.box(height="5em"),
        # rx.box("hello", id="text1"),
        # rx.vstack(
        #     rx.script(
        #         """const handle_press = (arg) => {
        #     window.alert("You clicked at " + arg.clientX + ", " + arg.clientY);
        # }"""
        #     ),
        #     rx.button(
        #         "Where Did I Click?",
        #         on_click=rx.client_side("handle_press(args)"),
        #     ),
        # ),
        #         rx.vstack(
        #             rx.script(
        # """function displayResult() {
        #     document.getElementById("text1").innerHTML = "Have a nice day!";
        # }"""
        #             ),
        #             rx.button(
        #                 "Where Did I Click?",
        #                 on_click=rx.client_side("""document.getElementById("text1").innerHTML = "Have a nice day!";"""),
        #             ),
        #         ),
        style=style.page,
    )
