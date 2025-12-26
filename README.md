# 📸 Image Processing Demo

An interactive **Streamlit web application** that demonstrates **basic image processing techniques** using **OpenCV**.
Users can upload an image and view each processing step **one by one** using navigation buttons.

---

##  Description

This project visualizes how an image is processed through multiple stages such as grayscale conversion, blurring, edge detection, thresholding, and rotation.
It is designed to help understand image processing concepts in a **simple and interactive way**.

---

## Technologies Used

* Python
* Streamlit
* OpenCV (cv2)
* NumPy

---

## How It Works

1. The user uploads an image (JPG / PNG).
2. The image is decoded using OpenCV.
3. Required color conversions are applied.
4. Multiple image processing operations are performed.
5. Each processed image is stored and displayed step-by-step.
6. Navigation buttons allow moving between processing stages.

---

## Image Processing Steps

The following operations are applied to the uploaded image:

1. Original Image
2. Grayscale Conversion
3. Image Resizing
4. Gaussian Blur
5. Edge Detection (Canny)
6. Binary Thresholding
7. Histogram Equalization
8. Image Rotation

---

## Project Structure

```text
image-processing-demo/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation & Run

### Clone the repository

```bash
git clone https://github.com/your-username/image-processing-demo.git
cd image-processing-demo
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## Key Concepts Demonstrated

* Image decoding using OpenCV
* Color space conversion (BGR → RGB, Grayscale)
* Common image processing techniques
* Streamlit session state handling
* Interactive UI in Python

---

