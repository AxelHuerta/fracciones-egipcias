import flet as ft
from fracciones import Fraccion, Fracciones, FraccionEgipcia


class Ops_Section(ft.Column):
    def __init__(self):
        super().__init__()


        self.numerador1 = ft.TextField(label="Numerador", width=200)
        self.denominador1 = ft.TextField(label="Denominador", width=200)

        self.numerador2 = ft.TextField(label="Numerador", width=200)
        self.denominador2 = ft.TextField(label="Denominador", width=200)

        self.active_operation = None

        self.result_text = ft.Text("Resultado: ", text_align=ft.TextAlign.CENTER) 

        self.result_numerador = ft.Text("a")
        self.result_denominador = ft.Text("b")

        def handle_op_button(e, operation):
            # Resetear los botones
            for btn in [self.suma_btn, self.resta_btn, self.mult_btn, self.div_btn]:
                btn.bgcolor = ft.colors.SURFACE_VARIANT
                # btn.color = ft.colors.WHITE

            # Activar el boton seleccionado
            e.control.bgcolor = ft.colors.TEAL_ACCENT_700
            e.control.color = ft.colors.WHITE
            self.active_operation = operation
            self.update()
        
        def handle_inputs(e):
            if self.numerador1.value == "" or self.denominador1.value == "" or self.numerador2.value == "" or self.denominador2.value == "" or self.active_operation == None:
                print("No hay datos")
                self.result_text.value = "Debe llenar los campos y seleccionar una operación"
                self.update()
                return
            


               
        # Botones
        self.suma_btn = ft.ElevatedButton(
            "+",
            bgcolor=ft.colors.SURFACE_VARIANT,
            on_click=lambda e: handle_op_button(e, "suma"),
        )

        self.resta_btn = ft.ElevatedButton(
            "-",
            bgcolor=ft.colors.SURFACE_VARIANT,
            on_click=lambda e: handle_op_button(e, "resta"),
        )

        self.mult_btn = ft.ElevatedButton(
            "×",
            bgcolor=ft.colors.SURFACE_VARIANT,
            on_click=lambda e: handle_op_button(e, "multiplicacion"),
        )

        self.div_btn = ft.ElevatedButton(
            "÷",
            bgcolor=ft.colors.SURFACE_VARIANT,
            on_click=lambda e: handle_op_button(e, "division"),
        )

        self.result_btn = ft.ElevatedButton(
            "Resultado",
            bgcolor=ft.colors.TEAL_ACCENT_400,
            color=ft.colors.BLACK,
            width=680,
            on_click=lambda e: handle_inputs(e),
        )

        self.controls = [
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text("Fracción 1"),
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
                                    ft.Text("Fracción 2"),
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
                    ft.Row([
                        ft.Column(
                            [
                                ft.Row(
                                    [
                                        self.result_text,
                                    ]
                                ),
                                ft.Row([
                                    self.result_numerador,
                                ]),
                                ft.Row([
                                    ft.Text("---"),
                                ]),
                                ft.Row([
                                    self.result_denominador,
                                ]),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=80,
                    alignment=ft.MainAxisAlignment.CENTER,
                    expand=True),
                ],
            )
        ]
