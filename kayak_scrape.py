from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import StaleElementReferenceException
import time
import random
import json

def scrape_page(driver,url):
    driver.get(url)
    time.sleep(random.uniform(50,60))
    count=1
    try:
        while len(driver.find_elements(By.XPATH, "//a[@class='moreButton']")) >0 :
            print("Show more link is available so Selenium bot will click on it.")
            WebDriverWait(driver, random.randint(40,50)).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='moreButton']"))).click()
            print('Clicked on show more link')
            time.sleep(random.uniform(1,2))
        else:
            print("Show more link is not available")
    except:
        print('Something else went wrong.')
        pass
    try:
        # Wait until the 'flight' elements are visible using XPath
        WebDriverWait(driver, random.uniform(45,60)).until(
            EC.visibility_of_element_located(
            (By.XPATH,
             ".//div[contains(@class, 'Base-Results-HorizonResult Flights-Results-FlightResultItem responsive phoenix-rising phoenix-rising')]"))
        )
        
        # Locate the <li> elements with class 'flight' using XPath
        flight_elements = driver.find_elements(By.XPATH,
                ".//div[contains(@class, 'Base-Results-HorizonResult Flights-Results-FlightResultItem responsive phoenix-rising phoenix-rising')]")
        print("Len of flights:", len(flight_elements))
        print("\n", "-"*80, "\n")
        # Loop through the flight elements and find carrier info
        for index in range(len(flight_elements)):
            try:
                # prices = driver.find_elements(By.XPATH, "//div[contains(@class, 'booking')]")[index]            
                flight0 = driver.find_elements(By.XPATH, "//li[@class = 'flight with-gutter']")[index]
                flight1 = driver.find_elements(By.XPATH, "//li[contains(@class, 'flight') and not(contains(@class, 'with-gutter'))]")[index]
                
                layovers0 = driver.find_elements(By.XPATH, "//div[contains(@id, 'info-leg-0') and contains(@class, 'Flights-Results-StopsPlot square')]")[index]
                layovers1 = driver.find_elements(By.XPATH, "//div[contains(@id, 'info-leg-1') and contains(@class, 'Flights-Results-StopsPlot square')]")[index]
                # print(f"Leyovers len: {len(layovers)}")
    
                
    
                carrier0 = flight0.find_element(By.XPATH, ".//div[contains(@class, 'col-field carrier')]").text
                carrier1 = flight1.find_element(By.XPATH, ".//div[contains(@class, 'col-field carrier')]").text
                
                duration0 = flight0.find_element(By.XPATH, ".//div[contains(@class, 'col-field duration')]").text
                duration1 = flight1.find_element(By.XPATH, ".//div[contains(@class, 'col-field duration')]").text
                
                departure0 = flight0.find_element(By.XPATH, ".//div[contains(@class, 'col-field time depart')]//div[@class='bottom']").text
                departure1 = flight1.find_element(By.XPATH, ".//div[contains(@class, 'col-field time depart')]//div[@class='bottom']").text
                
                arrival0 = flight0.find_element(By.XPATH, ".//div[contains(@class, 'col-field time return')]//div[@class='bottom']").text
                arrival1 = flight1.find_element(By.XPATH, ".//div[contains(@class, 'col-field time return')]//div[@class='bottom']").text
                
                departure_time0 = (
                        flight0.find_element(By.XPATH, ".//span[contains(@class, 'depart-time base-time')]").text +
                        " " +  # Add a space between the time and meridiem
                        flight0.find_element(By.XPATH, ".//span[contains(@class, 'time-meridiem meridiem')]").text
                        )
                departure_time1 = (
                        flight1.find_element(By.XPATH, ".//span[contains(@class, 'depart-time base-time')]").text +
                        " " +  # Add a space between the time and meridiem
                        flight1.find_element(By.XPATH, ".//span[contains(@class, 'time-meridiem meridiem')]").text
                        )
                
                arrival_time0 = (
                        flight0.find_element(By.XPATH, ".//span[contains(@class, 'arrival-time base-time')]").text +
                        " " +  # Add a space between the time and meridiem
                        flight0.find_element(By.XPATH, ".//div[contains(@class, 'col-field time return')]//span[contains(@class, 'time-meridiem meridiem')]").text
                        )
                arrival_time1 = (
                        flight1.find_element(By.XPATH, ".//span[contains(@class, 'arrival-time base-time')]").text +
                        " " +  # Add a space between the time and meridiem
                        flight1.find_element(By.XPATH, ".//div[contains(@class, 'col-field time return')]//span[contains(@class, 'time-meridiem meridiem')]").text
                        )
                
                # price = prices.find_element(By.XPATH, ".//span[contains(@class, 'price option-text')]//span[contains(@class, 'price-text')]").text 
                layover_elements0 = layovers0.find_elements(By.XPATH, ".//span[contains(@class, 'dot')]")
                layover_elements1 = layovers1.find_elements(By.XPATH, ".//span[contains(@class, 'dot')]")
                
                layover_titles0 = [element.get_attribute('title') for element in layover_elements0]
                layover_titles1 = [element.get_attribute('title') for element in layover_elements1]

                price_element = flight_elements[index].find_element(By.XPATH, ".//span[@class='price-text']")
                price = price_element.text.strip() 
    
                data["carrier"].append(carrier0)
                data["departure"].append(departure0)
                data["arrival"].append(arrival0)
                data["duration"].append(duration0)
                data["departure_time"].append(departure_time0)
                data["arrival_time"].append(arrival_time0)
                data["layover_titles"].append(layover_titles0)
                data["ret_carrier"].append(carrier1)
                data["ret_departure"].append(departure1)
                data["ret_arrival"].append(arrival1)
                data["ret_duration"].append(duration1)
                data["ret_departure_time"].append(departure_time1)
                data["ret_arrival_time"].append(arrival_time1)
                data["ret_layover_titles"].append(layover_titles1)
                data["price"].append(price)
             
                
                print("Scraped: ", count)
                count+=1
            except StaleElementReferenceException:
                print(f"Stale element error at flight index: {index}")
                continue  # Skip this element and move to the next one

    except Exception as e:
        print("TOTAL SCRAPED: ", count)
        print(f"An error occurred: {e}")
    print("TOTAL SCRAPED: ", count)


all_urls = {
    # November
    "Nov_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2024-11-08/2024-11-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Nov_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2024-11-08/2024-11-22?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Nov_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2024-11-02/2024-12-02?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    "Nov_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2024-11-08/2024-11-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Nov_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2024-11-02/2024-12-02?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Nov_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2024-11-08/2024-11-22?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",

    # Январь
    "Jan_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-01-05/2025-01-12?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jan_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-01-05/2025-01-19?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jan_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-01-05/2025-02-05?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Февраль
    "Feb_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-02-01/2025-02-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Feb_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-02-01/2025-02-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Feb_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-02-01/2025-03-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Март
    "Mar_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-03-01/2025-03-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Mar_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-03-01/2025-03-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Mar_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-03-01/2025-04-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Апрель
    "Apr_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-04-01/2025-04-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Apr_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-04-01/2025-04-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Apr_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-04-01/2025-05-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Май
    "May_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-05-01/2025-05-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "May_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-05-01/2025-05-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "May_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-05-01/2025-06-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Июнь
    "Jun_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-06-01/2025-06-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jun_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-06-01/2025-06-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jun_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-06-01/2025-07-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    # Июль
    "Jul_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-07-01/2025-07-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jul_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-07-01/2025-07-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jul_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-07-01/2025-08-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Август
    "Aug_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-08-01/2025-08-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Aug_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-08-01/2025-08-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Aug_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-08-01/2025-09-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Сентябрь
    "Sep_one_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-09-01/2025-09-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Sep_two_week_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-09-01/2025-09-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Sep_1_month_YVN_SA": "https://booking.kayak.com/flights/EVN-212cy/2025-08-25/2025-09-25?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",

    # Январь
    "Jan_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-01-05/2025-01-12?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jan_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-01-05/2025-01-19?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jan_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-01-05/2025-02-05?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Февраль
    "Feb_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-02-01/2025-02-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Feb_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-02-01/2025-02-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Feb_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-02-01/2025-03-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Март
    "Mar_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-03-01/2025-03-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Mar_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-03-01/2025-03-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Mar_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-03-01/2025-04-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Апрель
    "Apr_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-04-01/2025-04-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Apr_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-04-01/2025-04-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Apr_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-04-01/2025-05-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Май
    "May_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-05-01/2025-05-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "May_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-05-01/2025-05-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "May_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-05-01/2025-06-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Июнь
    "Jun_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-06-01/2025-06-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jun_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-06-01/2025-06-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jun_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-06-01/2025-07-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Июль
    "Jul_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-07-01/2025-07-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jul_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-07-01/2025-07-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Jul_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-07-01/2025-08-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Август
    "Aug_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-08-01/2025-08-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Aug_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-08-01/2025-08-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Aug_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-08-01/2025-09-01?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    
    # Сентябрь
    "Sep_one_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-09-01/2025-09-08?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Sep_two_week_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-09-01/2025-09-15?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
    "Sep_1_month_SA_YVN": "https://booking.kayak.com/flights/JED,RUH,DMM-EVN/2025-08-25/2025-09-25?sort=bestflight_a&fs=providers=QR,EK,ONLY_DIRECT,G9,PC,FZ,LH",
}

try:
    for key, url in all_urls.items():
        data = {
            "carrier": [],
            "departure": [],
            "arrival": [],
            "duration": [],
            "departure_time": [],
            "arrival_time": [],
            "layover_titles": [],
            "ret_carrier": [],
            "ret_departure": [],
            "ret_arrival": [],
            "ret_duration": [],
            "ret_departure_time": [],
            "ret_arrival_time": [],
            "ret_layover_titles": [],
            "price": []
            
        }
        # service=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome()

        scrape_page(driver, url)
        time.sleep(random.uniform(25,30))

        with open(f"{key}.json", "w") as outfile:
            json.dump(data, outfile, indent=4)
finally:
    driver.quit()