from View.viewProperties import *
from Controller.controllerWindowLoginEvents import *
def windowLogin(page: ft.Page):
    vars                    = UserProperties()
    colors                  = vars.colors

    page.title              = "the Habit: Login"
    page.window_width       = vars.scale(286)
    page.window_height      = vars.scale(330)
    page.bgcolor            = colors.background
    page.window_resizable   = False

    if page.platform is ft.PagePlatform.MACOS:
        page.window_title_bar_hidden = True

    svgLogo                 = ft.Image(
                                src     = os.path.join(os.getcwd(), "Assets", vars.logo_big_full),
                                fit     = ft.ImageFit.FILL,
                                width   = vars.scale(198),
                                height  = vars.scale(110),
                            )
    bgDots                  = ft.Image(
                                src     = os.path.join(os.getcwd(), "Assets", vars.dots_login),
                                fit     = ft.ImageFit.FILL,
                                width   = page.window_width,
                                height  = page.window_height,
                            )
    buttonLogin             = ft.Container(
                                content         = ft.Container(
                                                    ft.Text("Login", style=vars.default_text_style),
                                                    alignment=ft.alignment.center,
                                                    padding=8
                                                ),
                                width           = vars.scale(154),
                                height          = vars.scale(22),
                                bgcolor         = colors.accent,
                                border_radius   = vars.scale(4),
                                ink             = True,
                                data            = page,
                                on_click        = eventButtonLoginClick
                            )
    staticUsername          = ft.Text(
                                "Username",
                                style   = vars.default_text_style,
                                color   = colors.foreground,
                            )
    staticPassword          = ft.Text(
                                "Password",
                                style   = vars.default_text_style,
                                color   = colors.foreground,
                            )
    editUsername            = ft.TextField(
                                text_style      = vars.textfield_style,
                                border          = ft.InputBorder.NONE,
                                cursor_color    = vars.set_transparency(colors.accent, 0.5),
                                cursor_height   = vars.scale(19),
                                cursor_width    = 10,
                                dense           = True,
                                width           = vars.scale(242),
                                height          = vars.scale(22),
                                bgcolor         = vars.set_transparency(colors.foreground, 0.05),
    )
    editPassword            = ft.TextField(
                                password            = True,
                                can_reveal_password = True,
                                text_style          = vars.textfield_style,
                                border              = ft.InputBorder.NONE,
                                cursor_color        = vars.set_transparency(colors.accent, 0.5),
                                cursor_height       = vars.scale(19),
                                cursor_width        = 10,
                                dense               = True,
                                width               = vars.scale(242),
                                height              = vars.scale(22),
                                bgcolor             = vars.set_transparency(colors.foreground, 0.05),
    )
    
    staticUsername          = ft.Container(
                                staticUsername,
                                padding     = vars.default_top_left_padding,
                                width       = vars.scale(242),
                                height      = vars.scale(22),
                                left        = vars.scale(22),
                                top         = vars.scale(154),
                                alignment   = ft.alignment.center_left,
                            )
    staticPassword          = ft.Container(
                                staticPassword,
                                padding     = vars.default_top_left_padding,
                                width       = vars.scale(242),
                                height      = vars.scale(22),
                                left        = vars.scale(22),
                                top         = vars.scale(198),
                                alignment   = ft.alignment.center_left
                            )
    editUsername            = ft.Container(
                                editUsername,
                                left    = vars.scale(22),
                                top     = vars.scale(176)
                            )
    editPassword            = ft.Container(
                                editPassword,
                                left    = vars.scale(22),
                                top     = vars.scale(220)
                            )
    buttonLogin             = ft.Container(
                                buttonLogin,
                                left    = vars.scale(66),
                                top     = vars.scale(264)
                            )
    bgDots                  = ft.Container(
                                bgDots,
                                opacity = 0.2,
                                left    = 0,
                                top     = 0
                            )
    svgLogo                 = ft.Container(
                                svgLogo,
                                left    =vars.scale(44),
                                top     =vars.scale(44),
                            )
    stack                   = ft.Stack(
                                [
                                    bgDots,
                                    svgLogo,
                                    staticUsername,
                                    staticPassword,
                                    editUsername,
                                    editPassword,
                                    buttonLogin
                                ],
                            )
    page.add(stack)
