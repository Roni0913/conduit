import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
# texts for the modification and creation
text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar ullamcorper pharetra. Donec faucibus posuere turpis, id tincidunt lacus euismod et. Morbi in diam scelerisque, imperdiet nulla ut, facilisis lacus. Donec laoreet nunc ac sapien accumsan, ut facilisis erat finibus. Etiam suscipit ac ex quis ornare. Nulla eu massa sagittis, porttitor eros eget, varius sapien. Ut cursus tortor tempus dui ultrices cursus. Fusce at dui scelerisque, dignissim turpis et, blandit eros. ' \
       'Integer ullamcorper tempus ligula, ac lobortis nulla dignissim at. Aliquam ullamcorper ligula vel augue tempus, sit amet consequat nulla hendrerit. Aliquam risus quam, luctus sit amet risus eu, elementum blandit sem. Praesent sit amet nunc nec mi interdum pretium id feugiat tortor. Pellentesque pharetra, felis sit amet iaculis posuere, orci diam molestie arcu, ut consequat ligula massa eget lectus. Vestibulum rhoncus aliquam tristique. Quisque finibus purus eget commodo vehicula. Pellentesque sit amet nulla scelerisque, vestibulum augue in, condimentum neque. Vivamus eget iaculis tortor. Nam nec velit sed dui gravida interdum. Integer vehicula suscipit sagittis.'
text2 = '2 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar ullamcorper pharetra. Donec faucibus posuere turpis, id tincidunt lacus euismod et. Morbi in diam scelerisque, imperdiet nulla ut, facilisis lacus. Donec laoreet nunc ac sapien accumsan, ut facilisis erat finibus. Etiam suscipit ac ex quis ornare. Nulla eu massa sagittis, porttitor eros eget, varius sapien. Ut cursus tortor tempus dui ultrices cursus. Fusce at dui scelerisque, dignissim turpis et, blandit eros. ' \
        'Integer ullamcorper tempus ligula, ac lobortis nulla dignissim at. Aliquam ullamcorper ligula vel augue tempus, sit amet consequat nulla hendrerit. Aliquam risus quam, luctus sit amet risus eu, elementum blandit sem. Praesent sit amet nunc nec mi interdum pretium id feugiat tortor. Pellentesque pharetra, felis sit amet iaculis posuere, orci diam molestie arcu, ut consequat ligula massa eget lectus. Vestibulum rhoncus aliquam tristique. Quisque finibus purus eget commodo vehicula. Pellentesque sit amet nulla scelerisque, vestibulum augue in, condimentum neque. Vivamus eget iaculis tortor. Nam nec velit sed dui gravida interdum. Integer vehicula suscipit sagittis.'


class TestCondiutApp(object):
    # Chrome setup for testing
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get('http://localhost:1667')
        time.sleep(1)

    # Chrome quit
    def teardown(self):
        self.driver.quit()

    # Login function
    def login(self):
        self.driver.find_element_by_partial_link_text('Sign in').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('r1@gmail.com')
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('Rr0123456')
        self.driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()

    # New article function
    def new_article(self, title, short_description, text_data, tags):
        time.sleep(2)
        self.driver.find_element_by_partial_link_text('New Article').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(title)

        self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').send_keys(
            short_description)

        self.driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]').clear()
        self.driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]').send_keys(
            text_data)

        self.driver.find_element_by_xpath('//input[@placeholder="Enter tags"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Enter tags"]').send_keys(tags)

        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(2)

    # # Test0
    def test__home_page_appearances(self):
        assert self.driver.title == 'Conduit'

    # TEST3 (COOKIE ACCEPT)
    def test_cookie_accept(self):
        self.driver.maximize_window()
        cookie_accept = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'cookie__bar__buttons__button--accept'))
        )
        cookie_accept.click()
        try:
            WebDriverWait(
                self.driver, 5).until(
                EC.visibility_of_element_located((By.ID, 'cookie-policy-panel'))
            )
            not_found = False
        except:
            not_found = True
        time.sleep(2)
        assert not_found

    # TEST1 (REGISTRATION)
    def test_sign_up(self):
        self.driver.maximize_window()
        self.driver.find_element_by_partial_link_text('Sign up').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys('R1')
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('r1@gmail.com')
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('Rr0123456')
        self.driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
        time.sleep(2)
        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'swal-text'))
        )

        assert element.text == 'Your registration was successful!'

    # TEST2 (LOGIN)
    def test_login(self):
        self.driver.maximize_window()
        self.driver.find_element_by_partial_link_text('Sign in').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys('r1@gmail.com')
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('Rr0123456')
        self.driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'R1'))
        )
        assert element.text == 'R1'

    def test_add_new_article(self):
        self.driver.maximize_window()
        self.login()
        time.sleep(2)
        self.driver.find_element_by_partial_link_text('New Article').click()
        # Article title
        time.sleep(2)
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys('RA1')
        # Short description
        self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').send_keys(
            'Roni JAT exam1')
        # Article text
        self.driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]').clear()
        self.driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]').send_keys(text)
        # Article tags
        self.driver.find_element_by_xpath('//input[@placeholder="Enter tags"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Enter tags"]').send_keys('exam, JAT, Roni')

        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(2)

        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
        )
        assert element.text == 'RA1'
        article_content = self.driver.find_element_by_class_name('article-content')
        assert article_content.find_element_by_xpath('//p').text == text

    # TEST5 (MODIFY ARTICLE)
    def test_modify_article(self):
        self.driver.maximize_window()
        self.login()
        random_nr = int(time.time())
        random_title = 'RA1mod' + str(random_nr)
        self.new_article(random_title, 'RA1 modify', text, 'exammod')
        self.driver.find_element_by_partial_link_text('Edit Article').click()
        time.sleep(2)
        # Article title
        article_title = self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
        assert article_title.get_property('value') == random_title
        article_title.clear()
        article_title.send_keys('RA1modnew')

        # Short description new
        short_description = self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]')
        assert short_description.get_property('value') == 'RA1 modify'
        short_description.clear()
        short_description.send_keys(
            'RA1 modify new')
        # Article text new
        article_text = self.driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
        assert article_text.get_property('value') == text
        article_text.clear()
        self.driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]').send_keys(
            text2)
        # Article tags new
        self.driver.find_element_by_xpath('//input[@placeholder="Enter tags"]').clear()
        self.driver.find_element_by_xpath('//input[@placeholder="Enter tags"]').send_keys('exammodnew')

        self.driver.find_element_by_xpath('//button[@type="submit"]').click()
        time.sleep(2)
        element = WebDriverWait(
            self.driver, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
        )
        assert element.text == 'RA1modnew'
        article_content = self.driver.find_element_by_class_name('article-content')
        assert article_content.find_element_by_xpath('//p').text == text2

    # TEST6 (DELETE ARTICLE)
    def test_delete_article(self):
        self.driver.maximize_window()
        self.login()
        random_nr = int(time.time())
        random_title = 'RA1mod' + str(random_nr)
        self.new_article(random_title, 'RA1', text, 'exammod')
        time.sleep(2)
        self.driver.find_element_by_xpath('//button[@class="btn btn-outline-danger btn-sm"]').click()
        time.sleep(3)
        try:
            WebDriverWait(
                self.driver, 5).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, random_title))
            )
            not_found = False
        except:
            not_found = True

        assert not_found

    # TEST11 (LOG OUT)
    def test_logout(self):
        self.driver.maximize_window()
        self.login()
        time.sleep(2)
        self.driver.find_element_by_partial_link_text('Log out').click()

        try:
            WebDriverWait(
                self.driver, 5).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Log out'))
            )
            not_found = False
        except:
            not_found = True

        assert not_found

    # TEST7 (Repeated and sequential data entry from CSV file)
    def test_rsd_entry_from_file(self):
        self.driver.maximize_window()
        self.login()
        time.sleep(2)
        with open('./test_conduit/articles.csv', 'r') as kulcs:
            csv_reader = csv.reader(kulcs, delimiter=';')
            next(csv_reader)
            for formdata in csv_reader:
                # print(formdata)
                self.new_article(formdata[0], formdata[1], formdata[2], formdata[3])
                element = WebDriverWait(
                    self.driver, 5).until(
                    EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
                )
                assert element.text == formdata[0]
                article_content = self.driver.find_element_by_class_name('article-content')
                assert article_content.find_element_by_xpath('//p').text == formdata[2]
                comment = self.driver.find_element_by_xpath(
                    '//textarea[@placeholder="Write a comment..."]')
                comment.clear()
                comment.send_keys(formdata[4])
                self.driver.find_element_by_xpath('//button[@class="btn btn-sm btn-primary"]').click()
                time.sleep(2)
                comment_added = self.driver.find_element_by_css_selector('.card-text')
                assert comment_added.text == formdata[4]
                time.sleep(2)

    # TEST10 (Save data from web to file)
    def test_save_data_from_web_to_file(self):
        self.driver.maximize_window()
        self.login()
        time.sleep(2)
        posts = self.driver.find_elements_by_class_name('article-preview')
        with open('./test_conduit/web_data_save.txt', 'w') as web_save:
            for post in posts:
                post_title = post.find_element_by_tag_name('h1').text
                web_save.write(post_title)
                web_save.write('\n')

        with open('./test_conduit/web_data_save.txt', 'r') as web_saved:
            for post_title in web_saved:
                title = self.driver.find_elements_by_class_name('article-preview')[0].find_element_by_tag_name(
                    'h1').text
                assert post_title.strip() == title
                break

    # TEST9 (PAGINATION)
    def test_pagination(self):
        self.driver.maximize_window()
        self.login()
        time.sleep(2)
        posts = self.driver.find_elements_by_class_name('article-preview')
        first_post = posts[0].find_element_by_tag_name('h1').text
        pagination = self.driver.find_element_by_class_name('pagination')
        pages = pagination.find_elements_by_class_name('page-link')
        for index, page in enumerate(pages):
            if len(pages) <= index + 1:
                break
            else:
                pages[index + 1].click()

            time.sleep(2)
            posts_2 = self.driver.find_elements_by_class_name('article-preview')
            first_post_2 = posts_2[0].find_element_by_tag_name('h1').text
            assert first_post_2 != first_post
            first_post = first_post_2

    # TEST8 (DATA LISTING)
    def test_data_listing(self):
        self.driver.maximize_window()
        self.login()
        time.sleep(2)
        sidebar = self.driver.find_element_by_class_name('sidebar')
        popular_text = sidebar.find_elements_by_class_name('tag-pill')
        popular_text[0].click()
        time.sleep(2)
        page_elements = self.driver.find_elements_by_class_name('article-preview')
        for page in page_elements:
            article_tags = page.find_elements_by_css_selector('a.tag-list')
            for tag in article_tags:
                assert popular_text[0].text == tag.text
