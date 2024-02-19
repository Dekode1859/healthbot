# Health and Fitness Chatbot

To run the app there are two ways:
- Streamlit with Python
- Docker build and run

1. **Local Streamlit**
   - Clone this repo:
     ```
     git clone https://github.com/Dekode1859/healthbot.git
     ```
   - Change into the repo directory:
     ```
     cd healthbot
     ```
   - Create a virtual environment:
     ```
     python3 -m venv env
     ```
   - Activate the virtual environment:
     - On Windows:
       ```
       .\env\Scripts\activate
       ```
     - On Unix or MacOS:
       ```
       source env/bin/activate
       ```
   - Install the requirements:
     ```
     pip install -r requirements.txt
     ```
   - Run the application:
     ```
     streamlit run app.py
     ```
2. **Docker Build and Run**
   - Clone this repo:
     ```
     git clone https://github.com/Dekode1859/healthbot.git
     ```
   - Change into the repo directory:
     ```
     cd healthbot
     ```
   - Build the Docker image:
     ```
     docker build -t streamlitapp .
     ```
   - Run the Docker container:
     ```
     docker run -p 8501:8501 streamlitapp
     ```

## Additional Info on CI/CD deployment using Docker and Github Actions Flow[Link](https://johnardavies.github.io/technical/front_end/)