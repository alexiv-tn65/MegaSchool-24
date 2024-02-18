import argparse
import pickle

from langchain.vectorstores.faiss import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from telegram_json_loader import TgJsonLoader

embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

def prepare_data_file(data_file_path):
    loader = TgJsonLoader(data_file_path)
    loaded_data = loader.load()

    splitter = CharacterTextSplitter(separator="\n\n", chunk_size=512, chunk_overlap=20)
    document = splitter.split_documents(loaded_data)

    faiss_vectorstore = FAISS.from_documents(document, embedding_function)

    # create preprocessed file
    with open("preprocessed_data.pkl", "wb") as f:
        pickle.dump(faiss_vectorstore, f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('json_file_path', type=str,
                        help='Json(*.json) file from telegram or other sources')
    args = parser.parse_args()
    file_path = args.json_file_path
    prepare_data_file(file_path)
