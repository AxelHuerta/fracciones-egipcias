import flet as ft
from components.header import Header
from components.ops_section import Ops_Section
from components.to_egyptian import To_Egyptian


def main(page: ft.Page):
    page.title = "Calculadora de Fracciones"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#1c1c2b"
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.WHITE)

    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.WHITE,
            on_primary=ft.Colors.WHITE,
            secondary=ft.Colors.WHITE,
            on_secondary=ft.Colors.WHITE,
            surface=ft.Colors.WHITE,
        )
    )

    title = Header()
    ops_section = Ops_Section()
    to_egyptian = To_Egyptian()

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Calculadora",
                content=ops_section,
            ),
            ft.Tab(
                text="Fracción a Egipcia",
                content=to_egyptian,
            ),
        ],
        expand=1,
        padding=80,
        tab_alignment=ft.MainAxisAlignment.CENTER,
        unselected_label_color=ft.Colors.WHITE,
    )

    page.add(
        ft.Column(
            [
                ft.Row(
                    [title],
                    alignment=ft.MainAxisAlignment.CENTER,
                    width=page.window.width,
                ),
                tabs,
            ],
            expand=True,
            spacing=20,
        )
    )


ft.app(main)
