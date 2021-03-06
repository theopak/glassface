import cv2
import os
import urllib
import cStringIO
import numpy as np

from django.conf import settings
from django.contrib.auth.models import User

face_db_location = os.path.join(settings.PROJECT_PATH, 'glassface', 'recognition', 'known_faces.db')

classifier = cv2.CascadeClassifier()
classifier.load(os.path.join(settings.PROJECT_PATH, 'glassface', 'recognition', 'haarcascade_frontalface_alt.xml'))

model = cv2.createLBPHFaceRecognizer()
try:
    model.load(face_db_location)
except:
    pass

def learn(user, urls):
    photos = []
    for i in range(len(urls)-1):
        photo = urllib.urlopen(urls[i]).read()
        f = open("PPPPPP.jpg",'w')
        f.write(photo)
        f.close()
        print os.path.abspath(f.name)
        photos.append(normalize(cv2.imread(os.path.abspath(f.name), cv2.CV_LOAD_IMAGE_GRAYSCALE)))
    ids = [user.id]*len(photos)
    ids = np.array(ids)
    print photos[0],"HI"
    model.train(photos, ids)
    model.save(face_db_location)

def recognize(url):
    photo = cStringIO.StringIO(urllib.urlopen(url).read())
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
    cropped = photo[face[1]:face[1]+face[3], face[0]:face[0]+face[2]]
    print len(cropped),len(cropped[0])
    if len(cropped) < 100 or len(cropped[0]) < 100:
        raise IOError("Face is too small")
    resized = cv2.resize(cropped, (100, 100))
    return resized