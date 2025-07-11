import cv2
import numpy as np
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(model_complexity=0) # pose detection

BODY_CONNECTIONS = {
    (11, 12), (11, 13), (13, 15), (12, 14), (14, 16),
    (11, 23), (12, 24), (23, 24),
    (23, 25), (25, 27), (27, 29), (29, 31),
    (24, 26), (26, 28), (28, 30), (30, 32),
}

landmark_drawing_color = (0,0, 255)  
head_drawing_color = (0, 255, 255)      

connections = BODY_CONNECTIONS

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # rgb for mediapipe
    result = pose.process(rgb)

    canvas = np.zeros_like(frame)
    
    if result.pose_landmarks:
        h, w, _ = frame.shape
        landmarks = result.pose_landmarks.landmark # list of landmarks
        points = []

        for lm in landmarks: # Convert normalized coordinates to pixel coordinates
            x = int(lm.x * w)
            y = int(lm.y * h)
            points.append((x, y))

        for connection in connections:
            start_idx, end_idx = connection
            if landmarks[start_idx].visibility > 0.5 and landmarks[end_idx].visibility > 0.5:
                cv2.line(frame, points[start_idx], points[end_idx], (0, 255, 0), 2)
                cv2.line(canvas, points[start_idx], points[end_idx], (0, 255, 0), 2)

        joint_indices = [
            11, 12, 13, 14, 15, 16,  # shoulders, elbows, wrists
            23, 24, 25, 26, 27, 28, 29, 30, 31, 32  # hips, knees, ankles, heels, feet
        ]

        for idx in joint_indices:
            if landmarks[idx].visibility > 0.5:
                cv2.circle(canvas, points[idx], 6, landmark_drawing_color, -1)
                cv2.circle(frame, points[idx], 6, landmark_drawing_color, -1)

        head_idx = 0
        left_ear = points[7]
        right_ear = points[8]
        head_width = int(np.linalg.norm(np.array(left_ear) - np.array(right_ear)))

        if landmarks[head_idx].visibility > 0.5:
            cv2.circle(frame, points[head_idx], head_width // 2, head_drawing_color, 1)
            cv2.circle(canvas, points[head_idx], head_width // 2, head_drawing_color, 1)

    cv2.imshow("Live Video", frame)
    cv2.imshow("Body Tracking Net", canvas)

    if cv2.waitKey(1) & 0xFF == 27:  
        break

cap.release()
cv2.destroyAllWindows()