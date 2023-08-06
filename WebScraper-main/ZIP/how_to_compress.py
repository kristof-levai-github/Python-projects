import zipfile
import os

archive_name = "C:\\Users\\ADMIN\\Desktop\\python\\web\\webscraper_testsites\\ZIP\\test.zip"

# Check if the ZIP file already exists
if os.path.exists(archive_name):
    os.remove(archive_name)
    print("Existing ZIP file removed.")

# Create a new Zip file object
with zipfile.ZipFile(archive_name, "w") as zipf:
    # Add files to the Zip archive with full paths
    zipf.write("C:\\Users\ADMIN\\Desktop\\python\\web\\webscraper_testsites\\EMAIL\\how_to_send_email_attachments.py", "how_to_send_email_attachments.py")
    zipf.write("C:\\Users\ADMIN\\Desktop\\python\\web\\webscraper_testsites\\EMAIL\\howto_email_yourself.py", "howto_email_yourself.py")

print("Archive created successfully.")