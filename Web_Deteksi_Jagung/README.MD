# 🌿 AgroScan — Corn Leaf Disease Detection Web App

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=flat&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)

**AgroScan** adalah aplikasi web berbasis kecerdasan buatan (AI) yang mendeteksi penyakit pada daun jagung secara otomatis menggunakan model **Convolutional Neural Network (CNN)**. Proyek ini dikembangkan menggunakan **Flask** untuk backend dan antarmuka web modern yang responsif dengan vanilla CSS.

## 🚀 Demo Aplikasi
> [!TIP]
> 🔗 **Coba Aplikasi Langsung:** [Link Live Demo Anda (misal: Render/Hugging Face)]

*(Masukkan GIF atau Screenshot aplikasi di sini)*

## ✨ Fitur Utama
- **Klasifikasi Instan**: Deteksi 4 kelas kondisi daun jagung: *Blight*, *Common Rust*, *Gray Leaf Spot*, dan *Healthy*.
- **Akurasi Real-time**: Menampilkan tingkat keyakinan (confidence level) prediksi model dalam bentuk bar persentase yang interaktif.
- **Modern UI/UX**: Desain antarmuka bertema organik (dark mode) dengan transisi mulus, fitur *drag-and-drop* file, dan visualisasi interaktif.
- **Robust Model Workaround**: Implementasi penanganan kustom untuk memuat model Keras versi berbeda (`CustomDense` adapter).

## 🛠️ Teknologi yang Digunakan
- **Backend**: Python, Flask
- **Machine Learning**: TensorFlow / Keras (CNN Model)
- **Frontend**: HTML5, CSS3 (Custom Glassmorphism Design), Vanilla JavaScript
- **Dataset**: [Sebutkan dataset yang digunakan, contoh: Kaggle Corn Leaf Infection Dataset]

## 🧠 Arsitektur Model CNN
Model CNN dilatih untuk mengklasifikasikan gambar daun berukuran `224x224` piksel dengan normalisasi nilai piksel (`1/255.0`).
- **Input Layer**: `224x224x3`
- **Output Layer**: 4 Kelas (Softmax)
- **Akurasi**: ~73% (pada pengujian model awal)

## 💻 Cara Menjalankan Secara Lokal

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/username/Web_Deteksi_Jagung.git
   cd Web_Deteksi_Jagung
   ```

2. **Buat dan aktifkan Virtual Environment:**
   ```bash
   python -m venv .venv
   # Windows (PowerShell/Command Prompt):
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependensi:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi:**
   ```bash
   python app.py
   ```
   Buka `http://127.0.0.1:5000` di browser Anda.
