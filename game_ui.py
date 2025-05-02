import tkinter as tk
from tkinter import messagebox, PhotoImage
import os
import json
from quiz_manager import QuizManager
from score_manager import save_score
from difficulty import get_difficulty_settings

class QuizApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.geometry("800x600")
        self.window.configure(bg="SystemButtonFace")  

        self.canvas = tk.Canvas(self.window, height=600, width=800)
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_rectangle(0, 0, 800, 600, fill="skyblue", outline="")
        self.canvas.create_rectangle(0, 0, 800, 600, fill="lavender", stipple="gray50")

        self.player_name = ""
        self.level = ""
        self.category = ""
        self.quiz = None
        self.questions_saved = []
        self.current_question = None
        self.photo = None
        self.image_label = None

        self.bg_color = "#f0f4f8"  
        self.primary_color = "#4e73df"  
        self.secondary_color = "#1cc88a"  
        self.accent_color = "#e74a3b"  
        self.button_hover = "#2e59d9"  

    def run(self):
        self.show_name_entry()
        self.window.mainloop()

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def show_name_entry(self):
        self.clear_window()
        tk.Label(self.window, text="Entrez votre prénom :", font=("Arial", 20), bg=self.bg_color, fg=self.primary_color).pack(pady=30)
        self.name_entry = tk.Entry(self.window, font=("Arial", 16), bg="#ffffff", fg=self.primary_color)
        self.name_entry.pack(pady=10)
        tk.Button(self.window, text="Continuer", font=("Arial", 16), bg=self.secondary_color, fg="white", activebackground=self.button_hover, command=self.save_name).pack(pady=20)

    def save_name(self):
        name = self.name_entry.get().strip()
        if name == "":
            messagebox.showwarning("Attention", "Veuillez entrer un prénom.")
        else:
            self.player_name = name
            self.show_level_menu()

    def show_level_menu(self):
        self.clear_window()
        tk.Label(self.window, text=f"Bonjour {self.player_name}, choisis un niveau :", font=("Arial", 20), bg=self.bg_color, fg=self.primary_color).pack(pady=30)

        for lvl in ["easy", "medium", "hard"]:
            tk.Button(self.window, text=lvl.capitalize(), font=("Arial", 16), bg=self.primary_color, fg="white", activebackground=self.button_hover, command=lambda l=lvl: self.select_level(l)).pack(pady=10)

    def select_level(self, level):
        self.level = level
        self.show_category_menu()

    def show_category_menu(self):
        self.clear_window()
        try:
            with open(f"data/questions/{self.level}.json", "r") as f:
                all_questions = json.load(f)
        except FileNotFoundError:
            messagebox.showerror("Erreur", f"Fichier questions {self.level}.json introuvable.")
            return

        self.categories = list(all_questions.keys())
        self.all_questions = all_questions

        tk.Label(self.window, text=f"Niveau {self.level.capitalize()} - Choisis une catégorie :", font=("Arial", 20), bg=self.bg_color, fg=self.primary_color).pack(pady=30)

        for cat in self.categories:
            tk.Button(self.window, text=cat.capitalize(), font=("Arial", 16), bg=self.secondary_color, fg="white", activebackground=self.button_hover, command=lambda c=cat: self.start_quiz(c)).pack(pady=10)

    def start_quiz(self, category):
        self.category = category
        questions_list = self.all_questions[self.category]
        self.quiz = QuizManager(questions_list)
        self.questions_saved = questions_list
        self.show_next_question()

    def show_next_question(self):
        self.clear_window()
        question = self.quiz.get_question()

        if question is None:
            self.show_score()
            return

        self.current_question = question

        tk.Label(self.window, text=f"{self.player_name}, {question['question']}", font=("Arial", 18), bg=self.bg_color, fg=self.primary_color, wraplength=700).pack(pady=20)

        if question.get("type") == "image" and "image" in question:
            image_path = f"resources/images/{question['image']}"
            if os.path.exists(image_path):
                self.photo = PhotoImage(file=image_path)
                self.image_label = tk.Label(self.window, image=self.photo)
                self.image_label.pack(pady=10)
            else:
                tk.Label(self.window, text="(Image manquante)", font=("Arial", 12), bg=self.bg_color, fg=self.accent_color).pack(pady=5)

        for i, option in enumerate(question["options"]):
            tk.Button(self.window, text=option, font=("Arial", 16), bg=self.primary_color, fg="white", activebackground=self.button_hover, command=lambda idx=i: self.check_answer(idx)).pack(pady=5, ipadx=20, ipady=10)

    def check_answer(self, index):
        correct = self.quiz.check_answer(self.current_question, index)
        if correct:
            bonus = get_difficulty_settings(self.level)["score_bonus"]
            self.quiz.score += bonus
            messagebox.showinfo("Bonne réponse", "Bravo !")
        else:
            messagebox.showinfo("Mauvaise réponse", f"Faux.\n{self.current_question['explanation']}")
        self.show_next_question()

    def show_score(self):
        save_score(self.player_name, self.level, self.quiz.score)
        self.clear_window()

        tk.Label(self.window, text="🎯 Résultats 🎯", font=("Verdana", 26, "bold"), bg=self.bg_color, fg=self.primary_color).pack(pady=(40, 20))

        score_text = f"Bravo {self.player_name} !\n\nScore en {self.category.capitalize()} ({self.level.capitalize()}) :\n{self.quiz.score} / {len(self.questions_saved)} points"
        tk.Label(self.window, text=score_text, font=("Arial", 20), bg=self.bg_color, fg=self.primary_color, justify="center").pack(pady=(10, 40))

        replay_button = tk.Button(self.window, text="🔄 Rejouer", font=("Arial", 18), bg=self.secondary_color, fg="white", activebackground=self.button_hover, command=self.replay_game)
        replay_button.pack(pady=10, ipadx=30, ipady=10)

        quit_button = tk.Button(self.window, text="❌ Quitter", font=("Arial", 18), bg=self.accent_color, fg="white", activebackground=self.button_hover, command=self.quit_game)
        quit_button.pack(pady=10, ipadx=30, ipady=10)

    def replay_game(self):
        self.show_level_menu()

    def quit_game(self):
        self.window.destroy()
