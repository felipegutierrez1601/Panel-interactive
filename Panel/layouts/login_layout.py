from dash import html, dcc

def create_login_layout(app):
    return html.Div(
        className="login-container",
        children=[
            html.Div(
                className="login-card",
                children=[
                    html.H2("Iniciar Sesión"),
                    html.Img(
                        src="https://arauco.com/chile/wp-content/uploads/sites/14/2019/04/logo-arauco.png",
                        alt="Logo",
                        className="logo"
                    ),
                    html.H3("Arauco"),
                    # Mostrar mensajes de error
                    html.Div(
                        id="error-messages",
                        style={"color": "red"}
                    ),
                    # Entrada de usuario y contraseña (sin html.Form)
                    html.Div(
                        className="input-group",
                        children=[
                            dcc.Input(
                                id="usuario",
                                type="text",
                                placeholder="Usuario",
                                required=True,
                                className="login-input"
                            )
                        ]
                    ),
                    html.Div(
                        className="input-group",
                        children=[
                            dcc.Input(
                                id="password",
                                type="password",
                                placeholder="Contraseña",
                                required=True,
                                className="login-input"
                            )
                        ]
                    ),
                    html.Button(
                        "Iniciar Sesión",
                        id="login-button",
                        className="boton_inicio"
                    ),
                    html.Div(
                        className="login-footer",
                        children=[
                            html.A("¿No tienes una cuenta?", href="#"),
                            html.A("Olvidaste los detalles", href="#")
                        ]
                    )
                ]
            )
        ]
    )
