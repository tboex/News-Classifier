# News-Classifier
## Dependencies 
 **Required python Libraries**
### Machine Learning
   - numpy `pip install numpy`
   - scikit-learn `pip install sklearn`
   - stop_words `pip install stop_words`
### Web interaction
   - requests `pip install requests`
   - Beautiful Soup 4 `pip install bs4`
   - webbrowser `pip install webbrowser`
### Saving
   - pickle `pip install pickle`
   
## How-to-Run

### Starting the Importer
   _Run with Python 2.7 (_Not tested on Python 3.x_)_
   
   `python firstSetup/first.py` 
   
   **Be aware "first.py" will reset any currently trained model you have**
   
   `python main.py`
   
#### Choose a source
   1. EXIT
   
   2. New York Times
   
   3. Fox News
   
   4. MSNBC
   
   5. the Guardian
   
   6. Townhall
   
   7. Christian Science Monitor
   
   // TODO - Add More
     
   #### Enter a link to a story on the selected website
    `New York Times
     -Enter full URL:`
    
   #### You then can keep entering sources to increase your training set
    After you have enough sources you can hit `0 - EXIT` and be directed to the prediction UI.  
    **Make sure to have a large training set**
   #### Closing
    When you exit the program will automatically save all of your trained model and automatically reopen upon launch.
