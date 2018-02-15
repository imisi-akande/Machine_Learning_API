# Machine_Learning_API# Machine_Learning_API


## Machine learning API for automated detection of fake news with Django Rest Framework 

This sample project is a post-phase of applying Machine learning algorithms for detection of fake news. The Machine learning process involves data scraping from three different sources, data wrangling, data preparation, applying logistic regresion model for training our data sets and evaluation in a separate repo of have to do with users been able to create posts and also add comments. This project employ about 26000 data samples. The fakeness level takes categorical values of zeros and ones. 0 for real news 1 for fake news.


## Dependencies

To setup and run the sample code, you're going to install Python3, pip, virtualenvwrapper.

## Setup

To setup and run the sample code you need to clone the repo
        
1. Create a virtualenv to isolate our package dependencies locally
    virtual env
    
2. Activate the virtual environment
    source env/bin/activate
    
3. Install Python Requirements:

        pip install -r requirements.txt
        
4. For the server run :

        python manage.py runserver        
        
## Routes

**GET**
----
  <_The User will be able to view all news in the database_>
  
  * **URL**

  <_/api/news/)_>   -   http://127.0.0.1:8000/api/news/
  
  
* **URL**
 <_The User will be able to retrieve news by id_>
 
  <_/api/news/<int:pk>)_>    -   http://127.0.0.1:8000/api/news/6/
  
  
 *  **URL Params** 
 **Required:**
 `id=[IntField]`
 
 * **URL**
 <_The User will be able to retrieve news by keywords/words_>
 
  <_/api/news/$)_>    -   http://127.0.0.1:8000/api/news/?q=trump
  
  
 *  **URL Params** 
 **Required:**
 `headline=[StringField]`
 `body=[TextField]`
 
 * **URL**
 <_The User will be able to filter out fake news and real news_>
 
  <_/api/news/$search='')_>    -  http://127.0.0.1:8000/api/news/?search=0  |  http://127.0.0.1:8000/api/news/?search=1
  
  
 *  **URL Params** 
 **Required:**
 `id=[IntField]`
        