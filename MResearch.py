# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# Welcome to MR&CI Wednesday meet
        
         """)

msgs = [
 "as a Genz, What worries do you have?",
 "as a Genz, what are your expectations from your parents and other relatives",
 "as a Genz, how does your day look like, starting from when you wake up to the time you sleep",
 "as a Genz, What are some things your parents and older relatives have told you that don't make sense?"
 "as a Genz, What is your preferred way to rewind?",
 "as a Genz, if you could meet any historical figure, who would it be and what one question would you ask them?",
 "as a Genz, what brands would you love to be associated with?",
 "as a Genz, What is one talent you wish you had?"]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" Karibu sana to Research team meeting! Your presence is valued. "+msg)
