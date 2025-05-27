import cv2
import pickle
import os
import face_recognition
from supabase import create_client, Client
from dotenv import load_dotenv


# Supabase setup
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Importing student images
folderPath = 'images'
PathList = os.listdir(folderPath)
imgList = []
studentIds = []

for path in PathList:
    img = cv2.imread(os.path.join(folderPath, path))
    imgList.append(img)
    studentIds.append(os.path.splitext(path)[0])

# Check existing images in Supabase Storage
existing_images = supabase.storage.from_('images').list()  
existing_image_names = [img['name'] for img in existing_images]

# Upload missing images to Supabase Storage
for path in PathList:
    if path not in existing_image_names:  # Only upload if the image does not exist
        fileName = os.path.join(folderPath, path)
        with open(fileName, 'rb') as file:
            supabase.storage.from_('images').upload(path, file) 

print(studentIds)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

print("Encoding Started")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Completed")

# Save the encoding data to a pickle file
file = open("EncodeFile.p", 'wb')  
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")

# Upload missing encodings to Supabase
for student_id, encoding in zip(studentIds, encodeListKnown):
    existing_record = supabase.table('encodings').select('student_id').eq('student_id', student_id).execute()
    if not existing_record.data:  
        supabase.table('encodings').insert({
            'student_id': student_id,
            'encoding': encoding.tolist() 
        }).execute()

print("Encodings and images uploaded to Supabase.")