import streamlit as st
from PIL import Image
from textblob import TextBlob
import streamlit.components.v1 as components

container = st.container()

title = '<p style="font-family:Lucida Handwriting; color:White; font-size: 50px;">Mood Analyser</p>'
st.markdown(title, unsafe_allow_html=True)

def main():
    
    rad = st.sidebar.selectbox("Navigation", ["Home","Mood Analyser"])

    if rad == "Mood Analyser":

        title = '<p style="font-family:Sans-serif; color:White; font-size: 20px;">Certain Events can make you feel sad, anxious, surprised, excited or shocked. You can still make yourself feel better by watching a movie which would relax you, listening to songs which may calm you down or maybe read an adventure book!!</p>'
        st.markdown(title, unsafe_allow_html=True)


        title = '<p style="font-family:Courier; color:White; font-size: 30px;">Just Answer the below questions to get recommendations based on your current mood</p>'
        st.markdown(title, unsafe_allow_html=True)

        q1=st.radio(
        "1: When was the last time you where really happy?",
            ('I dont remember' ,'Few months ago' ,'Few weeks ago' ,'Few days ago','Few moments ago'))
            
        if q1=="I dont remember" :
            q1=1;
        elif q1=="Few months ago":
            q1=2;
        elif q1=="Few weeks ago":
            q1=3;
        elif q1=="Few days ago":
            q1=4;
        else :
            q1=5;


        q2=st.radio(
            "2. Overall how do you rate your comfortness around people: Low(1) and high (5)",
            ('1' ,'2' ,'3' ,'4','5'))

        if q2=="1" :
            q2=1;
        elif q2=="2":
            q2=2;
        elif q2=="3":
            q2=3;
        elif q2=="4":
            q2=4;
        else :
            q2=5;

        q3=st.radio(
            "3.Rate how often you face problems in your work/studies?",
            ( 'Always',   'Very often'   ,   'Sometimes'  ,  'Not much'  ,  'No'))

        if q3=="Always":
            q3=1
        elif q3=="Very often":
            q3=2
        elif q3=="Sometimes":
            q3=3
        elif q3=="Not much":
            q3=4
        else:
            q3=5

        q4=st.radio(
            "4.Rate how often you feel angry/irritated?",
            ( 'Always',   'Very often'   ,   'Sometimes'  ,  'Not much'  ,  'No'))

        if q4=="Always" :
            q4=1;
        elif q4=="Very Often":
            q4=2;
        elif q4=="Sometime":
            q4=3;
        elif q4=="Not much":
            q4=4;
        else :
            q4=5;

        q5=st.radio(
            "5.When was the last time you felt good about yourself?",
            ('I dont remember' ,'Few months ago' ,'Few weeks ago' ,'Few days ago','Few moments ago'))

        if q5=="I dont remember" :
            q5=1;
        elif q5=="Few months ago":
            q5=2;
        elif q5=="Few weeks ago":
            q5=3;
        elif q5=="Few days ago":
            q5=4;
        else :
            q5=5;

        q6=st.radio(
            "6.Rate how often you face problems in your work/studies?",
            ('Always' ,'Very Often' ,'Sometimes' ,'Not much','Never'))
        if q6=="Always" :
            q6=1;
        elif q6=="Very Often":
            q6=2;
        elif q6=="Sometime":
            q6=3;
        elif q6=="Not much":
            q6=4;
        else :
            q6=5;

        q7=st.radio(
            "7.How often do you overthink?",
            ('Always' ,'Very Often' ,'Sometimes' ,'Not much','Never'))

        if q7=="Always" :
            q7=1;
        elif q7=="Very Often":
            q7=2;
        elif q7=="Sometime":
            q7=3;
        elif q7=="Not much":
            q7=4;
        else :
            q7=5;

        q8=st.radio(
            "8.How content/happy you are with your relationship and family??",
        ('Never','Not much','Sometimes','Very often','Always'))
        if q8=="Never" :
            q8=1;
        elif q8=="Not much":
            q8=2;
        elif q8=="Sometimes":
            q8=3;
        elif q8=="Very Often":
            q8=4;
        else :
            q8=5;  

        q9=st.radio(
            "9.How often do you feel anxious/awkward around people?",
            ('Always' ,'Very Often' ,'Sometimes' ,'Not much','Never'))

        if q9=="Always" :
            q9=1;
        elif q9=="Very Often":
            q9=2;
        elif q9=="Sometime":
            q9=3;
        elif q9=="Not much":
            q9=4;
        else :
            q9=5;


        q10=st.radio(
        "10. How often you feel like sharing things with people?",
        ('Never','Not much','Sometimes','Very often','Always'))
        if q10=="Never" :
            q10=1;
        elif q10=="Not much":
            q10=2;
        elif q10=="Sometimes":
            q10=3;
        elif q10=="Very Often":
            q10=4;
        else :
            q10=5;  

        text_area = '<p style="font-family:Courier; color:White; font-size: 25px;">How was your day? Please describe in 20 words. You can describe about the various events that took place today. </p>'
        st.markdown(text_area, unsafe_allow_html=True)

        text_area = st.text_area("Start Typing here - ")
        blob = TextBlob(text_area)
        sentiment = blob.sentiment.polarity

        count = q1+q2+q3+q4+q5+q6+q7+q8+q9+q10
        print(count)
        print(sentiment)

        if st.button("Submit"):
            
            if(sentiment!=0):
                if(count > 35 and sentiment > 0.3):

                    st.subheader("Here are the list of movies, songs and books that you should watch to feel better\n")
                    # images
                    st.title("Songs")

                    image = Image.open('images\Happy\happybooks1.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\Happy\happybooks2.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\Happy\happybooks3.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\Happy\happymovies1.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\Happy\happymovies2.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\Happy\happymovies3.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\Happy\happysongs1.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\Happy\happysongs2.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\Happy\happysongs3.jpg')
                    st.image(image, caption=' ',width = 720)

                    st.write("List of books:\n 1. The panic years.\n 2. Carry on Jeeves\n 3. That moment when.\n 4. Bon Mortimer\n 5. The Idiot\n 6. The Timewaster letters.\n 7. The happiest project \n . 8. The Art of happiness \n . 9. The Wangs\n 10. How to be Normal")
                    st.write("List of movies:\n 1. Liar Liar \n 2. Inside out \n 3. Men in black \n 4. Housefull\n 5. Good Boys\n 6. Welcome.\n 7. Klown\n 8. Phir Hera Pheri\n 9. Khichadi\n 10.Dhamaal")
                    st.write("List of songs: \n 1. Bruno Mars \n 2. Maroon 5 \n 3. Justin Beiber\n 4. Taylor Swift\n 5. Beatles\n 6. Britney Sphears\n 7. Jennifer Lopes\n 8. Kelly Clarkson\n 9. Dua lipa\n 10. Shawn Mendes")

                if(count < 25 and count!=0 and sentiment < -0.3):
                    ans = '<p style="font-family:Courier; color:cayn; font-size: 40px;">Select Selection3 from sidebar menu to get your recommendations!  </p>'
                    st.markdown(ans, unsafe_allow_html=True)

                    image = Image.open('images\sad\sbook.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\sad\sbook1.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\sad\sbook2.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\sad\smovie.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\sad\smovie1.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\sad\smovie2.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\sad\ssong.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\sad\ssong1.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open('images\sad\ssong2.jpg')
                    st.image(image, caption=' ',width = 720)

                    st.subheader("Here are the list of movies, songs and books that you should watch to feel better\n")
                    st.subheader("List of books:\n 1. How to stay happy \n 2. When life gives you lemons \n 3. How to become a people magnet\n 4. The Aspirant\n 5. Ikigai\n 6. Being an Indian Teenager\n 7. Before the coffee gets cold\n 8. Fear Not Be strong\n 9. Better than best friends.\n 10. You only live once.")
                    st.subheader("List of movies:\n 1. Marley and me \n 2. Harry potter \n 3. The pursuit of happiness\n 4. Legally Blond\n 5. Little miss sunshine\n 6. Pitch Perfect\n 7. The Princess Diaries\n 8. The Shawshank Redemption\n 9. La La Land\n 10. Clueless")
                    st.subheader("List of songs:\n 1. Stronger \n 2. Titanium \n 3. Fight song\n 4. Yun hi chala chal\n 5. Hall of Fame\n 6. Roar\n 7. Jeete hain chal\n 8. Phir se ud chala\n 9. Chak de india\n 10. Roobaroo")

                if(25 < count < 35 and -0.3 < sentiment < 0.3):

                    image = Image.open(r'images\Neutral\B1.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open(r'images\Neutral\B2.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open(r'images\Neutral\B3.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open(r'images\Neutral\m1.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open(r'images\Neutral\m2.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open(r'images\Neutral\m3.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open(r'images\Neutral\s1.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open(r'images\Neutral\s2.jpg')
                    st.image(image, caption=' ',width = 720)

                    image = Image.open(r'images\Neutral\s3.jpg')
                    st.image(image, caption=' ',width = 720)

                    st.subheader("Here are the list of movies, songs and books that you should watch to feel better\n")
                    st.subheader("List of books:\n 1. Hardy boys \n 2. Harry potter \n 3. Percy Jackson\n 4. Famous Five\n 5. Secret seven\n 6. Mahabharata Secret\n 7. The girl on the train\n 8. Da vinci code\n 9. The sands of time\n 10. Angels and demons")
                    st.subheader("List of movies:\n 1. Angels and demons \n 2. Justice League \n 3. Spiderman\n 4. Avengers\n 5. Batman\n 6. Martian\n 7. Da vinci code\n 8. Gravity\n 9. Interstellar\n 10. Fast and furious")
                    st.subheader("List of songs:\n 1. Cold play \n 2. Kesha \n 3. Beatles\n 4. Arijit singh\n 5. A R Rahman\n 6. Atif Aslam\n 7. Pitbull\n 8. Drake\n 9. OneRepublic\n 10. Charlie Puth")


    if rad == "Home":    

        name = st.text_input("Your Name: ")

        if st.button("Submit"):
            st.title("Hey There! {name}.".format(name = name))

        title = '<p style="font-family:Lucida Handwriting; color:White; font-size: 30px;">Every day is a new day, a fresh morning for a new start. Start it with a cheerful smile on your face and hopes in your heart. </p>'
        st.markdown(title, unsafe_allow_html=True)

        html_temp = '<img src="https://img00.deviantart.net/bef5/i/2017/007/9/f/walking_through_the_winter_forest_by_caillean_photography-daulss7.jpg" alt="img" height="500" width="700">'
        st.markdown(html_temp, unsafe_allow_html = True)

        title = '''<p style="font-family:Lucida Handwriting; color:White; font-size: 25px;">We want to help people overcome the problems related to depression and mood swings by providing appropriate recommendations according to their mood.  Study says that 43% Indians suffering from depression. 26 % were suffering mild depression, 11 % were feeling moderately depressed, and 6 % were facing severe symptoms of depression. Most of the times we ourselves don't know whether we are experiencing depression. If we ignore this for longer time then it can get severe after some time. To prevent this to happen, we can analyze the emotions and help lift up the mood. </p>'''
        st.markdown(title, unsafe_allow_html=True)

        title = '''<p style="font-family:Lucida Handwriting; color:cyan; font-size: 25px;"> To get to know more about our Mood Analyser project, just select `Mood Analyser` from the sidebar. </p>'''
        st.markdown(title, unsafe_allow_html=True)

    
if __name__ == '__main__':
    main()

