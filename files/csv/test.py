from tempfile import NamedTemporaryFile
import shutil
import csv
 
# Create a temporary file in write mode ("w")to hold new values
tempfile = NamedTemporaryFile(mode="w", delete=False)
# Fields are the columns for the CSV file we wish to update
fields = ["ID", "Position", "Salary", "Joining Date", "Grade"]
# Open the CSV file in read mode ("r").
# We will write into the temporary file first.
 
with open("employees.csv", "r") as csvfile, tempfile:
    # Create reader and writer objects using csv library.
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    # Loop trow the rows of the CSV file
    for row in reader:
        # Based on the value of the "ID" column, create edits on the temporary file
        if row["ID"] == str(1947):
            print("Updating row with ID=", row["ID"])
            # New data
            new_data = ["Managing Director", 55000, "9/24/2009"]
            # Update the dictionary data with the new data, new_data.
            row["Position"], row["Salary"], row["Joining Date"] = new_data
        # create a complete row of data to write into the temporary file
        row = {
            "ID": row["ID"],
            "Position": row["Position"],
            "Salary": row["Salary"],
            "Joining Date": row["Joining Date"],
        }
        # write the row with the new data
        writer.writerow(row)
# Move the temporary file to the original CSV file. This replaces employees.csv.
 
shutil.move(tempfile.name, "employees.csv")