import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title('Random Choice')
    
    options = []

    choice1 = st.text_input('Choice 1')
    choice2 = st.text_input('Choice 2')

    options = options.append([choice1, choice2])

    add = st.button('Add Choice')
    if add:
        choice3 = st.text_input('Choice 3')
        options = options.append(choice3)

        add2 = st.button('Add Choice')
        if add2:
            choice4 = st.text_input('Choice 4')
            options = options.append(choice4)

            add3 = st.button('Add Choice')
            if add3:
                choice5 = st.text_input('Choice 5')
                options = options.append(choice5)
    
    flips = st.number_input('Number of total flips', min_value=1, max_value=1000000, step=1)

    

    score = pd.DataFrame([np.random.choice(options) for i in range(0,flips)])

    st.write(score.value_counts())

main()