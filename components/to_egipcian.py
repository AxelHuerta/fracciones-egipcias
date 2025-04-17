import flet as ft
from fracciones import Fraccion, FraccionEgipcia


class To_Egipcian(ft.Column):
    def __init__(self, page=None):
        super().__init__()

        self.page = page

        # Inputs
        self.numerador = ft.TextField(
            label="Numerador",
            width=200,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE),
        )
        self.denominador = ft.TextField(
            label="Denominador",
            width=200,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE),
        )

        # Elementos para el resultado
        self.result_text = ft.Text(
            "Resultado: ", color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER
        )

        self.result_values = ft.Text("", color=ft.Colors.WHITE, size=30)
        self.result_btn = ft.ElevatedButton(
            "Convertir",
            bgcolor=ft.Colors.TEAL_ACCENT_400,
            color=ft.Colors.BLACK,
            width=680,
            on_click=lambda e: handle_inputs(e),
        )

        # Manejar los inputs
        def handle_inputs(e):
            if self.numerador.value == "" or self.denominador.value == "":
                self.result_text.value = "Debe llenar los campos"
                self.update()
                return

            self.result_text.value = "Resultado: "

            a = self.numerador.value
            b = self.denominador.value

            fraccion: Fraccion = Fraccion(int(a), int(b))
            result = FraccionEgipcia.convertir(fraccion)
            result_text = FraccionEgipcia.to_string(result)
            self.result_values.value = result_text
            self.update()

        self.controls = [
            ft.Row(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Fracción 1", color=ft.Colors.WHITE
                                                ),
                                                self.numerador,
                                                self.denominador,
                                            ],
                                        ),
                                    ],
                                    spacing=80,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    width=680,
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            self.result_btn,
                                        ],
                                    ),
                                    padding=ft.padding.only(top=40),
                                ),
                                ft.Row(
                                    [
                                        ft.Column(
                                            [
                                                ft.Row(
                                                    [
                                                        self.result_text,
                                                    ],
                                                    width=680,
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                                ft.Row(
                                                    [
                                                        self.result_values,
                                                    ],
                                                    width=680,
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                        ),
                                    ],
                                    spacing=80,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                            ],
                        ),
                        alignment=ft.alignment.center,
                        padding=40,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]
