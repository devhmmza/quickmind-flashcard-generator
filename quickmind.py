import tkinter as tk
from tkinter import messagebox, scrolledtext
from flashcard_generator import generate_flashcards

class QuickMindApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QuickMind - AI Flashcard Generator")
        self.flashcards = []
        self.current = 0

        self.text_input = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD)
        self.text_input.pack(pady=10)

        self.generate_btn = tk.Button(root, text="Generate Flashcards", command=self.generate)
        self.generate_btn.pack()

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), wraplength=400)
        self.question_label.pack(pady=10)

        self.answer_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue", wraplength=400)
        self.answer_label.pack(pady=5)

        self.show_answer_btn = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.show_answer_btn.pack()

        self.next_btn = tk.Button(root, text="Next", command=self.next_flashcard)
        self.next_btn.pack()

    def generate(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Needed", "Please enter a topic or text.")
            return

        self.flashcards = generate_flashcards(text)
        self.current = 0

        if self.flashcards:
            self.display_flashcard()
        else:
            self.question_label.config(text="No flashcards generated.")
            self.answer_label.config(text="")

    def display_flashcard(self):
        q, _ = self.flashcards[self.current]
        self.question_label.config(text=q)
        self.answer_label.config(text="")

    def show_answer(self):
        _, a = self.flashcards[self.current]
        self.answer_label.config(text=a)

    def next_flashcard(self):
        if self.flashcards:
            self.current = (self.current + 1) % len(self.flashcards)
            self.display_flashcard()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuickMindApp(root)
    root.mainloop()
