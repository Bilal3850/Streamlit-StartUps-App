import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('I like it')
st.write('I am writing a small letter')
st.markdown("""
            ### This is Header 3
            - list 1
            - list 2
            - list 3


""")

st.code("""
def foo(num):
    return foo**2
        
x = foo(10)
""")

st.latex("x^2 + y^2 = 2")



df = pd.DataFrame({
    'name':['Bilal', 'Ali', 'Zad'],
    'marks': [20,29,28],
    'age': [28, 38, 20]
})


st.dataframe(df)

st.json({
    'name':['Bilal', 'Ali', 'Zad'],
    'marks': [20,29,28],
    'age': [28, 38, 20]
})

st.metric('Revenue', 'Rs 20L', '-3%')



st.image('cat.jpg')
st.video('video.mp4')

st.sidebar.title('sidebar of streamlit')

col1, col2 = st.columns(2)

with col1:
    st.image('cat.jpg')
    st.image('cat.jpg')
    st.image('cat.jpg')
with col2:
    st.video('video.mp4')   

st.error('error occure')
st.success('complete')
st.warning('warning message')
st.info('give some instruction')

bar = st.progress(0)

for i in range(1, 101):
    # time.sleep(0.10)
    bar.progress(i)

st.chat_input()
st.text_input('email')
st.date_input('enter a date')
st.number_input('inter number')
st.time_input('time')


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
import streamlit as st

email = st.text_input('email')
password = st.text_input('password')
course = st.selectbox('Select course', ['web dev', 'data science', 'devops', 'andriod dev'])

btn = st.button('login')

if btn:
    if email == 'bilalafridi313@outlook.com' and password == 'jamrud':
        st.success('login Successful')
        st.balloons()
        course
    else:
        st.error('incorrect email or password')