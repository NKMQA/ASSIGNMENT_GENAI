import os
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_pdf(file_path, max_pages=10):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    doc = fitz.open(file_path)
    text = ""
    for page_num in range(min(max_pages, len(doc))):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks

def create_index(chunks):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(chunks)
    return vectorizer, X

def retrieve(vectorizer, X, chunks, query, top_k=2):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, X).flatten()
    best_indices = similarities.argsort()[-top_k:][::-1]
    results = [(chunks[i], similarities[i]) for i in best_indices]
    return results

def main():
    print("Current working directory:", os.getcwd())
    
    pdf_path = "sample.pdf"  # <-- Change this to your PDF filename or full path

    print(f"Reading PDF: {pdf_path}")
    try:
        text = read_pdf(pdf_path, max_pages=10)
    except FileNotFoundError as e:
        print(e)
        return
    
    print(f"Extracted {len(text.split())} words from PDF")
    
    chunks = chunk_text(text)
    print(f"Text chunked into {len(chunks)} pieces")
    
    vectorizer, X = create_index(chunks)
    print("Created TF-IDF index")
    
    while True:
        query = input("\nEnter your question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            print("Exiting...")
            break

        results = retrieve(vectorizer, X, chunks, query, top_k=2)
        print("\nTop relevant chunks:\n")
        for i, (chunk, score) in enumerate(results):
            print(f"Chunk {i+1} (score: {score:.3f}):\n{chunk[:500]}...\n")  # show first 500 chars

if __name__ == "__main__":
    main()
