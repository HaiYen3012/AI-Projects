import cv2

video_path = "datasets/video/video1.mp4"
output_image_path = "video1_frame.jpg"

cap = cv2.VideoCapture(video_path)
success, frame = cap.read() # Đọc frame đầu tiên
if success:
    cv2.imwrite(output_image_path, frame)
    print(f"Đã lưu frame đầu tiên vào {output_image_path}")
else:
    print("Không thể đọc video.")
cap.release()