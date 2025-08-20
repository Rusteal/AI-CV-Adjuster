from pathlib import Path
from playwright.sync_api import sync_playwright
from datetime import datetime

def html_to_pdf(html_path: str, pdf_path: str):
    html_file = Path(html_path).resolve()
    pdf_file = Path(pdf_path).resolve()
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"file:///{html_file}", wait_until="load")
        page.pdf(path=str(pdf_file),
                 format="A4",
                 margin={"top":"12mm","bottom":"12mm","left":"12mm","right":"12mm"},
                 print_background=True)
        browser.close()

# html_to_pdf("cv.html", "cv.pdf")
if __name__ == "__main__":
    # safer, readable format than raw epoch timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"output_cv/cv_{timestamp}.pdf"
    html_to_pdf("master_cv/cv.html", output_file)
    print(f"Saved CV to {output_file}")
