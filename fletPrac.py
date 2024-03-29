import flet as ft

def main(page: ft.Page):
    
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
                    ),
                ),
                selected_files,
            ]
        ),
        ##dng bi doan nay chua biet xu ly
        ft.Row(
            [
                ft.ElevatedButton(
                    "Open File",
                    icon=ft.icons.OPEN_IN_FULL,
                )
        ]
        )
    )

ft.app(target=main)