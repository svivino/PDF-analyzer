#please note most of main isn't my code and I'm not sure who to credit. I will update if I find who to credit
import PyPDF2
from textblob import TextBlob

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text

def analyze_sentiment(text):
    """Analyze sentiment using TextBlob"""
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

# Update this with the actual PDF path
# If pdf is in same file that you are running from you dont need the whole path
#ex file.pdf is okay vs dive/docs/file.pdf
pdf_file = "File.pdf"

text = extract_text_from_pdf(pdf_file)

if text.strip():  # Check if text was extracted
    polarity, subjectivity = analyze_sentiment(text)
    print(f"Sentiment Polarity: {polarity} (range: -1 to 1)")
    print(f"Subjectivity: {subjectivity} (range: 0 to 1, higher means more opinionated)")
    #print(text)
    #remove the hash above to make it print the transcript 
else:
    print("No text extracted from PDF. Check if the file contains selectable text.")
