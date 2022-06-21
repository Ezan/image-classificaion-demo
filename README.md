# image-classificaion-demo
    - Data collection using bing-image-downloader to scrape images from Bing
    - Preprocessing the data by flattening and resizing
    - Splitting the data into train and test data
    - Train the model using SVM
    - Save the model using pickle
    - reuse the model

## Installation instructions
    - Install anaconda
    - Create virtual env via ananconda
        -- conda create -n venv python=1.8
    - Activate the virtual env
        -- source activate venv
    - Install requirements
        -- pip install -r requirement.txt


## How to run the app
    - Run scraper.py to scrape the data for 5 types of bacteria and save the images the data/images directory
        -- python scraper.py
    - Run predicter.py to train the model and save the model
    - Run tester.py to enter an outside image URL to predict the image
    

