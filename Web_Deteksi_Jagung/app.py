from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense
# pyrefly: ignore [missing-import]
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Mengatur folder penyimpanan untuk gambar yang di-upload pengguna
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Workaround for Keras version mismatch error: Unrecognized keyword arguments passed to Dense: {'quantization_config': None}
class CustomDense(Dense):
    @classmethod
    def from_config(cls, config):
        if 'quantization_config' in config:
            del config['quantization_config']
        return super().from_config(config)

# 1. REVISI: ME-LOAD MODEL PERTAMA YANG TIDAK ADA KATA "BAGUS"-NYA (Akurasi 73%)
MODEL_PATH = 'model_jagung.h5'
model = load_model(MODEL_PATH, custom_objects={'Dense': CustomDense})

# 2. MENDEFINISIKAN URUTAN KELAS PENYAKIT (Sesuai urutan abjad dataset)
class_names = ['Blight', 'Common Rust', 'Gray Leaf Spot', 'Healthy']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Mengecek apakah ada file gambar yang dikirim
        if 'file' not in request.files:
            return render_template('index.html', hasil="Tidak ada file gambar.")
        
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html', hasil="Nama file kosong.")
            
        if file:
            # Menyimpan file gambar yang diupload ke folder static/uploads
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # 3. PREPROCESSING GAMBAR AGAR SESUAI STANDAR INPUT CNN
            img = image.load_img(filepath, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalisasi piksel

            # 4. MELAKUKAN PREDIKSI MENGGUNAKAN MODEL
            predictions = model.predict(img_array)
            predicted_class_index = np.argmax(predictions)
            
            # Mengambil nama penyakit dan persentase keyakinannya
            predicted_class_name = class_names[predicted_class_index]
            confidence = round(np.max(predictions) * 100, 2)

            # Mengirimkan hasil kembali ke halaman web (index.html)
            return render_template('index.html', 
                                   hasil=predicted_class_name, 
                                   akurasi=confidence, 
                                   gambar=filepath)
            
    return render_template('index.html', hasil=None)

if __name__ == '__main__':
    app.run(debug=True)