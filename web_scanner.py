import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebScanner:
    def __init__(self):
        self.target_url = None

    def get_target_url(self):
        while True:
            self.target_url = input("Enter the URL to scan: ").strip()
            if self.target_url:
                break
            print("URL cannot be empty. Please try again.")

    def scan(self):
        if not self.target_url:
            print("No target URL specified. Please provide a valid URL.")
            return
        
        try:
            response = requests.get(self.target_url)
            if response.status_code == 200:
                print("Page successfully fetched!")
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract and display page title
                page_title = soup.title.string.strip() if soup.title else "N/A"
                print(f"Page Title: {page_title}")

                # Extract and display meta description (if available)
                meta_description = soup.find("meta", attrs={"name": "description"})
                if meta_description:
                    print(f"Meta Description: {meta_description['content'].strip()}")

                # Extract and display all links (href attributes)
                links = soup.find_all('a', href=True)
                if links:
                    print("\nLinks found:")
                    for link in links:
                        href = link['href']
                        full_url = urljoin(self.target_url, href)
                        print(f"  {full_url}")

            else:
                print(f"Failed to fetch page. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    scanner = WebScanner()
    scanner.get_target_url()
    scanner.scan()
