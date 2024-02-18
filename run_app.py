import sys
import pickle
from process_request import create_chain

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")


if __name__ == "__main__":
    with open("preprocessed_data.pkl", "rb") as f:
        vectordata = pickle.load(f)
    new_chain = create_chain(vectordata)
    history = []
    
    while True:
        print("\nВаш вопрос:")
        question = input()
        result = new_chain({"question": question, "chat_history": history})
        history.append((question, result["answer"]))
        print("\nAI ассистент:")
        # print(result["answer"])
