# Kayak Airfare Scraping and Analysis

## Project Overview

This project involves scraping airfare data from Kayak using Selenium, followed by cleaning and analyzing the data to explore pricing trends.The scraper collects airfare information for various flight routes between Yerevan (EVN) and multiple cities in Saudi Arabia (SA) over different time frames (1 week, 2 weeks, 1 month) and across different months (November, January, February, etc.). The collected data includes flight prices, departure and arrival times, airlines, layovers, and more. The analysis helps users understand patterns in airfare based on factors like trip duration, destination, airline, time of booking and etc.

## Dataset

The dataset contains flight information scraped from Kayak, covering different flight durations (1 week, 2 weeks, 1 month) and various months. The key features of the dataset include:

* Carrier: Airline providing the service.
* Departure and Arrival: Departure and arrival locations.
* Flight Duration: Total travel time.
* Layovers: Layover information.
* Price: Airfare cost.

## Objectives

* Web Scraping: Automate the scraping of airfare data for multiple months and routes.
* Data Cleaning: Clean the scraped data by handling missing values, formatting times, and removing outliers.
* Exploratory Data Analysis (EDA): Visualize and analyze trends in airfare data to understand how prices vary by date, destination, and other factors.

## Questions to Explore:

1. Which routes are the most cost-effective?
Based on the average prices, the most affordable economy class round-trip ticket from Armenia to Saudi Arabia is from Yerevan to Medina, while the best-priced business class round-trip ticket is from Yerevan to Riyadh. Additionally, for travel to Armenia from Saudi Arabia, the cheapest round-trip tickets for both economy and business classes are from Dammam to Yerevan.
  ![image](https://github.com/user-attachments/assets/342b1f38-31b8-41a2-9248-bb3255891257)



  
2. Which routes have the shortest travel times?
Based on the previous and current visualizations, it can be concluded that for Armenia, the best route is Yerevan to Riyadh, while for Saudi Arabia, it is Dammam to Yerevan.
  ![image](https://github.com/user-attachments/assets/fb134788-97a4-431e-84ad-493fa283b8a4)



  
3. How do layovers impact overall travel time and price?
 
![image](https://github.com/user-attachments/assets/6f523703-34b0-4c73-8b22-af0cb49d8483)
![image](https://github.com/user-attachments/assets/0d6debcc-2497-45ed-861a-8f57aa81d994)

Based on this visualization, it can be concluded that economy class may have up to three layovers, while business class typically has only one layover. Additionally, for economy class, prices range from $300 to $1,800, while for business class, they start at $1,500 and can go up to $4,500, with most prices falling between $1,500 and $2,700


![image](https://github.com/user-attachments/assets/00dc7cae-1d02-4b3f-9eea-45e1b8d0b857)
![image](https://github.com/user-attachments/assets/63e6368b-8979-4990-a6e7-d98b58549dce)

For economy class, the duration of the trip can last up to 50 hours, while for business class, it typically lasts a maximum of 30 hours.


4. What are the price trends and seasonal changes for both directions?

![image](https://github.com/user-attachments/assets/520c6802-a1a3-4409-9066-d40a7e4960d2)
![image](https://github.com/user-attachments/assets/94b17ae2-de30-4db2-a45c-da04e1d93611)
![image](https://github.com/user-attachments/assets/0a51a694-fd11-4b0d-ab2f-1591f789f34d)

The cheapest tickets for both classes are available in the fall, although the prices in other seasons vary only slightly for each class.

![image](https://github.com/user-attachments/assets/e91526b3-4853-4d4a-9f90-00014f085fd8)

In October, the cheapest tickets for economy class are available. Since the lowest prices for business class are also in the fall, it can be assumed that October offers the cheapest tickets for business class as well.

![image](https://github.com/user-attachments/assets/61491f16-71d3-458b-a66a-59b451c9b917)
![image](https://github.com/user-attachments/assets/4c01aab9-2170-4967-b6e1-7df205aae748)


![image](https://github.com/user-attachments/assets/7f6d92a8-5475-4af8-a79a-fd2dcddb30eb)
![image](https://github.com/user-attachments/assets/bc723fdb-6391-4860-9972-36debf113316)


5. What are the most profitable airlines?

## Project Structure

### 1. Web Scraping

Using Selenium, the airfare data was scraped for different routes and durations across multiple months. Each request resulted in a JSON file containing flight details such as carrier, departure/arrival times, and price.

### 2. Data Cleaning

In the Cleaning and EDA notebook, the scraped data was processed and cleaned:

* Handling Missing Data: Missing values were removed or filled based on the dataset’s context.
* Formatting Dates: Departure and return dates were reformatted for consistency.
* Add new columns: Added new columns like Season,Total Stops and etc.

### 3. Exploratory Data Analysis (EDA)

The EDA focused on uncovering patterns in airfare prices:

* Price Trends by Month: Visualization of how airfare prices fluctuate month to month.
* Trip Duration vs Price: Analysis showing how the length of the trip affects the price.
* Top Destinations by Price: Ranking destinations based on average airfare costs.
* Airline Comparison: Comparison of average prices across different airlines.

### 4. Data Analysis and Insights

After cleaning the data, key insights were derived from the analysis:

* Optimal Booking Time: Identified the best time to book flights based on price trends.
* Price Fluctuations by Trip Duration: Found that longer trips tend to have higher airfare, but specific durations (e.g., 1-week trips) show more stable prices.
* Airline Performance: Certain airlines consistently offer cheaper flights for specific routes, providing cost-saving insights.

## Conclusion

This project automates the collection of airfare data from Kayak and provides valuable insights into pricing trends.
