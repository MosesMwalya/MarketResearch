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

msgs = ["If you could have any superpower, what would it be and why? ",
"What is your favorite book or movie, and what makes it special to you? ",
"If you could travel anywhere in the world, where would you go and what would you do there? ",
"What is the most unusual or interesting job you've ever had? ",
"If you could meet any historical figure, who would it be and what one question would you ask them? ",
"What is one thing on your bucket list that you hope to accomplish in the next five years? ",
"If you were an animal, which one would you be and why? ",
"What is a hobby or activity you’ve always wanted to try but haven’t yet? ",
"If you could instantly become an expert in any field, what would it be and why? ",
"What is the best piece of advice you've ever received, and how has it impacted you? ",
"If you were a season, which one would you be and why? ",
"If you could magically learn any language, which one would you choose and why? ",
"What is your favorite way to spend a day off? ",
"If you could swap lives with anyone for a day, who would it be and what would you do? ",
"What is the weirdest food you've ever tried, and did you like it? ",
"What is one talent you wish you had? "
        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" Welcome at Research team meeting! Your presence is valued. "+msg)
