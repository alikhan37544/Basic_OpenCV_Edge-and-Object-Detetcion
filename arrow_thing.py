import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe hands detection
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Set up hand detection parameters
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Open webcam
cap = cv2.VideoCapture(0)

# Track the previous state of the hand (open or closed)
is_hand_closed = False

def detect_hand_gesture(hand_landmarks):
    # Get landmark coordinates for the tip of the thumb and tip of the pinky
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y

    # Get base position of each finger
    thumb_base = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y
    pinky_base = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y

    # Simple heuristic: Check if fingers are closed by comparing the tip and base y coordinates
    fingers_folded = all([
        thumb_tip > thumb_base,
        index_tip > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y,
        middle_tip > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y,
        ring_tip > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y,
        pinky_tip > pinky_base
    ])

    return fingers_folded

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Flip the frame horizontally for a mirrored effect
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hand landmarks
    result = hands.process(rgb_frame)

    # Variable to track if any action is performed
    action_performed = False

    # If hand landmarks are detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Detect if the hand is open or closed
            if detect_hand_gesture(hand_landmarks):
                # Hand is closed, trigger continuous right arrow press
                if not is_hand_closed:
                    print("Pressing and holding right arrow")
                    pyautogui.keyDown('right')
                    is_hand_closed = True
                cv2.putText(frame, "Right Arrow (Held)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                action_performed = True
            else:
                # Hand is open, trigger continuous left arrow press
                if is_hand_closed:
                    print("Releasing right arrow")
                    pyautogui.keyUp('right')
                    is_hand_closed = False

                print("Pressing and holding left arrow")
                pyautogui.keyDown('left')
                cv2.putText(frame, "Left Arrow (Held)", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                action_performed = True

    if not action_performed:
        # If no action is performed, release both keys
        if is_hand_closed:
            print("Releasing right arrow")
            pyautogui.keyUp('right')
            is_hand_closed = False
        print("Releasing left arrow")
        pyautogui.keyUp('left')

    # Display the frame
    cv2.imshow('Hand Gesture Control', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()

