import tkinter as tk
from tkinter import messagebox


class TemperatureConverter:
    def __init__(self, root):
        # Configurar ventana
        self.root = root
        self.root.title("🌡️ Conversor de Temperaturas")
        self.root.geometry("350x250")
        self.root.configure(bg="#f5f5f5")

        self.create_widgets()

    def create_widgets(self):
        # Título
        title = tk.Label(self.root, text="Conversor de Temperaturas",
                         font=("Arial", 14, "bold"), bg="#f5f5f5", fg="#333")
        title.pack(pady=15)

        # Campo de entrada
        tk.Label(self.root, text="Ingresa la temperatura:",
                 font=("Arial", 10), bg="#f5f5f5").pack(pady=5)

        self.temp_entry = tk.Entry(self.root, font=("Arial", 12), width=15, justify="center")
        self.temp_entry.pack(pady=5)

        # Botones de conversión
        button_frame = tk.Frame(self.root, bg="#f5f5f5")
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Celsius → Fahrenheit",
                  command=self.celsius_to_fahrenheit, bg="#3498db", fg="white",
                  font=("Arial", 10), padx=10).pack(side="left", padx=5)

        tk.Button(button_frame, text="Fahrenheit → Celsius",
                  command=self.fahrenheit_to_celsius, bg="#e74c3c", fg="white",
                  font=("Arial", 10), padx=10).pack(side="left", padx=5)

        # Resultado
        tk.Label(self.root, text="Resultado:",
                 font=("Arial", 10, "bold"), bg="#f5f5f5").pack(pady=(10, 5))

        self.result_label = tk.Label(self.root, text="---",
                                     font=("Arial", 14, "bold"), bg="#f5f5f5",
                                     fg="#2c3e50")
        self.result_label.pack(pady=5)

        # Botón limpiar
        tk.Button(self.root, text="🔄 Limpiar", command=self.clear_all,
                  bg="#95a5a6", fg="white", font=("Arial", 10),
                  padx=20).pack(pady=15)

    # MÉTODOS DE FUNCIONALIDAD

    def celsius_to_fahrenheit(self):
        """
        Convierte temperatura de Celsius a Fahrenheit
        Fórmula: F = (C × 9/5) + 32
        """
        try:
            # Obtener el valor del campo de entrada y convertirlo a número
            celsius = float(self.temp_entry.get())

            # Aplicar la fórmula de conversión
            fahrenheit = (celsius * 9 / 5) + 32

            # Mostrar el resultado en la etiqueta (con 1 decimal)
            self.result_label.config(text=f"{fahrenheit:.1f}°F")

        except ValueError:
            # Si el usuario no ingresó un número válido, mostrar error
            messagebox.showerror("Error", "Ingresa un número válido")

    def fahrenheit_to_celsius(self):
        """
        Convierte temperatura de Fahrenheit a Celsius
        Fórmula: C = (F - 32) × 5/9
        """
        try:
            # Obtener el valor del campo de entrada y convertirlo a número
            fahrenheit = float(self.temp_entry.get())

            # Aplicar la fórmula de conversión
            celsius = (fahrenheit - 32) * 5 / 9

            # Mostrar el resultado en la etiqueta (con 1 decimal)
            self.result_label.config(text=f"{celsius:.1f}°C")

        except ValueError:
            # Si el usuario no ingresó un número válido, mostrar error
            messagebox.showerror("Error", "Ingresa un número válido")

    def clear_all(self):
        """
        Limpia todos los campos y reinicia la aplicación
        """
        # Borrar todo el contenido del campo de entrada
        self.temp_entry.delete(0, tk.END)

        # Restaurar el texto del resultado al estado inicial
        self.result_label.config(text="---")

        # Enfocar el cursor en el campo de entrada para facilitar uso
        self.temp_entry.focus()


# ========== EJECUCIÓN PRINCIPAL ==========
# Este bloque solo se ejecuta si el archivo se ejecuta directamente
if __name__ == "__main__":
    # Crear la ventana principal de tkinter
    root = tk.Tk()

    # Crear una instancia de nuestra aplicación
    app = TemperatureConverter(root)

    # Iniciar el bucle principal de eventos (mantiene la ventana abierta)
    root.mainloop()