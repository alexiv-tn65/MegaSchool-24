import pickle
from process_request import create_chain


if __name__ == "__main__":
    with open("preprocessed_data.pkl", "rb") as f:
        vectordata = pickle.load(f)
    new_chain = create_chain(vectordata)
    chat_history = []
    print("Chat with your docs!")
    while True:
        print("Ваш вопрос:")
        question = input()
        result = new_chain({"question": question, "chat_history": chat_history})
        chat_history.append((question, result["answer"]))
        print("AI ассистент:")
        print(result["answer"])