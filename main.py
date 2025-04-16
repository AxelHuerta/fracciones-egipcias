import flet as ft
from components.header import Header
from components.ops_section import Ops_Section


def main(page: ft.Page):
    page.title = "Calculadora de fracciones"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    title = Header()

    ops_section = Ops_Section()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    page.add(
        ft.Column(
            [
                ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([ops_section], alignment=ft.MainAxisAlignment.CENTER),
            ],
            spacing=80,
        )
    )


ft.app(main)
