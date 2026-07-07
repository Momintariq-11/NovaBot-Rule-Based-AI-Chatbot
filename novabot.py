import tkinter as tk

class NovaBot:
    def __init__(self, root):
        self.root = root
        self.root.title("NovaBot")
        self.root.geometry("500x650")
        self.root.configure(bg="black")

        self.waiting = False

        tk.Label(root, text="NOVA", bg="black", fg="red",
                 font=("Arial", 20, "bold")).pack(pady=10)

        self.chatBox = tk.Text(root, bg="#1f1f1f", fg="white",
                               font=("Arial", 11), wrap="word",
                               state="disabled")
        self.chatBox.pack(fill="both", expand=True, padx=10)

        bottom = tk.Frame(root, bg="black")
        bottom.pack(fill="x", padx=10, pady=10)

        self.message = tk.Entry(bottom, font=("Arial", 11),
                                bg="silver", fg="black")
        self.message.pack(side="left", fill="x", expand=True)
        self.message.bind("<Return>", lambda e: self.send())

        tk.Button(bottom, text="Send", bg="red", fg="white",
                  command=self.send).pack(side="left", padx=5)

        self.show("Nova", "Hi! I'm Nova.\nType 'help' to see what I can do.")

    def show(self, who, text):
        self.chatBox.config(state="normal")
        self.chatBox.insert("end", f"\n{who}: {text}\n")
        self.chatBox.see("end")
        self.chatBox.config(state="disabled")

    def send(self):
        text = self.message.get().strip()
        if not text:
            return
        self.show("You", text)
        self.message.delete(0, "end")
        t = text.lower()

        if t in ["exit","quit","bye","1"]:
            reply="Goodbye! Thanks for chatting."
            self.show("Nova", reply)
            self.root.after(1200,self.root.destroy)
            return
        elif t in ["hi","hello","hey"]:
            self.waiting=True
            reply="Hello! How are you?"
        elif self.waiting and t in ["fine","good","great","i am fine","i'm fine","im fine"]:
            self.waiting=False
            reply="Glad to hear that! How can I help?"
        elif "how are you" in t:
            reply="I'm doing well. Thanks for asking!"
        elif "name"==t or "what is your name" in t:
            reply="I'm Nova."
        elif "who are you" in t:
            reply="I'm a simple Python chatbot."
        elif "who made you" in t or "creator" in t:
            reply="I was created by Momin Tariq as a Python project."
        elif "python" in t:
            reply="I was built using Python."
        elif "tkinter" in t or "gui" in t:
            reply="My interface is made with Tkinter."
        elif "joke" in t:
            reply="Why do programmers prefer dark mode? Because light attracts bugs!"
        elif "fact" in t:
            reply="Python is one of the most popular programming languages."
        elif "quote" in t:
            reply="Success comes from consistent effort."
        elif "motivate" in t:
            reply="Keep learning. Small progress every day leads to big results."
        elif "study" in t:
            reply="Practice every day instead of studying everything at once."
        elif "skills" in t:
            reply="I can answer simple predefined questions and have basic conversations."
        elif "weather" in t:
            reply="I can't check live weather."
        elif "time" in t:
            reply="I can't access the current time."
        elif "date" in t:
            reply="I can't access today's date."
        elif "thanks" in t:
            reply="You're welcome!"
        elif t=="help":
            reply=("Commands:\nhi\nhello\nhow are you\nwhat is your name\n"
                   "who are you\nwho made you\npython\ngui\njoke\nfact\n"
                   "quote\nmotivate me\nstudy\nskills\nweather\ntime\n"
                   "date\nthanks\nexit")
        else:
            reply="Sorry, I don't know that command yet. Type 'help' to see the available commands."

        self.show("Nova", reply)

root = tk.Tk()
NovaBot(root)
root.mainloop()
