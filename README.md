# ReceiptScanPrediction
 
This solution trains an linear classifier to predict receipt scan.

# Requirement
Python >= 3.8, Pip, Docker

# Setup & Run
NOTE: Please run ```pip install requirements.txt``` to install dependencies for both training and inferencing.

**Inference**
1. Open a command line tool, navigate to the project directory. run ```python3 app.py```.
2. Visit [localhost:8020](http://localhost:8020), enter a date in MM/DD/YYYY format and click submit.
3. Run ```Ctrl+C``` in the same command line window to abort/exit.

**Training**
1. Prepare your data file, or use the one provided by the project directory.
2. In a command line tool, enter ```jupyter notebook```, it will automatically open a window.
3. In the window, navigate to project folder, double click the file ```Train.ipynb```, this will open the file in a new window.
4. (Optional) In the new window, if you want to experinment with your own file, replace url with your data file's path.
5. Select Run - Run All Cells, this command will train and export model weights along with some performance insights.

# Docker
NOTE: Docker version is not usable due to a weird gradio error (not invoking function calls with button click).
1. Open a command line tool, navigate to ```./app``` directory of the project directory.
2. Run ```docker build -t gefei_fetch_ml ./``` to build image.
3. Run ```docker run -p 8123:8020 gefei_fetch_ml``` to run the image, visit the site with [localhost:8123](http://localhost:8123), you can replace 8123 with any ports you wish to use.
4. Run ```docker stop gefei_fetch_ml``` to stop container.
5. Run ```docker rm gefei_fetch_ml``` to remove the container.
