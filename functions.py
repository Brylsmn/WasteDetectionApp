import cv2
from ultralytics import YOLO
from PIL import Image, ImageTk  

def yolo_real_time(video_label, model_path='best.pt', conf_threshold=0.5, width=640, height=480):
    
    model = YOLO(model_path)
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def update_frame():
        ret, frame = cap.read()
        if not ret:
            return

        results = model.predict(frame, conf=conf_threshold, show=False, verbose=False)
        annotated_frame = results[0].plot()

        frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

        resized_frame = cv2.resize(frame_rgb, (width, height))
        img = Image.fromarray(resized_frame)
        imgtk = ImageTk.PhotoImage(image=img)

        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)
        video_label.after(10, update_frame)

    update_frame()

def yolo_image_input(image_path, image_label, model_path='best.pt', conf_threshold=0.5, width=640, height=480):
    
    model = YOLO(model_path)
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image from {image_path}")
        return

    results = model.predict(image, conf=conf_threshold, show=False, verbose=False)
    annotated_image = results[0].plot()

    resized_image = cv2.resize(annotated_image, (width, height))

    image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image_rgb)
    imgtk = ImageTk.PhotoImage(image=img)

    image_label.imgtk = imgtk
    image_label.configure(image=imgtk)
