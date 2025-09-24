import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Lista de Tareas")
        self.root.geometry("500x600")
        self.root.resizable(True, True)

        # Configurar estilo
        self.configure_styles()

        # Lista para almacenar las tareas
        self.tasks = []

        # Crear la interfaz
        self.create_interface()

        # Configurar eventos de teclado
        self.configure_events()

    def configure_styles(self):
        """Configurar los estilos de la aplicación"""
        style = ttk.Style()
        style.configure('Title.TLabel', font=('Arial', 14, 'bold'))
        style.configure('Completed.TLabel', foreground='gray', font=('Arial', 9, 'italic'))

    def create_interface(self):
        """Crear todos los componentes de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configurar expansión de la ventana
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(3, weight=1)

        # Título
        title_label = ttk.Label(main_frame, text="📝 Gestor de Tareas", style='Title.TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Frame para entrada de nueva tarea
        input_frame = ttk.Frame(main_frame)
        input_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        input_frame.columnconfigure(1, weight=1)

        # Campo de entrada para nueva tarea
        ttk.Label(input_frame, text="Nueva tarea:").grid(row=0, column=0, padx=(0, 5))
        self.task_entry = ttk.Entry(input_frame, font=('Arial', 10))
        self.task_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))

        # Botón añadir
        self.add_button = ttk.Button(input_frame, text="➕ Añadir", command=self.add_task)
        self.add_button.grid(row=0, column=2)

        # Frame para botones de acción
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=3, pady=(0, 10))

        # Botones de acción
        self.complete_button = ttk.Button(button_frame, text="✓ Completar",
                                          command=self.toggle_complete_task, state='disabled')
        self.complete_button.grid(row=0, column=0, padx=(0, 5))

        self.delete_button = ttk.Button(button_frame, text="🗑️ Eliminar",
                                        command=self.delete_task, state='disabled')
        self.delete_button.grid(row=0, column=1, padx=(0, 5))

        self.clear_completed_button = ttk.Button(button_frame, text="🧹 Limpiar Completadas",
                                                 command=self.clear_completed)
        self.clear_completed_button.grid(row=0, column=2)

        # Treeview para mostrar las tareas
        self.create_task_list(main_frame)

        # Label con estadísticas
        self.stats_label = ttk.Label(main_frame, text="Tareas: 0 | Completadas: 0 | Pendientes: 0")
        self.stats_label.grid(row=4, column=0, columnspan=3, pady=(10, 0))

        # Actualizar estadísticas iniciales
        self.update_stats()

    def create_task_list(self, parent):
        """Crear el componente de lista de tareas con Treeview"""
        # Frame para el Treeview y scrollbar
        list_frame = ttk.Frame(parent)
        list_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        # Crear Treeview
        columns = ('Estado', 'Tarea', 'Fecha')
        self.task_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)

        # Configurar columnas
        self.task_tree.heading('Estado', text='Estado')
        self.task_tree.heading('Tarea', text='Tarea')
        self.task_tree.heading('Fecha', text='Fecha de Creación')

        self.task_tree.column('Estado', width=80, anchor='center')
        self.task_tree.column('Tarea', width=250, anchor='w')
        self.task_tree.column('Fecha', width=120, anchor='center')

        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.task_tree.yview)
        self.task_tree.configure(yscroll=scrollbar.set)

        # Grid layout
        self.task_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

    def configure_events(self):
        """Configurar todos los eventos de la aplicación"""
        # Evento Enter en el campo de entrada
        self.task_entry.bind('<Return>', lambda e: self.add_task())

        # Eventos del Treeview
        self.task_tree.bind('<<TreeviewSelect>>', self.on_task_select)
        self.task_tree.bind('<Double-1>', lambda e: self.toggle_complete_task())

        # Eventos de teclado para toda la aplicación
        self.root.bind('<Delete>', lambda e: self.delete_task())
        self.root.bind('<F5>', lambda e: self.refresh_display())

        # Focus en el campo de entrada al iniciar
        self.task_entry.focus()

    def add_task(self):
        """Añadir una nueva tarea a la lista"""
        task_text = self.task_entry.get().strip()

        if not task_text:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")
            return

        if len(task_text) > 100:
            messagebox.showwarning("Advertencia", "La tarea es demasiado larga (máximo 100 caracteres).")
            return

        # Crear nueva tarea
        task = {
            'id': len(self.tasks),
            'text': task_text,
            'completed': False,
            'created_date': datetime.now().strftime("%d/%m/%Y"),
            'created_time': datetime.now().strftime("%H:%M")
        }

        self.tasks.append(task)
        self.refresh_display()
        self.task_entry.delete(0, tk.END)
        self.task_entry.focus()

        # Mostrar mensaje de confirmación
        self.show_status_message(f"✓ Tarea añadida: {task_text}")

    def toggle_complete_task(self):
        """Alternar el estado de completado de la tarea seleccionada"""
        selection = self.task_tree.selection()

        if not selection:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")
            return

        item = selection[0]
        # Obtener el índice de la tarea en la lista actual mostrada
        index = self.task_tree.index(item)
        display_tasks = self.get_display_tasks()

        if index < len(display_tasks):
            task_to_toggle = display_tasks[index]
            # Encontrar la tarea en la lista principal y alternar su estado
            for task in self.tasks:
                if task['id'] == task_to_toggle['id']:
                    task['completed'] = not task['completed']
                    status = "completada" if task['completed'] else "marcada como pendiente"
                    self.show_status_message(f"✓ Tarea {status}")
                    break

        self.refresh_display()

    def delete_task(self):
        """Eliminar la tarea seleccionada"""
        selection = self.task_tree.selection()

        if not selection:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar esta tarea?"):
            item = selection[0]
            # Obtener el índice de la tarea en la lista actual mostrada
            index = self.task_tree.index(item)

            # Obtener la tarea desde la lista filtrada actual
            if index < len(self.get_display_tasks()):
                task_to_remove = self.get_display_tasks()[index]
                self.tasks = [task for task in self.tasks if task['id'] != task_to_remove['id']]
                self.show_status_message("🗑️ Tarea eliminada")
                self.refresh_display()

    def clear_completed(self):
        """Eliminar todas las tareas completadas"""
        completed_tasks = [task for task in self.tasks if task['completed']]

        if not completed_tasks:
            messagebox.showinfo("Información", "No hay tareas completadas para eliminar.")
            return

        if messagebox.askyesno("Confirmar", f"¿Eliminar {len(completed_tasks)} tareas completadas?"):
            self.tasks = [task for task in self.tasks if not task['completed']]
            self.show_status_message(f"🧹 {len(completed_tasks)} tareas completadas eliminadas")
            self.refresh_display()

    def get_display_tasks(self):
        """Obtener las tareas ordenadas para mostrar (pendientes primero)"""
        return sorted(self.tasks, key=lambda x: (x['completed'], x['id']))

    def refresh_display(self):
        """Actualizar la visualización de las tareas"""
        # Limpiar el Treeview
        for item in self.task_tree.get_children():
            self.task_tree.delete(item)

        # Añadir tareas ordenadas
        for task in self.get_display_tasks():
            if task['completed']:
                status = "✅ Completada"
                task_text = f"~~{task['text']}~~"  # Simulamos tachado con tildes
            else:
                status = "⏳ Pendiente"
                task_text = task['text']

            # Insertar con tags para el estilo
            item = self.task_tree.insert('', 'end',
                                         values=(status, task_text, task['created_date']),
                                         tags=('completed' if task['completed'] else 'pending',))

        # Configurar tags para el estilo visual
        self.task_tree.tag_configure('completed', foreground='gray', background='#f0f0f0')
        self.task_tree.tag_configure('pending', foreground='black', background='white')

        self.update_stats()
        self.update_button_states()

    def on_task_select(self, event):
        """Manejar la selección de tareas"""
        self.update_button_states()

    def update_button_states(self):
        """Actualizar el estado de los botones según la selección"""
        selection = self.task_tree.selection()

        if selection:
            self.complete_button['state'] = 'normal'
            self.delete_button['state'] = 'normal'
        else:
            self.complete_button['state'] = 'disabled'
            self.delete_button['state'] = 'disabled'

    def update_stats(self):
        """Actualizar las estadísticas de tareas"""
        total = len(self.tasks)
        completed = len([task for task in self.tasks if task['completed']])
        pending = total - completed

        self.stats_label.config(text=f"Tareas: {total} | Completadas: {completed} | Pendientes: {pending}")

    def show_status_message(self, message):
        """Mostrar un mensaje de estado temporal"""
        original_text = self.stats_label.cget('text')
        self.stats_label.config(text=message, foreground='green')
        self.root.after(2000, lambda: self.stats_label.config(text=original_text, foreground='black'))


def main():
    """Función principal para ejecutar la aplicación"""
    root = tk.Tk()
    app = TodoApp(root)

    # Configurar el comportamiento al cerrar
    def on_closing():
        if messagebox.askokcancel("Salir", "¿Quieres salir de la aplicación?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Centrar la ventana en la pantalla
    root.update_idletasks()
    x = (root.winfo_screenwidth() - root.winfo_width()) // 2
    y = (root.winfo_screenheight() - root.winfo_height()) // 2
    root.geometry(f"+{x}+{y}")

    # Mostrar mensaje de bienvenida
    root.after(500, lambda: messagebox.showinfo("Bienvenido",
                                                "¡Bienvenido al Gestor de Tareas!\n\n"
                                                "💡 Consejos:\n"
                                                "• Presiona Enter para añadir tareas rápidamente\n"
                                                "• Doble clic en una tarea para marcarla como completada\n"
                                                "• Usa la tecla Suprimir para eliminar tareas\n"
                                                "• Presiona F5 para refrescar la vista"))

    root.mainloop()


if __name__ == "__main__":
    main()