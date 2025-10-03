import tkinter as tk
from tkinter import ttk, messagebox


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Mi Gestor de Tareas")
        self.root.geometry("500x600")
        self.root.configure(bg="#2d3748")

        # Lista para almacenar tareas: [texto, completada]
        self.tasks = []

        self.setup_ui()
        self.bind_shortcuts()

    def setup_ui(self):
        # Frame principal con degradado simulado
        main_frame = tk.Frame(self.root, bg="#2d3748")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Título
        title = tk.Label(main_frame, text="📝 MIS TAREAS",
                         font=("Arial", 24, "bold"),
                         bg="#2d3748", fg="#63b3ed")
        title.pack(pady=(0, 20))

        # Frame para entrada y botón añadir
        input_frame = tk.Frame(main_frame, bg="#2d3748")
        input_frame.pack(fill=tk.X, pady=(0, 15))

        # Campo de entrada con estilo
        self.entry = tk.Entry(input_frame, font=("Arial", 12),
                              bg="#4a5568", fg="white",
                              insertbackground="white", relief=tk.FLAT,
                              highlightthickness=2, highlightbackground="#63b3ed")
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 10))
        self.entry.focus()

        # Botón añadir
        add_btn = tk.Button(input_frame, text="➕ Añadir",
                            command=self.add_task,
                            bg="#48bb78", fg="white",
                            font=("Arial", 11, "bold"),
                            relief=tk.FLAT, cursor="hand2",
                            activebackground="#38a169")
        add_btn.pack(side=tk.LEFT, ipady=6, ipadx=15)

        # Frame para lista de tareas
        list_frame = tk.Frame(main_frame, bg="#1a202c", relief=tk.FLAT)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))

        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox con estilo
        self.listbox = tk.Listbox(list_frame, font=("Arial", 11),
                                  bg="#1a202c", fg="white",
                                  selectbackground="#4299e1",
                                  selectforeground="white",
                                  relief=tk.FLAT,
                                  yscrollcommand=scrollbar.set,
                                  activestyle="none")
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.config(command=self.listbox.yview)

        # Frame de botones de acción
        btn_frame = tk.Frame(main_frame, bg="#2d3748")
        btn_frame.pack(fill=tk.X, pady=(0, 15))

        # Botón completar
        complete_btn = tk.Button(btn_frame, text="✓ Completar (C)",
                                 command=self.complete_task,
                                 bg="#4299e1", fg="white",
                                 font=("Arial", 10, "bold"),
                                 relief=tk.FLAT, cursor="hand2",
                                 activebackground="#3182ce")
        complete_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, ipady=8, padx=(0, 5))

        # Botón eliminar
        delete_btn = tk.Button(btn_frame, text="✗ Eliminar (D)",
                               command=self.delete_task,
                               bg="#f56565", fg="white",
                               font=("Arial", 10, "bold"),
                               relief=tk.FLAT, cursor="hand2",
                               activebackground="#e53e3e")
        delete_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, ipady=8, padx=(5, 0))

        # Contador de tareas
        self.counter_label = tk.Label(main_frame, text="Pendientes: 0 | Completadas: 0",
                                      font=("Arial", 10), bg="#2d3748",
                                      fg="#a0aec0")
        self.counter_label.pack()

        # Leyenda de atajos
        help_text = "💡 Enter: Añadir | C: Completar | D/Del: Eliminar | Esc: Salir"
        help_label = tk.Label(main_frame, text=help_text,
                              font=("Arial", 9), bg="#2d3748", fg="#718096")
        help_label.pack(pady=(10, 0))

    def bind_shortcuts(self):
        # Atajos de teclado
        self.root.bind('<Return>', lambda e: self.add_task())
        self.root.bind('<c>', lambda e: self.complete_task())
        self.root.bind('<C>', lambda e: self.complete_task())
        self.root.bind('<d>', lambda e: self.delete_task())
        self.root.bind('<D>', lambda e: self.delete_task())
        self.root.bind('<Delete>', lambda e: self.delete_task())
        self.root.bind('<Escape>', lambda e: self.root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            # Añadir tarea como [texto, False] (no completada)
            self.tasks.append([task, False])
            self.update_listbox()
            self.entry.delete(0, tk.END)
            self.entry.focus()
        else:
            messagebox.showwarning("Advertencia", "¡Escribe una tarea!")

    def complete_task(self):
        try:
            idx = self.listbox.curselection()[0]
            # Alternar estado completado
            self.tasks[idx][1] = not self.tasks[idx][1]
            self.update_listbox()
            # Mantener selección
            self.listbox.selection_set(idx)
        except IndexError:
            messagebox.showinfo("Info", "Selecciona una tarea primero")

    def delete_task(self):
        try:
            idx = self.listbox.curselection()[0]
            del self.tasks[idx]
            self.update_listbox()
        except IndexError:
            messagebox.showinfo("Info", "Selecciona una tarea para eliminar")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        pending = 0
        completed = 0

        # Mostrar tareas con formato especial
        for task, is_completed in self.tasks:
            if is_completed:
                # Tarea completada: texto tachado con emoji
                display = f"✓ {task}"
                self.listbox.insert(tk.END, display)
                # Cambiar color (simulado con texto)
                idx = self.listbox.size() - 1
                self.listbox.itemconfig(idx, fg="#68d391")
                completed += 1
            else:
                # Tarea pendiente
                display = f"○ {task}"
                self.listbox.insert(tk.END, display)
                pending += 1

        # Actualizar contador
        self.counter_label.config(text=f"Pendientes: {pending} | Completadas: {completed}")


# Crear y ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()