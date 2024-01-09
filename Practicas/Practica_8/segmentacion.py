import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np

class ImageSegmentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Segmentation App")

        self.image_path = "wish_you_were_here.jpg"
        self.image = cv2.imread(self.image_path)
        self.segmented_image = np.zeros_like(self.image)

        self.h_var = tk.IntVar()
        self.s_var = tk.IntVar()
        self.v_var = tk.IntVar()

        # Crear controles
        ttk.Label(root, text="Hue (0-179):").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(root, text="Saturation (0-255):").grid(row=1, column=0, padx=5, pady=5)
        ttk.Label(root, text="Value (0-255):").grid(row=2, column=0, padx=5, pady=5)

        ttk.Scale(root, from_=0, to=179, orient=tk.HORIZONTAL, variable=self.h_var).grid(row=0, column=1, padx=5, pady=5)
        ttk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, variable=self.s_var).grid(row=1, column=1, padx=5, pady=5)
        ttk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, variable=self.v_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(root, text="Segmentar", command=self.segment_image).grid(row=3, column=0, columnspan=2, pady=10)

        # Etiquetas para mostrar las imágenes
        self.label_original = ttk.Label(root)
        self.label_original.grid(row=4, column=0, padx=5, pady=5)
        self.label_segmented = ttk.Label(root)
        self.label_segmented.grid(row=4, column=1, padx=5, pady=5)

        # Mostrar la imagen original
        self.update_label(self.image, self.label_original)

    def segment_image(self):
        # Convertir la imagen a espacio de color HSV
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

        # Obtener los valores de los sliders
        h_value = self.h_var.get()
        s_value = self.s_var.get()
        v_value = self.v_var.get()

        # Crear una máscara basada en los valores de los sliders
        lower_bound = np.array([h_value - 10, max(0, s_value - 30), max(0, v_value - 30)])
        upper_bound = np.array([h_value + 10, min(255, s_value + 30), min(255, v_value + 30)])
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

        # Aplicar la máscara a la imagen original
        self.segmented_image = cv2.bitwise_and(self.image, self.image, mask=mask)

        # Mostrar la imagen segmentada
        self.update_label(self.segmented_image, self.label_segmented)

    def update_label(self, image, label):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = self.resize_image(image, 300)
        image = Image.fromarray(image)
        image_tk = ImageTk.PhotoImage(image=image)
        label.config(image=image_tk)
        label.image = image_tk

    def resize_image(self, image, max_width):
        original_height, original_width, _ = image.shape
        ratio = max_width / original_width
        height = int(original_height * ratio)
        return cv2.resize(image, (max_width, height))

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageSegmentationApp(root)
    root.mainloop()
