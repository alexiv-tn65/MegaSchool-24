import json
import pandas as pd
from pathlib import Path
from typing import List

from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader


class TgJsonLoader(BaseLoader):
    """Loads json file from telegram or other sources."""

    def __init__(self, path: str):
        self.file_path = path

    def join_stings(self, row):
        date = row['date']
        sender = row['from']
        text = row['text']
        return f'{sender} on {date}: {text}\n\n'

    def load(self):
        p = Path(self.file_path)

        with open(p, encoding="utf8") as f:
            d = json.load(f)

        normalized = pd.json_normalize(d['messages'])
        df_normalized = pd.DataFrame(normalized)

        # filter messages
        df_filtered = df_normalized[
            (df_normalized.type == "message") &
            (df_normalized.text.apply(lambda x: type(x) == str))
            ]

        df_filtered = df_filtered[["date", "text", "from"]]
        text = df_filtered.apply(self.join_stings, axis=1).str.cat(sep='')

        info = {"source": str(p)}

        return [Document(page_content=text, metadata=info)]
