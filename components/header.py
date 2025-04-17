import flet as ft


class Header(ft.Text):
    def __init__(self):
        super().__init__(
            "Calculadora de Fracciones",
            size=32,
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
            color=ft.Colors.WHITE,
        )
