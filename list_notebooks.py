from evernote.api.client import EvernoteClient

from config import evernote_personal_token

    
if __name__ == '__main__':

    client = EvernoteClient(
        token=evernote_personal_token,
        sandbox=True
    )
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print('%s - %s' % (notebook.guid, notebook.name))
