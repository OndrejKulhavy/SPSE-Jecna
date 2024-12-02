# Requirements

Create a user interface and database for any activity falling within the scope of public administration in the Czech Republic, according to the list: [Agenda List](https://archi.gov.cz/znalostni_baze:seznam_agend). The database must have at least six tables. Within the database, there must be at least one M:N relationship and at least two database views. Use the following data types for attributes: Real Number (`float`), Logical Value (`bool`), Enumeration (`enum`), String (`string`), Date and Time (`datetime`).

## User Interface or API Functionalities

1. **Insertion, Deletion, and Modification of Information:**
   - Allow insertion, deletion, and modification of information/records that are stored in more than one table. For example, inserting an order that has items, etc.

2. **Transactions Across Multiple Tables:**
   - Perform transactions across more than one table. For example, transferring credit points between two accounts, etc.

3. **Generate Summary Report:**
   - Generate a summary report containing meaningful aggregated data from at least three tables in your database, such as the count and sums of purchases by city, etc. The report must have a header and footer.

4. **Data Import:**
   - Import data into at least two tables from CSV, XML, or JSON format.

5. **Configuration in a File:**
   - Configure the entire program in a configuration file.

## Submission

Submit the following:
- **Test Scenarios in PDF Format:**
  - A PDF with a test scenario for running the application, including configuration and database structure import.
  - At least three additional test scenarios in PDF format for testing all the above points, including all types of errors and configuration possibilities.

- **Documentation:**
  - Proper documentation containing everything from Appendix 1—Checklist in Czech or English.

## Program Requirements

- The program must react reasonably to all possible errors and may require user cooperation to resolve the issue. This needs to be captured in the test scenarios.

- The program must use design patterns and best practices where appropriate.

- The program does not need to include unit tests; instead, it must include test scenarios for testers. The tester is a person who will test the application.

- Use any programming language or group of languages taught in school or approved by your teacher. Ensure that you do not share your source code with any classmates.
