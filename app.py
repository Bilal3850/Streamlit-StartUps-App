import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='StartUp Analysis')

# df = pd.read_csv('startup_funding.csv')
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')

def load_overall_analysis():
    st.title('Overall Analysis')

    # Total investment amount
    total_invst = round(df['amount'].sum())
    # Max amount infused in a StartUp
    max = round(df.groupby('startup')['amount'].max()).sort_values(ascending=False).head(1).values[0]
    # Avg amount infused in a startup
    avg = round(df.groupby('startup')['amount'].sum().mean())
    # Total funded startups 
    num_startups = df['startup'].nunique()


    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric('Total', str(total_invst) + ' Cr')
    with col2:
        st.metric('Maximum', str(max) + ' Cr')
    with col3:
        st.metric('Average', str(avg) + ' Cr')
    with col4:
        st.metric('Funded StartUps', str(num_startups) + ' Cr')
    
    st.header('Month on Month Graph')
    selected_option = st.selectbox('Select Type', ['Type', 'Count'])
    if selected_option == 'Type':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig0, ax0 = plt.subplots()
    ax0.plot(temp_df['x_axis'], temp_df['amount'])
    st.pyplot(fig0)

def load_startUp_details(startUp):
    st.title(startUp)
    industry = df[df['startup'] == startUp].groupby(['vertical', 'city'])['amount'].sum().reset_index().rename(columns={'vertical': 'Industry'})

    st.dataframe(industry)
 

def load_investor_details(investor):
    st.title(investor)
    # load the recent investments of the investor
    last5_df = df[df['investors'].str.contains(investor)].head()[['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Invesments')
    st.dataframe(last5_df)

    col1, col2 = st.columns(2)

    with col1:
        # biggest investments
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest Invesments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)

        # Stage Pie chart
        stage_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Stage Invesments')
        fig, ax_1 = plt.subplots()
        ax_1.pie(stage_series, labels=stage_series.index,autopct="%0.01f%%")
        st.pyplot(fig)

    with col2:

        verical_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors invested in')
        fig1, ax2 = plt.subplots()
        ax2.pie(verical_series,labels=verical_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)


        city_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader('City invested in')
        fig1, ax2 = plt.subplots()
        ax2.pie(city_series,labels=city_series.index,autopct="%0.01f%%")
        st.pyplot(fig1)

    print(df.info())

    df['year'] = df['date'].dt.year
    year_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    st.subheader('Year ON Year Investment')

    fig2, ax2 = plt.subplots()
    ax2.plot(year_series.index, year_series.values)
    st.pyplot(fig2)


st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One',['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    load_overall_analysis()
elif option == 'StartUp':
    # st.title('StartUp Analysis')
    select_startUp = st.sidebar.selectbox('Select StartUp', df['startup'].value_counts().index)
    btn_1 = st.sidebar.button('Find StartUp Details')
    load_startUp_details(select_startUp)
    
else:
    select_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    # btn_2 = st.sidebar.button('Find Investor Details')
    # if btn_2:
    load_investor_details(select_investor)