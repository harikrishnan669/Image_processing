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

st.title("📸 Image Processing Demo")
st.caption("Step-by-step visualization")


uploaded_file = st.file_uploader(
    "Upload an image (JPG / PNG)",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    results = [
        ("Original Image", image_rgb),
        ("Grayscale Image", gray),
        ("Resized Image", cv2.resize(image_rgb, (300, 300))),
        ("Gaussian Blur", cv2.GaussianBlur(gray, (7, 7), 0)),
        ("Edge Detection", cv2.Canny(gray, 100, 200)),
        ("Thresholding", cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]),
        ("Histogram Equalization", cv2.equalizeHist(gray)),
        ("Rotated Image", cv2.warpAffine(
            image_rgb,
            cv2.getRotationMatrix2D(
                (image_rgb.shape[1] // 2, image_rgb.shape[0] // 2),
                45, 1.0
            ),
            (image_rgb.shape[1], image_rgb.shape[0])
        ))
    ]

    if "step" not in st.session_state:
        st.session_state.step = 0

    st.subheader(results[st.session_state.step][0])
    st.image(
        results[st.session_state.step][1],
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Previous"):
            st.session_state.step = (st.session_state.step - 1) % len(results)

    with col2:
        if st.button("Next"):
            st.session_state.step = (st.session_state.step + 1) % len(results)

else:
    st.info("Upload an image to begin")
