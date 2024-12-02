# Setup | Client App

Make sure you have `Python 3.12` or higher installed on your machine. You can check this by running `python --version`
in your terminal.
If you don't have Python installed, you can download it [here](https://www.python.org/downloads/).

Clone the repository to your local machine or unzip the file downloaded from Moodle and navigate to the `root` directory
of the project.

<warning>
    <p>
        <b>Do not install packages without virtual environment</b> as it may cause issues with the packages installed on your machine.
    </p>
</warning>


<tabs group="system">
    <tab title="Windows" group-key="windows">
        <p>Create a virtual environment by running:</p>
        <code-block lang="bash">
            python -m venv venv
        </code-block>
        <p>Activate virtual environment by running:</p>
        <code-block lang="bash">
            venv\Scripts\activate
        </code-block>
        <p>Install required packages by running:</p>
        <code-block lang="bash">
            pip install -r requirements.txt
        </code-block>
        <p>Run the app by running:</p>
        <code-block lang="bash">
            python main.py
        </code-block>
    </tab>
    <tab title="Mac" group-key="mac">
        <p>Create a virtual environment by running:</p>
        <code-block lang="bash">
            python3 -m venv venv
        </code-block>
        <p>Activate virtual environment by running:</p>
        <code-block lang="bash">
            source venv/bin/activate
        </code-block>
        <p>Install required packages by running:</p>
        <code-block lang="bash">
            pip install -r requirements.txt
        </code-block>
        <p>Run the app by running:</p>
        <code-block lang="bash">
            python main.py
        </code-block>
    </tab>
    <tab title="Linux" group-key="linux">
        <p>Create a virtual environment by running:</p>
        <code-block lang="bash">
            python3 -m venv venv
        </code-block>
        <p>Activate virtual environment by running:</p>
        <code-block lang="bash">
            source venv/bin/activate
        </code-block>
        <p>Install required packages by running:</p>
        <code-block lang="bash">
            pip install -r requirements.txt
        </code-block>
        <p>Run the app by running:</p>
        <code-block lang="bash">
            python main.py
        </code-block>
    </tab>
</tabs>

### Configuration

<p>
    Don not forget to fill in the `config.ini` file with the correct values for database connection. If you don't have database set up, please refer to the <a href="Set-Up-Database.md">database setup</a> guide.
    You can find the `config.ini` file in the `root` directory of the project.
</p>
<p>
    Here is the template for the `config.ini` file:
</p>
<code-block lang="ini">
    [database]
    host = 
    user = 
    password = 
    schema = e_prescription
</code-block>

<note>
    <p><b>
    Troubleshooting
    </b></p>
    <p>
        If you encounter any issues, make sure you have followed the steps above correctly 
        and especially that you have activated the virtual environment.
    </p>
    <p>
        If the issue persists, please try to run the app in a different virtual environment. Good Luck👍
    </p>
</note>