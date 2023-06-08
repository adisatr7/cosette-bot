import firebase_admin
from firebase_admin import credentials, firestore

# Path to your service account key JSON file
service_account_key_path = "./api/firebase-adminsdk.json"

# Initialize the Firebase Admin SDK
cred = credentials.Certificate(service_account_key_path)
app = firebase_admin.initialize_app(cred)

# Export the database client so it can by other classes/files
db = firestore.client(app)

# Print a 'connection successful' message to console
print("Connected to Firebase successfully!")
