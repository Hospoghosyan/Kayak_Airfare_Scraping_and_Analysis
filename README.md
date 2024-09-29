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

![image](https://github.com/user-attachments/assets/342b1f38-31b8-41a2-9248-bb3255891257)
Based on the average prices, the most affordable economy class round-trip ticket from Armenia to Saudi Arabia is from Yerevan to Medina, while the best-priced business class round-trip ticket is from Yerevan to Riyadh. Additionally, for travel to Armenia from Saudi Arabia, the cheapest round-trip tickets for both economy and business classes are from Dammam to Yerevan.

2. Which routes have the shortest travel times?

![image](https://github.com/user-attachments/assets/9fe51e60-e16c-4c8a-a806-218c0cd30ac7)
Based on the previous and current visualizations, it can be concluded that for Armenia, the best route is Yerevan to Riyadh, while for Saudi Arabia, it is Dammam to Yerevan.

3. How do layovers impact overall travel time and price?
![image](https://github.com/user-attachments/assets/e44dd20b-3d5b-4460-bad4-7a68249cc978)
![image](https://github.com/user-attachments/assets/85a3a461-f68d-4789-9c77-b67cf744e5f3)
Based on this visualization, it can be concluded that economy class may have up to three layovers, while business class typically has only one layover. Additionally, for economy class, prices range from $300 to $1,800, while for business class, they start at $1,500 and can go up to $4,500, with most prices falling between $1,500 and $2,700

![image](https://github.com/user-attachments/assets/ed397ea5-2ba7-48c6-899f-c2eb65bed00c)
![image](https://github.com/user-attachments/assets/07ced2b4-feb0-4b56-93d0-2b390947c4b0)
For economy class, the duration of the trip can last up to 50 hours, while for business class, it typically lasts a maximum of 30 hours.

5. What are the price trends and seasonal changes for both directions?

6. What are the most profitable airlines?

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
