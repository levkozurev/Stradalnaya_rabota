import flet as ft

def main(page: ft.Page):
    page.title = "Заметки с счетчиком"

    notes = ft.Column()
    input_field = ft.TextField(label="Введите заметку")
    counter = ft.Text("Количество заметок: 0")  # Счетчик заметок

    def add_note(e):
        if input_field.value:
            notes.controls.append(ft.Text(input_field.value))
            input_field.value = ""
            # Обновляем счетчик
            counter.value = f"Количество заметок: {len(notes.controls)}"
            page.update()

    button = ft.ElevatedButton("Добавить заметку", on_click=add_note)

    page.add(input_field, button, counter, notes)  # Добавляем счетчик на страницу

ft.app(target=main)
