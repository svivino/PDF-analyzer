import PyPDF2
from textblob import TextBlob
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser  # To open website

# Extract text from the selected PDF
def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted_text = page.extract_text()
                if extracted_text:
                    text += extracted_text + "\n"
        return text
    except Exception as e:
        messagebox.showerror("Error", f"Error reading PDF: {e}")
    return text  # Return full text

# Analyze sentiment using TextBlob
def analyze_sentiment(text):
    """Analyze sentiment using TextBlob"""
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# GUI Function to upload file and show results
def upload_file():
    global extracted_text  # Store text globally for saving
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not file_path:
        return

    extracted_text = extract_text_from_pdf(file_path)

    if extracted_text.strip():  
        polarity, subjectivity = analyze_sentiment(extracted_text)
        
        # Display sentiment analysis results in the GUI
        result_text.set(f"Sentiment Polarity: {polarity} (range: -1 to 1)\n"
                        f"Subjectivity: {subjectivity} (range: 0 to 1, higher means more opinionated)")
    else:
        messagebox.showerror("Error", "No text extracted from PDF. Check if the file contains selectable text.")

# Function to save extracted text to a .txt file
def save_text():
    if not extracted_text.strip():
        messagebox.showerror("Error", "No text extracted to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not file_path:
        return

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(extracted_text)
    messagebox.showinfo("Success", "Text saved successfully.")

# Open website function
def open_website():
    webbrowser.open("https://github.com/svivino")

# GUI Setup
root = tk.Tk()
root.title("PDF Sentiment Analyzer")
root.geometry("500x125")

# Credit Label (Aligned left)
tk.Label(root, text="Developed by Luc_Vivino", font=("Arial", 12, "italic")).pack(side="top", anchor="nw", padx=10)

# Frame to hold buttons in a row
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Upload PDF Button (Left)
tk.Button(button_frame, text="Upload PDF", command=upload_file, font=("Arial", 12)).pack(side="left", padx=10)

# Save as .txt Button (Middle)
tk.Button(button_frame, text="Save as .txt", command=save_text, font=("Arial", 12)).pack(side="left", padx=10)

# Visit Website Button (Right)
tk.Button(button_frame, text="Visit github", command=open_website, font=("Arial", 12)).pack(side="right", padx=10)

# Result Label
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, wraplength=450, justify="left", font=("Arial", 12)).pack(pady=5)

# Start GUI
root.mainloop()
