def DetectionModule(path):
    import cv2
    from deepface import DeepFace
    # Intitialize variables
    angry, disgust, fear, happy, sad, suprise, neutral = 0, 0, 0, 0, 0, 0, 0
    # Load the cascad
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Read the input video
    if path != 0:
        cap = cv2.VideoCapture(f"{path}")
        # Convert into grayscale
        while (cap.isOpened()):
            ret, frame = cap.read()

            try:
                result = DeepFace.analyze(frame, actions=['emotion'])
                print(result[0]['dominant_emotion'])
                if result[0]['dominant_emotion'] == 'angry':
                    angry += 1
                elif result[0]['dominant_emotion'] == 'disgust':
                    disgust += 1
                elif result[0]['dominant_emotion'] == 'fear':
                    fear += 1
                elif result[0]['dominant_emotion'] == 'happy':
                    happy += 1
                elif result[0]['dominant_emotion'] == 'sad':
                    sad += 1
                elif result[0]['dominant_emotion'] == 'suprise':
                    suprise += 1
                elif result[0]['dominant_emotion'] == 'neutral':
                    neutral += 1
            except:
                print("No Face Detected")

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            # Draw rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255),
                              2)
                cv2.putText(frame, result[0]['dominant_emotion'], (x, y - 15),
                            cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2,
                            (255, 255, 255), 2)
            # Display the output
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # Find the most common Emotion shown
        if angry > disgust and angry > fear and angry > happy and angry > sad and angry > suprise and angry > neutral:
            print("The most repeated Emotion is Anger")
        if disgust > angry and disgust > fear and disgust > happy and disgust > sad and disgust > suprise and disgust > neutral:
            print("The most repeated Emotion is Disgust")
        if fear > disgust and fear > angry and fear > happy and fear > sad and fear > suprise and fear > neutral:
            print("The most repeated Emotion is Fear")
        if happy > disgust and happy > fear and happy > angry and happy > sad and happy > suprise and happy > neutral:
            print("The most repeated Emotion is Happy")
        if sad > disgust and sad > fear and sad > happy and sad > angry and sad > suprise and sad > neutral:
            print("The most repeated Emotion is Sad")
        if suprise > disgust and suprise > fear and suprise > happy and suprise > sad and suprise > angry and suprise > neutral:
            print("The most repeated Emotion is Suprise")
        if neutral > disgust and neutral > fear and neutral > happy and neutral > sad and neutral > suprise and neutral > angry:
            print("The most repeated Emotion is Neutral")
    else:
        cap = cv2.VideoCapture(0)
        # Convert into grayscale
        while (cap.isOpened()):
            ret, frame = cap.read()

            try:
                result = DeepFace.analyze(frame, actions=['emotion'])
                print(result[0]['dominant_emotion'])
                if result[0]['dominant_emotion'] == 'angry':
                    angry += 1
                elif result[0]['dominant_emotion'] == 'disgust':
                    disgust += 1
                elif result[0]['dominant_emotion'] == 'fear':
                    fear += 1
                elif result[0]['dominant_emotion'] == 'happy':
                    happy += 1
                elif result[0]['dominant_emotion'] == 'sad':
                    sad += 1
                elif result[0]['dominant_emotion'] == 'suprise':
                    suprise += 1
                elif result[0]['dominant_emotion'] == 'neutral':
                    neutral += 1
            except:
                print("No Face Detected")

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            # Draw rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255),
                              2)
                cv2.putText(frame, result[0]['dominant_emotion'], (x, y - 15),
                            cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2,
                            (255, 255, 255), 2)
            # Display the output
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    # Find the most common Emotion shown
        if angry > disgust and angry > fear and angry > happy and angry > sad and angry > suprise and angry > neutral:
            print("The most repeated Emotion is Anger")
        if disgust > angry and disgust > fear and disgust > happy and disgust > sad and disgust > suprise and disgust > neutral:
            print("The most repeated Emotion is Disgust")
        if fear > disgust and fear > angry and fear > happy and fear > sad and fear > suprise and fear > neutral:
            print("The most repeated Emotion is Fear")
        if happy > disgust and happy > fear and happy > angry and happy > sad and happy > suprise and happy > neutral:
            print("The most repeated Emotion is Happy")
        if sad > disgust and sad > fear and sad > happy and sad > angry and sad > suprise and sad > neutral:
            print("The most repeated Emotion is Sad")
        if suprise > disgust and suprise > fear and suprise > happy and suprise > sad and suprise > angry and suprise > neutral:
            print("The most repeated Emotion is Suprise")
        if neutral > disgust and neutral > fear and neutral > happy and neutral > sad and neutral > suprise and neutral > angry:
            print("The most repeated Emotion is Neutral")
