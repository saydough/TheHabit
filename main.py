import flet as ft
from backendController import Login

def main(page: ft.Page):
    page.title = "Login Example"


    
    def login_clicked(e):
        login_user = Login(username.value, password.value)
        if login_user.userVerification():
            dlg = ft.AlertDialog(
                title=ft.Text("Login Successful"),
                on_dismiss=lambda e: page.update(),
            )
        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Login Failed"),
                on_dismiss=lambda e: page.update(),
            )

        page.dialog = dlg
        dlg.open = True
        page.update()
    
    username = ft.TextField(label="Username")
    password = ft.TextField(label="Password", password=True)
    login_btn = ft.ElevatedButton("Login", on_click=login_clicked)
    
    page.add(
        ft.Column(
            [
                username,
                password,
                login_btn,
            ]
        )
    )

if __name__ == "__main__":
    ft.app(target=main)