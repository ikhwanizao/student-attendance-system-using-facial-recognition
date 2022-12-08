import face_recognition
import numpy as np
import os

def Recognizer(details):
    known_face_encodings = []
    known_face_names = []

    # base_dir = os.path.dirname(os.path.abspath(__file__))
    # image_dir = os.path.join(base_dir, "static")
    # image_dir = os.path.join(image_dir, "profile_pics")

    # base_dir = os.getcwd()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # os.chdir("..")
    base_dir = os.getcwd()
    image_dir = os.path.join(base_dir,"{}\{}\{}".format('static','images','Student_Images'))
    # print(image_dir)
    names = []


    for root,dirs,files in os.walk(image_dir):
        for file in files:
            if file.endswith('jpg') or file.endswith('png'):
                path = os.path.join(root, file)
                img = face_recognition.load_image_file(path)
                label = file[:len(file)-4]
                img_encoding = face_recognition.face_encodings(img)[0]
                known_face_names.append(label)
                known_face_encodings.append(img_encoding)
                
    face_locations = []            
    face_encodings = []

    while True:
        

        face_locations = face_recognition.face_locations()
        face_encodings = face_recognition.face_encodings(face_locations)
        face_names = []


        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_face_encodings, np.array(face_encoding), tolerance = 0.6)

            face_distances = face_recognition.face_distance(known_face_encodings,face_encoding)	
            
            try:
                matches = face_recognition.compare_faces(known_face_encodings, np.array(face_encoding), tolerance = 0.6)

                face_distances = face_recognition.face_distance(known_face_encodings,face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    face_names.append(name)
                    if name not in names:
                        names.append(name)
            except:
                pass