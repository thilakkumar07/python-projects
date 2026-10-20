import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import os
from pathlib import Path 
from pypdf import PdfReader
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

# .env ஃபைலை லோடு செய்ய
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("Error: Not found. Please check your API key!")

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", google_api_key=GOOGLE_API_KEY)

def load_pdf(pdf_path):
  print(f"\nLoading PDF...")
  reader = PdfReader(pdf_path)
  content = "\n".join(page.extract_text() for page in reader.pages)

  print(f"Loaded: {Path(pdf_path).name}")
  print(f"Pages: {len(reader.pages)}")
  print(f"Characters: {len(content):,}")

  return content

def main():
  print("PDF Question Answering Tool\n\n")
  pdf_path = input("Enter the path to your PDF file: ").strip()

  if not Path(pdf_path).exists():
    print(f"Error: File not found: {pdf_path}")
    return 

  pdf_content = load_pdf(pdf_path)
  system_prompt = f"""You are a helpful assistant that answers about this PDF document.
  Document content: 
  {pdf_content}
  Please answer questions based only on the information in this document. If the answer is not in the document, say so.
  """
  messages = [SystemMessage(content=system_prompt)]
  print(f"Ready for Questions!")

  question_count = 0
  while True:
    question = input("\nAsk a question (or 'quit' to exit): ").strip()

    if question.lower() in ['quit', 'exit', 'q']:
      break
    if not question:
      continue

    messages.append(HumanMessage(content=question))
    print(f"\nThinking...")
    response = llm.invoke(messages)

    answer_text = response.content

    print("\nAnswer: ")
    print(answer_text)

    messages.append(response)
    question_count += 1

  print(f"\n Done! Analyzed a 1 PDF with {question_count} questions.")

if __name__ == "__main__":
  main()
