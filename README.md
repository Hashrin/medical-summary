# Medical Record Summarizer


# Goal
The goal of this project is to make the lives of doctors who process insurance applications a lot easier. Doctors have to go through a lot of medical records of the applicant who applies for a new insurance policy. This is a time-consuming process. We can use LLMs here to provide a concise and key summary of the medical records.
You can also use only the relevant parts to just generate summaries of your medical records.

Please note that this is a hobby projects, and that LLMs can hallucinate. More serious work shall be done to tackle hallucination.

# Setup
* step 1: Create a virtual environment using tools like miniconda or venv. Always code your Python projects in virtual environments.
* step 2: Generate the crendentials file by setting up Google OAuth. Once you set it up and sign in initially, you will receive the access token and refresh token which you can further use in this project. Knowledge about the OAuth setup is a mandatory prerequisite. You can read further here: https://support.google.com/cloud/answer/6158849?hl=en
* step 3: Run `pip install -r requirements.txt` to install the dependencies. Since this project was built in parallel with another in the same virtual environment, there could be a lot of unnecessary dependencies. Identify and install only the ones required.
* step 4: Run `uvicorn main:app` to start the server
* step 5: When you receive an email with the medical records of a patient, hit the `process-new-email` endpoint locally. It will read the latest email, summarize the medical records, and send an email with an attachment of the summary back to the sender.
* step 6: Only PDF records are supported at present. Feel free to add additional support.


**IMPORTANT**: Run `sudo apt install wkhtmltopdf` if you want the Ubuntu system to support HTML to PDF conversion.
