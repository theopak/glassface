import cv2
import os
import urllib
import cStringIO

from django.conf import settings
from django.contrib.auth.models import User

face_db_location = os.path.join(settings.PROJECT_PATH, 'glassface', 'recognition', 'known_faces.db')

classifier = cv2.CascadeClassifier()
classifier.load(os.path.join(settings.PROJECT_PATH, 'glassface', 'recognition', 'haarcascade_frontalface_alt.xml'))

model = cv2.createFisherFaceRecognizer()
try:
    model.load(face_db_location)
except:
    pass

def learn(user, photos):
    for i in range(len(photos)):
        photos[i] = normalize(cv2.imread(photos[i], cv2.CV_LOAD_IMAGE_GRAYSCALE))
    ids = [user.id]*len(photos)
    model.train(photos, ids)
    model.save(face_db_location)

def recognize(photo):
    photo = normalize(cv2.imread(photo, cv2.CV_LOAD_IMAGE_GRAYSCALE))
    id = model.predict(photo)
    try:
        user = User.objects.get(id=id)
    except:
        return None
    return user

def find_good_photos(photos):
    good = []
    for photo in photos:
        file = cStringIO.StringIO(urllib.urlopen(photo).read())
        picture = normalize(cv2.imread(file, cv2.CV_LOAD_IMAGE_GRAYSCALE))
        faces = classifier.detectMultiScale(picture)
        if len(faces) == 1:
            face = faces[0]
            cropped = picture[face[2]:face[3], face[0]:face[1]]
            if len(cropped) >= 100 and len(cropped[0]) >= 100:
                good.append(photo)
    return good


def normalize(photo):
    faces = classifier.detectMultiScale(photo)
    face = faces[0]
    cropped = photo[face[2]:face[3], face[0]:face[1]]
    if len(cropped) < 100 or len(cropped[0]) < 100:
        raise IOError("Face is too small")
    resized = cv2.resize(cropped, (100, 100))
    return resized