from bs4 import BeautifulSoup
import requests

# List of user agents for rotating
user_agent_list = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:64.0) Gecko/20100101 Firefox/64.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:65.0) Gecko/20100101 Firefox/65.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:66.0) Gecko/20100101 Firefox/66.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:67.0) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:68.0) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:64.0) Gecko/20100101 Firefox/64.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:65.0) Gecko/20100101 Firefox/65.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:66.0) Gecko/20100101 Firefox/66.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:67.0) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:68.0) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:64.0) Gecko/20100101 Firefox/64.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:66.0) Gecko/20100101 Firefox/66.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:67.0) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:68.0) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:64.0) Gecko/20100101 Firefox/64.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:65.0) Gecko/20100101 Firefox/65.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:66.0) Gecko/20100101 Firefox/66.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:67.0) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:68.0) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.18 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko) Version/8.0.8 Safari/600.8.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.18 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.8 (KHTML, like Gecko) Version/9.1.3 Safari/601.7.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.18 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.18 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.18262','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.27 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36','Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36','Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36','Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36','Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.27 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.18 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (Windows NT 6.2; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.18 Safari/537.36','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:65.0) Gecko/20100101 Firefox/65.0','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (Windows NT 6.3; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/44.1.54 like Chrome/44.0.2403.63 Safari/537.36']

# Method to make request to a url
def make_request(url):
    response = requests.get(url='https://proxy.scrapeops.io/v1/', params={'api_key': '6231c4e8-779f-44f3-ba7e-ec30f3121f2f', 'url': url}, timeout=20)
    return response

# Method for crawl process
def crawl_process(keyword):
    url = 'https://www.amazon.in/s?k=' + str(keyword).strip()
    retry_count = 0 # initial retry count is set to 0
    retry_limit = 1 # max retry limit
    while retry_count < retry_limit:
        response = make_request(url)
        # check for successful requests
        if response.status_code == 200:
            # parsing raw html str into html dom
            parsed_html = BeautifulSoup(response.text, features='html.parser')
            # looking for brand filter node
            if parsed_html.select('#brandsRefinements'):
                brand_filter = parsed_html.select_one('#brandsRefinements')
                brand_dict = {}
                brand_str = ''
                # iterating brand values
                for brand_iter in brand_filter.select('span.a-list-item'):
                    brand_name = brand_iter.text.strip()
                    brand_url = 'https://www.amazon.in' + brand_iter.select_one('a').get('href').strip()
                    if str(brand_name).strip() != '' and brand_name != None and str(brand_url).strip() != '' and brand_url != None and 'see more' not in str(brand_name).lower().strip():
                        brand_str += brand_name + ', '
                        brand_dict[str(brand_name).lower().strip()] = str(brand_url).strip()
                # make sure brand availability
                if str(brand_str).strip() != '':
                    brand_str = brand_str[:-2].strip()
                    print("Available Brands: ", brand_str)
                    user_brand_check = 0
                    while True:
                        # prompt user to get a brand name
                        user_brand = input("Enter a Brand: ")
                        if str(user_brand).lower().strip() in str(brand_str).lower().strip().split(', '):
                            brand_select_url = brand_dict[str(user_brand).lower().strip()]
                            # hitting user selected brand url for products
                            brand_response = make_request(brand_select_url)
                            if brand_response.status_code == 200:
                                user_brand_check = 1
                                # parsing brand response
                                brand_soup = BeautifulSoup(brand_response.text.strip(), features='html.parser')
                                result_list = []
                                # iterating all products for a listing page
                                for asin_id in brand_soup.select('.s-result-item'):
                                    result_dict = {}
                                    if asin_id.get('data-asin'):
                                        # extracting product title, link and price information
                                        pdp_name = asin_id.select_one('.a-link-normal.a-text-normal').select_one('span').text.strip()
                                        product_url = 'https://www.amazon.in' + asin_id.select_one('.a-link-normal.a-text-normal').get('href')
                                        regular_price = markdown_price = 'n/a'
                                        # excluding non-product sku
                                        if "slredirect/picassoRedirect" not in product_url and "gp/video/ssoredirect" not in product_url and "cv_ct_cx=" not in product_url:
                                            try:
                                                markdown_price = str(asin_id.select('.a-offscreen')[0].text.strip())
                                                try:
                                                    regular_price = str(asin_id.select('.a-offscreen')[1].text.strip())
                                                except:
                                                    regular_price = "n/a"
                                            except:
                                                try:
                                                    markdown_price = str(asin_id.select('.a-color-price')[0].text.strip())
                                                except:
                                                    markdown_price = "n/a"
                                                regular_price = markdown_price
                                            try:
                                                if regular_price == 'n/a' and markdown_price != 'n/a':
                                                    regular_price = markdown_price
                                                if regular_price != 'n/a' and markdown_price == 'n/a':
                                                    markdown_price = regular_price
                                            except:
                                                pass
                                        # copying all extracted attributes to list
                                        result_dict['keyword'] = str(keyword).strip()
                                        result_dict['brand'] = user_brand
                                        result_dict['product_name'] = pdp_name
                                        result_dict['product_url'] = product_url
                                        result_dict['regular_price'] = regular_price
                                        result_dict['markdown_price'] = markdown_price
                                        result_list.append(result_dict)
                                print(result_list, "\n")
                            else:
                                print("Brand request is failed")
                            break
                        else:
                            print("Invalid Brand.")
                            continue
                    if user_brand_check == 0:
                        print("Unable to retrieve brand filter")
                else:
                    print("No Brand Filter available")
            elif 'No results for ' in str(parsed_html).strip():
                print("No results for ", keyword)
            else:
                print("No Brand Filter available")
            retry_count = retry_limit
        # printing non-200 response code
        else:
            print("Status code:", response.status_code)
        retry_count += 1


# keywords = ['ball']
# getting list of keywords from the user
keywords = input('Enter the Keywords(comma separated): ').split(',')
# iterating keywords one by one
for keyword in keywords:
    # make sure entered keywords is proper
    if keyword.isalnum():
        print("Keyword crawling.. ", keyword.strip())
        crawl_process(keyword)
    # printing invalid keywords
    else:
        print("Invalid keyword, ", keyword)
