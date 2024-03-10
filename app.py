import streamlit as st
from keras.models import load_model
from tensorflow import keras
import numpy as np 
from PIL import Image
import os

st.title("See Who You Are")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# if uploaded_image is not None:
#     st.image(uploaded_image, caption='Uploaded Image.', use_column_width=True)
print(uploaded_image)

model = load_model('model.keras')

if uploaded_image is not None:
    uploaded_image = Image.open(uploaded_image)
    resized_image = uploaded_image.resize((64, 64))
    # st.image(resized_image, caption='Resized Image.', use_column_width=True)
    image = keras.utils.img_to_array(
        img = resized_image
    )
    #print(image)
    image = image[None , :,:,:]
    pred = model.predict(image)

    for i in range(len(pred[0])):
        if pred[0][i] == np.max(pred[0]):
            print(i)
            break 

    #directory = 'data/'

    folder_names = ['Aamir_Khan', 'Abhay_Deol', 'Abhishek_Bachchan', 'Aftab_Shivdasani', 'Aishwarya_Rai', 'Ajay_Devgn', 'Akshaye_Khanna', 'Akshay_Kumar', 'Alia_Bhatt', 'Ameesha_Patel', 'Amitabh_Bachchan', 'Amrita_Rao', 'Amy_Jackson', 'Anil_Kapoor', 'Anushka_Sharma', 'Anushka_Shetty', 'Arjun_Kapoor', 'Arjun_Rampal', 'Arshad_Warsi', 'Asin', 'Ayushmann_Khurrana', 'Bhumi_Pednekar', 'Bipasha_Basu', 'Bobby_Deol', 'Deepika_Padukone', 'Disha_Patani', 'Emraan_Hashmi', 'Esha_Gupta', 'Farhan_Akhtar', 'Govinda', 'Hrithik_Roshan', 'Huma_Qureshi', 'Ileana_DCruz', 'Irrfan_Khan', 'Jacqueline_Fernandez', 'John_Abraham', 'Juhi_Chawla', 'Kajal_Aggarwal', 'Kajol', 'Kangana_Ranaut', 'Kareena_Kapoor', 'Karisma_Kapoor', 'Kartik_Aaryan', 'Katrina_Kaif', 'Kiara_Advani', 'Kriti_Kharbanda', 'Kriti_Sanon', 'Kunal_Khemu', 'Lara_Dutta', 'Madhuri_Dixit', 'Manoj_Bajpayee', 'Mrunal_Thakur', 'Nana_Patekar', 'Nargis_Fakhri', 'Naseeruddin_Shah', 'Nushrat_Bharucha', 'Paresh_Rawal', 'Parineeti_Chopra', 'Pooja_Hegde', 'Prabhas', 'Prachi_Desai', 'Preity_Zinta', 'Priyanka_Chopra', 'Rajkummar_Rao', 'Ranbir_Kapoor', 'Randeep_Hooda', 'Rani_Mukerji', 'Ranveer_Singh', 'Richa_Chadda', 'Riteish_Deshmukh', 'R_Madhavan', 'Saif_Ali_Khan', 'Salman_Khan', 'Sanjay_Dutt', 'Sara_Ali_Khan', 'Shahid_Kapoor', 'Shah_Rukh_Khan', 'Shilpa_Shetty', 'Shraddha_Kapoor', 'Shreyas_Talpade', 'Shruti_Haasan', 'Sidharth_Malhotra', 'Sonakshi_Sinha', 'Sonam_Kapoor', 'Suniel_Shetty', 'Sunny_Deol', 'Sushant_Singh_Rajput', 'Taapsee_Pannu', 'Tabu', 'Tamannaah_Bhatia', 'Tiger_Shroff', 'Tusshar_Kapoor', 'Uday_Chopra', 'Vaani_Kapoor', 'Varun_Dhawan', 'Vicky_Kaushal', 'Vidya_Balan', 'Vivek_Oberoi', 'Yami_Gautam', 'Zareen_Khan']

    # for folder_name in os.listdir(directory):
    #     if os.path.isdir(os.path.join(directory, folder_name)):
    #         folder_names.append(folder_name)

    print(folder_names[i])
    st.write(folder_names[i])