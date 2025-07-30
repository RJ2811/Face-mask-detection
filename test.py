from tensorflow.keras.models import load_model

model = load_model('mask_detector.model')

# Save it in HDF5 format
model.save("C://Users//rithvik jaswal//Downloads//Face-Mask-Detection-master//Face-Mask-Detection-master//mask_detector.h5")