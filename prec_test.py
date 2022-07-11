import pickle
import streamlit as st
pickle_in = open("D:\Downloads\Prec_Prediction.sav", 'rb') 
classifier = pickle.load(pickle_in)
def prediction(DATE, AWND, TMAX, TMIN, WDF2, WDF5, WSF2, WSF5) :
  prediction = classifier.predict([ [ DATE, AWND, TMAX, TMIN, WDF2, WDF5, WSF2, WSF5 ] ])
  if prediction >= 0.5 :
     pred = 'Precipitation would occur in Los Angeles'
  else :
     pred = 'Precipitation would not occur in Los Angeles'   
  return pred
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Precipitation Prediction App</h1> 
    </div> 
    """  
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)      
    # following lines create boxes in which user can enter data required to make prediction 
    DATE = st.date_input("ENTER THE DATE") 
    AWND = st.number_input("ENTER THE AWND") 
    TMAX = st.number_input("ENTER THE MAXIMUM TEMPERATURE") 
    TMIN = st.number_input("ENTER THE MINIMUM TEMPERATURE") 
    WDF2 = st.number_input("ENTER THE WDF2") 
    WDF5 = st.number_input("ENTER THE WDF5") 
    WSF2 = st.number_input("ENTER THE WSF2") 
    WSF5 = st.number_input("ENTER THE WSF5") 
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(DATE, AWND, TMAX, TMIN, WDF2, WDF5, WSF2, WSF5) 
        print(result)
if __name__=='__main__': 
    main()