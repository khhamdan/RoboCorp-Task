from RPA.Browser.Selenium import Selenium

browser_lib = Selenium()


def open_the_website(url):
    browser_lib.open_available_browser(url)


button_selector = "css:search-button"
input_selector = "css:search-input"

def click_button(selector):
    browser_lib.click(selector)

def input_search_term(selector, term):
    browser_lib.input_text(selector, term)
    browser_lib.press_keys(selector, "ENTER")


# Define a main() function that calls the other functions in order:
def main():
    try:
        open_the_website("www.nytimes.com")
        click_button(button_selector)
        input_search_term(input_selector, "Riplle") 
    finally:
        browser_lib.close_all_browsers()


# Call the main() function, checking that we are running as a stand-alone script:
if __name__ == "__main__":
    main()