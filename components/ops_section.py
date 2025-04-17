import flet as ft
from fracciones import Fraccion


class Ops_Section(ft.Column):
    def __init__(self, page=None):
        super().__init__()

        self.page = page

        self.numerador1 = ft.TextField(
            label="Numerador",
            width=200,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE),
        )
        self.denominador1 = ft.TextField(
            label="Denominador",
            width=200,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE),
        )

        self.numerador2 = ft.TextField(
            label="Numerador",
            width=200,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE),
        )
        self.denominador2 = ft.TextField(
            label="Denominador",
            width=200,
            color=ft.Colors.WHITE,
            label_style=ft.TextStyle(color=ft.Colors.WHITE),
        )

        self.active_operation = None

        self.result_text = ft.Text(
            "Resultado: ", color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER
        )
        self.result_numerador = ft.Text("", color=ft.Colors.WHITE, size=30)
        self.result_denominador = ft.Text("", color=ft.Colors.WHITE, size=30)

        def handle_op_button(e, operation):
            # Resetear los botones
            for btn in [self.suma_btn, self.resta_btn, self.mult_btn, self.div_btn]:
                btn.bgcolor = ft.Colors.WHITE
                btn.color = ft.Colors.BLACK

            # Activar el boton seleccionado
            e.control.bgcolor = ft.Colors.TEAL_ACCENT_700
            e.control.color = ft.Colors.WHITE
            self.active_operation = operation
            self.update()

        def handle_inputs(e):
            # Comprobar los campos
            if (
                self.numerador1.value == ""
                or self.denominador1.value == ""
                or self.numerador2.value == ""
                or self.denominador2.value == ""
                or self.active_operation == None
            ):
                self.result_text.value = (
                    "Debe llenar los campos y seleccionar una operación"
                )
                self.update()
                return

            # Comprobar la operacion
            if self.active_operation == "+":
                a = Fraccion(int(self.numerador1.value), int(self.denominador1.value))
                b = Fraccion(int(self.numerador2.value), int(self.denominador2.value))
                result: Fraccion = a + b
                self.result_numerador.value = str(result.numerador)
                self.result_denominador.value = str(result.denominador)
                self.update()

            if self.active_operation == "-":
                a = Fraccion(int(self.numerador1.value), int(self.denominador1.value))
                b = Fraccion(int(self.numerador2.value), int(self.denominador2.value))
                result: Fraccion = a - b
                self.result_numerador.value = str(result.numerador)
                self.result_denominador.value = str(result.denominador)
                self.update()

            if self.active_operation == "*":
                a = Fraccion(int(self.numerador1.value), int(self.denominador1.value))
                b = Fraccion(int(self.numerador2.value), int(self.denominador2.value))
                result: Fraccion = a * b
                self.result_numerador.value = str(result.numerador)
                self.result_denominador.value = str(result.denominador)
                self.update()

            if self.active_operation == "/":
                a = Fraccion(int(self.numerador1.value), int(self.denominador1.value))
                b = Fraccion(int(self.numerador2.value), int(self.denominador2.value))
                result: Fraccion = a / b
                self.result_numerador.value = str(result.numerador)
                self.result_denominador.value = str(result.denominador)
                self.update()

        # Botones
        self.suma_btn = ft.ElevatedButton(
            "+",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            on_click=lambda e: handle_op_button(e, "+"),
        )

        self.resta_btn = ft.ElevatedButton(
            "-",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            on_click=lambda e: handle_op_button(e, "-"),
        )

        self.mult_btn = ft.ElevatedButton(
            "×",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            on_click=lambda e: handle_op_button(e, "*"),
        )

        self.div_btn = ft.ElevatedButton(
            "÷",
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            on_click=lambda e: handle_op_button(e, "/"),
        )

        self.result_btn = ft.ElevatedButton(
            "Resultado",
            bgcolor=ft.Colors.TEAL_ACCENT_400,
            color=ft.Colors.BLACK,
            width=680,
            on_click=lambda e: handle_inputs(e),
        )

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
                                                self.numerador1,
                                                self.denominador1,
                                            ]
                                        ),
                                        ft.Column(
                                            [
                                                ft.Row(
                                                    [
                                                        self.suma_btn,
                                                        self.resta_btn,
                                                    ]
                                                ),
                                                ft.Row(
                                                    [
                                                        self.mult_btn,
                                                        self.div_btn,
                                                    ]
                                                ),
                                            ]
                                        ),
                                        ft.Column(
                                            [
                                                ft.Text(
                                                    "Fracción 2", color=ft.Colors.WHITE
                                                ),
                                                self.numerador2,
                                                self.denominador2,
                                            ]
                                        ),
                                    ],
                                    spacing=80,
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
                                                    [self.result_numerador],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    width=680,
                                                ),
                                                ft.Row(
                                                    [
                                                        ft.Container(
                                                            bgcolor=ft.Colors.WHITE,
                                                            width=100,
                                                            height=2,
                                                            border_radius=5,
                                                        )
                                                    ],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    width=680,
                                                ),
                                                ft.Row(
                                                    [self.result_denominador],
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    width=680,
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
