import flet as ft

def main(page: ft.Page):

    t = ft.Text(value="Xin chao", color="blue")
    page.add(t)
    
    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )
    #goi ham pick file
    def pick_files_result(e: ft.FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        selected_files.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
#goi ham page.overlay de hien thu khung chon file
    page.overlay.append(pick_files_dialog)
#page.add de them button
    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=True
                    ),#ham tao button voi cac chuc nang 
                ),
                selected_files,
            ]
        )
    )

ft.app(target=main)