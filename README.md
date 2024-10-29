# UI Automation Coding Challenge

### Step-by-Step Guide for Setting Up the Coding Challenge

This guide will walk you through setting up a GitHub repository, creating a virtual environment, organizing project files, and setting up a GitHub Actions workflow for continuous integration.


### Step 1: Create a GitHub Repository

1. **Create a Repository:**
   - Go to GitHub and create a new repository named `UI_Automation_Coding_Challenge`.
   - Clone the repository to your local machine.
   
   ```bash
   git clone https://github.com/your-username/UI_Automation_Coding_Challenge.git
   ```

2. **Open the Project in PyCharm:**
   - Open the cloned repository in your IDE (e.g., PyCharm) for easier setup and development.

---

### Step 2: Set Up Project Structure and Dependencies

1. **Create `requirements.txt`:**
   - Add all necessary dependencies to a `requirements.txt` file to manage packages. Here’s an example for a Selenium project:
   
     ```plaintext
     selenium
     pytest
     pytest-html
     pytest-retry
     ```
     
   - Install dependencies using:
   
     ```bash
     pip install -r requirements.txt
     ```

2. **Set Up a Virtual Environment:**
   - Create a virtual environment to isolate project dependencies.
   
     ```bash
     python -m venv venv
     ```
   
   - Activate the virtual environment:
     - **Windows:** `venv\Scripts\activate`

3. **Create Project Folders:**
   - Create two main packages to organize your test files:
     - **`LocatorPage`**: For element locators.
     - **`ActionPage`**: For actions and methods interacting with locators.


4. **Define Locator and Action Files:**
   - In `LocatorPage`, create a Python file named `Locators_page.py`.
   - In `ActionPage`, create a Python file named `Action_page.py`.

---

### Step 3: Set Up GitHub Workflow for Continuous Integration

1. **Create a `.github/workflows` Directory:**
   - In the root of your project, create a directory to store GitHub Actions workflows.
   

2. **Create the GitHub Actions Workflow File:**
   - Inside `.github/workflows`, create a YAML file named `main.yml`.
   
     ```yaml
     name: UI Automation CI

     on:
       push:
         branches: [main]
       pull_request:
         branches: [main]

     jobs:
       test:
         runs-on: ubuntu-latest

         steps:
           - name: Check out code
             uses: actions/checkout@v2

           - name: Set up Python
             uses: actions/setup-python@v2
             with:
               python-version: '3.8'

           - name: Install dependencies
             run: |
               python -m pip install --upgrade pip
               pip install -r requirements.txt

           - name: Run tests
             run: |
               pytest --html=reports/report.html
             
           - name: Upload test report
             uses: actions/upload-artifact@v2
             with:
               name: test-report
               path: reports/report.html
     ```

3. **Explanation of Workflow Steps:**
   - **Checkout Code**: Checks out your repository’s code so GitHub Actions can access it.
   - **Set up Python**: Configures a specific Python version for the environment.
   - **Install Dependencies**: Installs required dependencies from `requirements.txt`.
   - **Run Tests**: Executes the tests using `pytest` and generates an HTML report.
   - **Upload Test Report**: Uploads the test report so it can be accessed from the workflow summary.

4. **Commit and Push Changes:**
   - Commit your changes to the repository and push them to GitHub.

     ```bash
     git add .
     git commit -m "Setup GitHub Actions CI workflow"
     git push origin main
     ```

---

### Step 4: Verify the Workflow

1. **Check GitHub Actions:**
   - Go to your GitHub repository and open the **Actions** tab.
   - Verify that the workflow runs successfully on each push or pull request to the main branch.
