from selenium import webdriver


def create_chrom(chrome_path):
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_extension(chrome_path)
    # chrome_options.add_argument('--headless')  # 无头浏览器
    # chrome_options.add_argument('ignore-certificate-errors')  # 无视证书验证
    # chrome_options.add_argument('--start-maximized')  # 开始时直接最大屏幕
    return webdriver.Chrome(executable_path=chrome_path)
