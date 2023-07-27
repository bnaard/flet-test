import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(value="Hello, world!"))

ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8550)