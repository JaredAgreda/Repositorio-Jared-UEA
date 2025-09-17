import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import calendar


class DatePicker:
    """Selector de fechas personalizado"""

    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

    def show_calendar(self):
        """Muestra ventana de calendario"""
        self.cal_window = tk.Toplevel(self.parent)
        self.cal_window.title("Seleccionar Fecha")
        self.cal_window.geometry("250x200")
        self.cal_window.grab_set()

        today = datetime.now()
        self.current_month = today.month
        self.current_year = today.year

        # Navegación
        nav_frame = tk.Frame(self.cal_window)
        nav_frame.pack(pady=5)

        tk.Button(nav_frame, text="<", command=self.prev_month).pack(side=tk.LEFT, padx=5)
        self.month_label = tk.Label(nav_frame, font=('Arial', 10, 'bold'))
        self.month_label.pack(side=tk.LEFT, padx=10)
        tk.Button(nav_frame, text=">", command=self.next_month).pack(side=tk.LEFT, padx=5)

        self.cal_frame = tk.Frame(self.cal_window)
        self.cal_frame.pack(pady=5)
        self.update_calendar()

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.update_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.update_calendar()

    def update_calendar(self):
        for widget in self.cal_frame.winfo_children():
            widget.destroy()

        month_name = calendar.month_name[self.current_month]
        self.month_label.config(text=f"{month_name} {self.current_year}")

        days = ['L', 'M', 'X', 'J', 'V', 'S', 'D']
        for i, day in enumerate(days):
            tk.Label(self.cal_frame, text=day, font=('Arial', 9, 'bold')).grid(row=0, column=i, padx=1, pady=1)

        cal = calendar.monthcalendar(self.current_year, self.current_month)
        for week_num, week in enumerate(cal, 1):
            for day_num, day in enumerate(week):
                if day == 0:
                    tk.Label(self.cal_frame, text="", width=3).grid(row=week_num, column=day_num)
                else:
                    tk.Button(self.cal_frame, text=str(day), width=3,
                              command=lambda d=day: self.select_date(d)).grid(row=week_num, column=day_num)

    def select_date(self, day):
        selected_date = datetime(self.current_year, self.current_month, day)
        self.callback(selected_date.strftime("%d/%m/%Y"))
        self.cal_window.destroy()


class AgendaPersonal:
    """Aplicación de Agenda Personal"""

    def __init__(self, root):
        self.root = root
        self.eventos = []
        self.setup_window()
        self.create_widgets()

    def setup_window(self):
        """Configura ventana principal"""
        self.root.title("Agenda Personal")
        self.root.geometry("800x600")
        self.root.configure(bg='white')

    def create_widgets(self):
        """Crea widgets de la interfaz"""
        main_frame = tk.Frame(self.root, bg='white')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Título
        tk.Label(main_frame, text="Agenda Personal",
                 font=('Arial', 16, 'bold'), bg='white').pack(pady=(0, 20))

        # Frame de visualización
        view_frame = tk.LabelFrame(main_frame, text="Lista de Eventos",
                                   font=('Arial', 10, 'bold'), bg='white')
        view_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))

        # TreeView
        columns = ('Fecha', 'Hora', 'Descripción')
        self.tree = ttk.Treeview(view_frame, columns=columns, show='headings', height=10)

        self.tree.heading('Fecha', text='Fecha')
        self.tree.heading('Hora', text='Hora')
        self.tree.heading('Descripción', text='Descripción')

        self.tree.column('Fecha', width=100)
        self.tree.column('Hora', width=80)
        self.tree.column('Descripción', width=300)

        scrollbar = ttk.Scrollbar(view_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

        # Frame de entrada
        input_frame = tk.LabelFrame(main_frame, text="Nuevo Evento",
                                    font=('Arial', 10, 'bold'), bg='white')
        input_frame.pack(fill=tk.X, pady=(0, 20))

        # Campos de entrada
        fields_frame = tk.Frame(input_frame, bg='white')
        fields_frame.pack(fill=tk.X, padx=10, pady=10)

        # Fecha
        tk.Label(fields_frame, text="Fecha:", bg='white').grid(row=0, column=0, sticky='w', padx=(0, 5))
        fecha_frame = tk.Frame(fields_frame, bg='white')
        fecha_frame.grid(row=0, column=1, sticky='w', padx=(0, 20))

        self.fecha_entry = tk.Entry(fecha_frame, width=12)
        self.fecha_entry.pack(side=tk.LEFT, padx=(0, 5))

        self.date_picker = DatePicker(self.root, self.set_date)
        tk.Button(fecha_frame, text="...", width=3,
                  command=self.date_picker.show_calendar).pack(side=tk.LEFT)

        # Hora
        tk.Label(fields_frame, text="Hora:", bg='white').grid(row=0, column=2, sticky='w', padx=(0, 5))
        self.hora_entry = tk.Entry(fields_frame, width=10)
        self.hora_entry.grid(row=0, column=3, sticky='w', padx=(0, 20))
        self.hora_entry.insert(0, "09:00")

        # Descripción
        tk.Label(fields_frame, text="Descripción:", bg='white').grid(row=1, column=0, sticky='w', pady=(10, 0))
        self.descripcion_entry = tk.Entry(fields_frame, width=50)
        self.descripcion_entry.grid(row=1, column=1, columnspan=3, sticky='ew', pady=(10, 0), padx=(0, 5))

        # Frame de botones
        button_frame = tk.Frame(main_frame, bg='white')
        button_frame.pack(fill=tk.X)

        tk.Button(button_frame, text="Agregar Evento",
                  command=self.agregar_evento, bg='#4CAF50', fg='white',
                  font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=(0, 10))

        tk.Button(button_frame, text="Eliminar Seleccionado",
                  command=self.eliminar_evento, bg='#f44336', fg='white',
                  font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=(0, 10))

        tk.Button(button_frame, text="Limpiar",
                  command=self.limpiar_campos, bg='#ff9800', fg='white',
                  font=('Arial', 10, 'bold')).pack(side=tk.LEFT, padx=(0, 10))

        tk.Button(button_frame, text="Salir",
                  command=self.root.quit, bg='#9E9E9E', fg='white',
                  font=('Arial', 10, 'bold')).pack(side=tk.RIGHT)

    def set_date(self, date_str):
        """Establece fecha seleccionada"""
        self.fecha_entry.delete(0, tk.END)
        self.fecha_entry.insert(0, date_str)

    def agregar_evento(self):
        """Agrega nuevo evento"""
        fecha = self.fecha_entry.get().strip()
        hora = self.hora_entry.get().strip()
        descripcion = self.descripcion_entry.get().strip()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
            return

        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Error", "Formato incorrecto. Fecha: DD/MM/AAAA, Hora: HH:MM")
            return

        evento = {
            'fecha': fecha,
            'hora': hora,
            'descripcion': descripcion,
            'datetime': datetime.strptime(f"{fecha} {hora}", "%d/%m/%Y %H:%M")
        }

        self.eventos.append(evento)
        self.eventos.sort(key=lambda x: x['datetime'])
        self.actualizar_vista()
        self.limpiar_campos()
        messagebox.showinfo("Éxito", "Evento agregado correctamente")

    def actualizar_vista(self):
        """Actualiza TreeView"""
        for item in self.tree.get_children():
            self.tree.delete(item)

        for evento in self.eventos:
            self.tree.insert('', 'end', values=(evento['fecha'], evento['hora'], evento['descripcion']))

    def eliminar_evento(self):
        """Elimina evento seleccionado"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar el evento seleccionado?"):
            index = self.tree.index(selected[0])
            del self.eventos[index]
            self.actualizar_vista()
            messagebox.showinfo("Éxito", "Evento eliminado")

    def limpiar_campos(self):
        """Limpia campos de entrada"""
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.hora_entry.insert(0, "09:00")
        self.descripcion_entry.delete(0, tk.END)


def main():
    """Función principal"""
    root = tk.Tk()
    app = AgendaPersonal(root)
    root.mainloop()


if __name__ == "__main__":
    main()