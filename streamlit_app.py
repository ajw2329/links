import streamlit as st
from st_functions import st_button, load_css, st_project_button, st_project_sub_button
from PIL import Image

load_css()

#st.write("[![Star](https://img.shields.io/github/stars/dataprofessor/links.svg?logo=github&style=social)](https://gitHub.com/dataprofessor/links)")

col1, col2, col3 = st.columns(3)
col2.image(Image.open('76d28216ebff.png'))

st.header('Andrew Wallace, Ph.D.')

st.info('Data Scientist and Computational Biologist at Genentech')

icon_size = 20

st_button('github', 'https://github.com/ajw2329', 'GitHub', icon_size)
#st_button('youtube', 'https://youtube.com/codingprofessor', 'Coding Professor YouTube channel', icon_size)
#st_button('medium', 'https://data-professor.medium.com/', 'Read my Blogs', icon_size)
#st_button('twitter', 'https://twitter.com/thedataprof/', 'Follow me on Twitter', icon_size)
st_button('linkedin', 'https://www.linkedin.com/in/ajw2329', 'Follow me on LinkedIn', icon_size)
#st_button('keyboard', 'https://anjowall.shinyapps.io/digital_divide_dash/', 'Visualizing the Digital Divide', icon_size)
st_project_button('Projects', icon_size)
st_project_sub_button('https://anjowall.shinyapps.io/digital_divide_dash/', 'Visualizing the Digital Divide')
#st_button('newsletter', 'https://sendfox.com/dataprofessor/', 'Sign up for my Newsletter', icon_size)
#st_button('cup', 'https://www.buymeacoffee.com/dataprofessor/', 'Buy me a Coffee', icon_size)
