import tkinter as tk
from tkinter import Label, Entry, Button
from sequence_processor import SequenceProcessor


class SequencePatternSolver(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sequence pattern solver")
        self.geometry("600x400")

        # Initialiser la classe SequenceProcessor
        self.sequence_processor = SequenceProcessor()

        # Création de l'étiquette pour indiquer à l'utilisateur d'entrer la séquence
        self.label_sequence = Label(self, text="What sequence? (space separated):")
        self.label_sequence.pack()

        # Création de la zone de texte pour entrer la séquence
        self.sequence_entry = Entry(self)
        self.sequence_entry.pack(fill='both')

        # Création du bouton pour déclencher la résolution du motif de séquence
        self.button_solve = Button(self, text="Solve", command=self.solve_pattern)
        self.button_solve.pack()

        # Création de la grille pour afficher les paires titre/réponse
        self.result_grid = tk.Frame(self)
        self.result_grid.pack()

        self.data = [
            ("Arithmetic", '_'),
            ("Geometric", '_'),
            #("Square", '_'),
            #("Cube", '_'),
            ("Power", '_'),
            ("Prime", '_'),
            ("Symmetric", '_'),
            ("Repetitive", '_'),
        ]

        # Remplir la grille avec les paires titre/réponse
        self.fill_grid()

        # Lier l'événement 'KeyPress' de la touche 'Return' à la méthode solve_pattern
        self.sequence_entry.bind("<Return>", lambda event: self.solve_pattern())

        # Autofocus sur la zone de texte dès le lancement de la fenêtre
        self.sequence_entry.focus_set()

    def fill_grid(self):
        # Parcourir les données et les afficher dans la grille
        for i, (title, response) in enumerate(self.data):
            color = "red"
            disk_label = Label(self.result_grid, text="●", fg=color)
            disk_label.grid(row=i, column=0)

            # Créer une étiquette pour le titre
            title_label = Label(self.result_grid, text=title)
            title_label.grid(row=i, column=1)

            response_title = Label(self.result_grid, text="the next is: ")
            response_title.grid(row=i, column=2)

            # Créer une étiquette pour la réponse (avec un disque rouge ou vert)
            response_label = Label(self.result_grid, text=response)
            response_label.grid(row=i, column=3)

            formula_title = Label(self.result_grid, text="formula: ")
            formula_title.grid(row=i, column=4)

            formula_label = Label(self.result_grid, text=response)
            formula_label.grid(row=i, column=5)

    def solve_pattern(self):
        for i, (_, _) in enumerate(self.data):
            disk_label = self.result_grid.grid_slaves(row=i, column=0)[0]
            disk_label.config(fg="red")

            response_label = self.result_grid.grid_slaves(row=i, column=3)[0]
            response_label.config(text='_')

            formula_label = self.result_grid.grid_slaves(row=i, column=5)[0]
            formula_label.config(text='_')
        sequence = self.sequence_entry.get()
        numbers = [int(num) for num in sequence.split() if num.isdigit()]
        if len(numbers) > 2:
            self.update_grid(self.sequence_processor.process_sequence(numbers))

    def update_grid(self, responses):
        # Parcourir les paires titre/réponse
        for i, (title, answer) in enumerate(self.data):
            if responses[i][0] is not None and responses [i][0] is not None:
                disk_label = self.result_grid.grid_slaves(row=i, column=0)[0]
                disk_label.config(fg="green")

                response_label = self.result_grid.grid_slaves(row=i, column=3)[0]
                response_label.config(text=responses[i][1])

                formula_label = self.result_grid.grid_slaves(row=i, column=5)[0]
                formula_label.config(text=responses[i][0])
                break


if __name__ == "__main__":
    app = SequencePatternSolver()
    app.mainloop()
