import spacy

# Load spaCy model (en_core_web_sm is a small pre-trained model)
nlp = spacy.load("en_core_web_sm")

# Define a dictionary to store your data (replace with your data source)
data = {
    "capital of France": "Paris",
    "highest mountain in the world": "Mount Everest",
    "largest country in Africa": "Algeria"
}

def answer_query(question):
  """
  This function takes a question as input and tries to answer it using the data dictionary.
  """
  # Use spaCy for basic named entity recognition (NER)
  doc = nlp(question)
  for ent in doc.ents:
    if ent.text.lower() in data:
      return data[ent.text.lower()]
  # No answer found based on NER, provide a generic response
  return "I couldn't find information related to your question."

# Get user query as input
question = input("Ask me a question: ")
answer = answer_query(question)

# Print the answer
print(answer)