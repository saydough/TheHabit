import flet as ft
from View.viewWindowLogin import *
from View.viewProperties import *
from View.viewWindowMain import *
def main(page: ft.Page):
<<<<<<< HEAD
    page.data = UserProperties()
    test = windowLogin(page)
    view = ft.View('login', controls=[test.stack], bgcolor='#FFe5e5e5')
    page.views.append(view)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main)