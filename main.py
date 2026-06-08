import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from database import DatabaseManager

# Configure UI Aesthetics
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class FinPulseApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("FinPulse - Analytics Dashboard")
        self.geometry("900x550")
        
        # Initialize Database Manager
        self.db = DatabaseManager()
        
        self._build_layout()
        self.render_dashboard()

    def _build_layout(self):
        """Constructs the core grid layout and sidebar navigation."""
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar setup
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="FinPulse ⚡", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=30)

        # Main Content Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

    def render_dashboard(self):
        """Fetches data and draws the financial charts."""
        title = ctk.CTkLabel(self.main_frame, text="Expense Overview", font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(anchor="w", pady=(0, 15))

        # Fetch data securely (Assuming user_id = 1 for the showcase)
        categories, amounts = self.db.fetch_user_expenses(user_id=1)

        if not categories:
            ctk.CTkLabel(self.main_frame, text="No data available. Please add transactions.").pack()
            return

        # Generate Matplotlib Chart
        self._embed_chart(categories, amounts)

    def _embed_chart(self, categories: list, amounts: list):
        """Handles the logic of drawing and embedding the Matplotlib figure."""
        fig, ax = plt.subplots(figsize=(6, 4), facecolor='#2b2b2b')
        ax.set_facecolor('#2b2b2b')

        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        ax.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140, 
               colors=colors, textprops=dict(color="w"))
        
        ax.set_title("Spending Breakdown", color="w", fontsize=12, pad=10)

        canvas = FigureCanvasTkAgg(fig, master=self.main_frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        canvas.draw()

if __name__ == "__main__":
    app = FinPulseApp()
    app.mainloop()
