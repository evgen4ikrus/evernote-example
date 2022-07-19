from dotenv import load_dotenv
import os

load_dotenv()

evernote_consumer_key = os.getenv("EVERNOTE_CONSUMER_KEY")
evernote_consumer_secret = os.getenv("EVERNOTE_CONSUMER_SECRET")
evernote_personal_token = os.getenv("EVERNOTE_PERSONAL_TOKEN")

journal_template_note_guid = os.getenv("JOURNAL_TEMPLATE_NOTE_GUID")
journal_notebook_guid = os.getenv("JOURNAL_NOTEBOOK_GUID")

inbox_notebook_guid = os.getenv("INBOX_NOTEBOOK_GUID")
