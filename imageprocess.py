import cv2
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Image Processing Demo",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
button {
    width: 100%;
    height: 3rem;
    font-size: 1rem;
}
img {
    max-width: 100%;
    height: auto;
}
</style>
""", unsafe_allow_html=True)

st.title("Image Processing Operations")
st.caption("A single image is uploaded and used as the input for all processing. Each time the Next button is clicked, a different image processing operation is applied to the same original image, generating a new processed output such as grayscale conversion, resizing, blurring, edge detection, thresholding, histogram equalization, or rotation. The application displays one processed image at a time, allowing users to navigate through the transformations step by step and download the currently displayed result.")

if "step" not in st.session_state:
    st.session_state.step = 0

uploaded_file = st.file_uploader(
    "Upload an image (JPG / PNG)",
    type=["jpg", "jpeg", "png"]
)

def image_to_bytes(img):
    if len(img.shape) == 2:  # Grayscale
        success, buffer = cv2.imencode(".png", img)
    else:  # RGB
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        success, buffer = cv2.imencode(".png", img_bgr)
    return buffer.tobytes()

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    results = [
        ("Original Image", image_rgb),
        ("Grayscale Image", gray),
        ("Resized Image", cv2.resize(image_rgb, (300, 300))),
        ("Gaussian Blur Image", cv2.GaussianBlur(gray, (7, 7), 0)),
        ("Edge Detection Image", cv2.Canny(gray, 100, 200)),
        ("Thresholding Image", cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]),
        ("Histogram Equalization Image", cv2.equalizeHist(gray)),
        ("Rotated Image", cv2.warpAffine(
            image_rgb,
            cv2.getRotationMatrix2D(
                (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2),
                45, 1.0
            ),
            (image_rgb.shape[1], image_rgb.shape[0])
        ))
    ]

    total_steps = len(results)

    def next_step():
        st.session_state.step = (st.session_state.step + 1) % total_steps

    def prev_step():
        st.session_state.step = (st.session_state.step - 1) % total_steps

    title, current_image = results[st.session_state.step]

    st.subheader(f"{title}")

    st.image(current_image, use_container_width=True)

    image_bytes = image_to_bytes(current_image)

    st.download_button(
        label="Download Image",
        data=image_bytes,
        file_name=f"{title.replace(' ', '_').lower()}.png",
        mime="image/png"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.button("⬅ Previous", on_click=prev_step)

    with col2:
        st.button("Next ➡", on_click=next_step)

else:
    st.info("Upload an image to begin")
