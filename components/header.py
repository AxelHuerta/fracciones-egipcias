import flet as ft


class Header(ft.Column):
    def __init__(self):
        super().__init__()
        self.controls = [
            ft.Text(
                "Calculadora de Fracciones",
                size=32,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            )
        ]
