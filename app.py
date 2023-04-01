import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title('Random Choice')
    
    # options = []

    choice1 = str(st.text_input('Choice 1'))
    choice2 = str(st.text_input('Choice 2'))
    
    flips = int(st.number_input('Number of total flips', min_value=1, max_value=1000000, step=1))

    go = st.button("Let's begin")    
    if go:
        options = [choice1,choice2]
        
        score = pd.DataFrame([np.random.choice(options, p=[0.5,0.5]) for i in range(0,flips)])

        count = score.value_counts(sort=False)

        st.write('Total Count for %s: '%choice1, str(count[choice1]))
        st.write('Total Count for %s: '%choice2, str(count[choice2]))
        options.sort()
        fig, ax = plt.subplots()
        ax.pie(x=count, labels=options, autopct="%.1f%%")

        st.pyplot(fig)

main()