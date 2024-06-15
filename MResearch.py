# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import random

st.write("""
 
# Welcome to B&M Mission cascade
        
         """)

msgs = ['Your tech insights are like hidden gems in the digital finance landscape.',
        'Your determination in tackling tech challenges is truly inspiring',
        'Your dedication to excellence is like a heavenly virtue, infusing our projects with the essence of success and achievement',
        'Your tech skills are like the backbone of our digital infrastructure, providing stability and reliability in an ever-changing landscape',
        'You demonstrates a high level of creativity in developing innovative brand communication strategies',
        'Your tech insights are like guiding stars in the digital universe, illuminating paths to innovation and progress. Keep shining bright and leading the way',
        'Your determination in the face of technical challenges is like a force of nature. Your resilience and tenacity propel us forward, overcoming obstacles and achieving greatness.',
        'Your tech expertise is like a cornerstone, providing stability and strength to our digital endeavors. Keep building and fortifying our technological foundations!',
        'Your tech insights are like a guiding light, illuminating the path to innovation and progress.',
        'Your strategic thinking and problem-solving abilities are invaluable assets to our team. Keep shining bright!',
        'Looking gorgeous as ever! loving the outfit also, we see the glow.',
        'Your bubbly yet grounded approach to everything is a breath of fresh air in this tech space. You are doing well, keep up!',
        'Your warmth and appreciation for people radiates all through'
        ]


f_name = st.text_input('Enter your first name')

    
    
if st.button('SUBMIT'):
    intpos = random.randint(0,len(msgs))
    name = f_name.capitalize()
    msg = msgs[intpos]
    
    st.write(name +" Welcome to B&M Mission Cascade. "+msg)
