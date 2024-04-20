import os
import requests
from lxml import html

# Specify the directory containing the files
directory = "/nfs/libgen/23000"

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Check if the file has no extension
    if '.' not in filename:
        # Construct the URL with the file's MD5 hash
        url = f"https://libgen.is/book/index.php?md5={filename}"
        print(f"Processing {filename} - Fetching URL: {url}")

        # Fetch the page
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML
            tree = html.fromstring(response.content)

            # XPath queries
            title_xpath = "/html/body/table/tr[2]/td[3]/b/a/text()"
            additional_xpath = "/html/body/table/tr[11]/td[4]/text()"
            language_xpath = "/html/body/table/tr[7]/td[2]/text()"

            # Extract data using XPaths
            title_result = tree.xpath(title_xpath)
            additional_result = tree.xpath(additional_xpath)
            language_result = tree.xpath(language_xpath)

            # Check and concatenate the results
            if title_result and additional_result and language_result:
                # Process the title to include only the first six words
                shortened_title = ' '.join(title_result[0].split()[:6])
                combined_result = f"{shortened_title}.{additional_result[0]}"
                print("Combined Result:", combined_result)

                # Check language and decide action
                if language_result[0] in ['Arabic', 'English', 'German']:
                    # Define the new filename with combined result
                    new_filename = os.path.join(directory, combined_result.replace('/', '-'))  # Replace '/' to avoid path issues
                    old_filename = os.path.join(directory, filename)

                    # Rename the file
                    try:
                        os.rename(old_filename, new_filename)
                        print(f"Renamed '{filename}' to '{combined_result}'")
                    except OSError as e:
                        print(f"Error renaming file '{filename}' to '{combined_result}': {e}")
                else:
                    # Delete the file if the language is not Arabic, English, or German
                    os.remove(os.path.join(directory, filename))
                    print(f"Deleted '{filename}' due to unsupported language: {language_result[0]}")
            else:
                print("One of the XPaths did not return data or missing language info.")
        else:
            print(f"Failed to retrieve the webpage for {filename}, status code: {response.status_code}")
    else:
        print(f"Skipping {filename} - it has an extension.")
