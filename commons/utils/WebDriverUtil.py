from selenium import webdriver


def create_chrom(chrome_path):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_extension(chrome_path)
    # 禁用 Chrome 启动时的某些行为，例如弹出警告、自动打开调试器等
    # chrome_options.add_argument('--disable-extensions')
    # chrome_options.add_argument('--disable-infobars')
    # chrome_options.add_argument('--disable-popup-blocking')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--disable-gpu')
    return webdriver.Chrome()
