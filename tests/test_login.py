from pages.login_page import LoginPage

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.load("https://practicetestautomation.com/practice-test-login/")
    login_page.login("student", "Password123")
    assert "logged-in-successfully" in driver.current_url