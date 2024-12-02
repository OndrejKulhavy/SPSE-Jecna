# Setup | Database

First, make sure you have `MySQL` installed on your machine. If not, you can download it from the official
website [here](https://dev.mysql.com/downloads/installer/).

<note>
    <p><b>
    Locating the database file
    </b></p>
    <p>
        Database export file is located in the <code>database/export/schema_with_demo_data.sql</code> directory of the project.
    </p>
</note>

<tabs group="system">
    <tab title="MySQL Workbench" group-key="workbench">
        <p>Open MySQL Workbench and run follow instructions:</p>
        <ol>
            <li>Open MySQL Workbench</li>
            <li>Click on the <b>Server</b> menu</li>
            <li>Click on the <b>Data Import</b> option</li>
            <li>Click on the <b>Import from Self-Contained File</b> option</li>
            <li>Locate the database export file in the <code>database/export</code> directory of the project</li>
            <li><b>Default Target Schema</b> should be empty</li>
            <li>Click on the <b>Start Import</b> button</li>
        </ol>
    </tab>
    <tab title="Windows Console" group-key="console">
        <p>Open the console and run the following command:</p>
        <code-block lang="bash">
            mysql -u [name of user] -p < database/export/schema_with_demo_data.sql
        </code-block>
        <p>Enter your password when prompted.</p>
        <note>
            <p><b>
            Note
            </b></p>
            <p>
                Make sure you have `mysql` added to your system's PATH.
            </p>
        </note>
    </tab>
</tabs>