import firebase_admin
from firebase_admin import credentials, firestore


# Initialize Firebase
cred = credentials.Certificate('./service_key/arc-ai-platform-firebase-adminsdk-w5b50-01b91c00da.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Reference the collection storing your code submissions
code_submissions_ref = db.collection('codeSubmissions')

# Example query: Fetch all documents
docs = code_submissions_ref.get()
for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))

# More specific query example: Get documents where 'styling' is greater than 70
query = code_submissions_ref.where('settings.styling', '>', 70)
results = query.get()
for result in results:
    print(result.to_dict())
