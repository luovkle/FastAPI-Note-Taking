import json
import zipfile
from secrets import token_urlsafe
from typing import List

from app.core.config import settings
from app.models import Note


def generate_zip_file(notes: List[Note]) -> str:
    file = f"{token_urlsafe()}.zip"
    with zipfile.ZipFile(f"{settings.STATIC_DIR}/{file}", "a") as zf:
        for note in notes:
            body = {"title": note.title, "content": note.content, "tags": note.tags}
            zf.writestr(f"{note.title}.json", json.dumps(body))
    return file
