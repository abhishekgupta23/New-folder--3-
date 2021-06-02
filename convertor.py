import streamlit as st
from textblob import TextBlob
import pandas as pd

st.title ("Converter")
df = pd.read_csv('Language with code.csv')
atk = df.Languages
c=[]
for j in atk:
    v={}
    v=j
    c.append(v)
cod = df.Code
g=[]
for k in cod:
    n={}
    n=k
    g.append(n)


def s(c,n):
    for j in c[0:n]:
        x=j
    return x


a=st.text_input("enter the text you want to convert")
p=0
if a:
    selected_box = st.selectbox(
                'Choose one of the following',
                ('Afrikaans','Albanian','Amharic','Arabic','Armenian','Azerbaijani','Basque','Belarusian','Bengali','Bosnian','Bulgarian','Catalan','Cebuano','Chinese (Simplified)','Chinese (Traditional)','Corsican','Croatian','Czech','Danish','Dutch','English','Esperanto','Estonian', 'Finnish', 'French','Frisian','Galician','Georgian','German','Greek','Gujarati','Haitian Creole','Hausa','Hawaiian','Hebrew','Hindi','Hmong', 'Hungarian','Icelandic','Igbo','Indonesian','Irish','Italian','Japanese', 'Javanese','Kannada','Kazakh','Khmer','Kinyarwanda', 'Korean', 'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese', 'Maori', 'Marathi', 'Mongolian', 'Myanmar (Burmese)', 'Nepali', 'Norwegian', 'Nyanja (Chichewa)', 'Odia (Oriya)', 'Pashto', 'Persian','Polish', 'Portuguese (Portugal, Brazil)', 'Punjabi', 'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian','Sesotho', 'Shona', 'Sindhi', 'Sinhala (Sinhalese)', 'Slovak', 'Slovenian', 'Somali', 'Spanish','Sundanese', 'Swahili', 'Swedish', 'Tagalog (Filipino)', 'Tajik', 'Tamil', 'Tatar', 'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur', 'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu')
                )
    for i in c:
        p=p+1
        if selected_box == i:
           q=s(g,p)
           blob = TextBlob(a)
           te = blob.translate(to=q)
           st.write("translated text :-")
           st.write(te)
