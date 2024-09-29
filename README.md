# Kayak Airfare Scraping and Analysis

## Project Overview

This project involves scraping airfare data from Kayak using Selenium, followed by cleaning and analyzing the data to explore pricing trends. The analysis helps users understand patterns in airfare based on factors like trip duration, destination, airline, and time of booking.

## Dataset

The dataset contains flight information scraped from Kayak, covering different flight durations (1 week, 2 weeks, 1 month) and various months. The key features of the dataset include:

* Carrier: Airline providing the service.
* Departure and Arrival: Departure and arrival locations.
* Flight Duration: Total travel time.
* Layovers: Layover information.
* Price: Airfare cost.

## Objectives

 • Web Scraping: Automate the scraping of airfare data for multiple months and routes.
 • Data Cleaning: Clean the scraped data by handling missing values, formatting times, and removing outliers.
 • Exploratory Data Analysis (EDA): Visualize and analyze trends in airfare data to understand how prices vary by date, destination, and other factors.## Questions to Explore:

## Questions to Explore:

1. Which routes are the most cost-effective?

2. Which routes have the shortest travel times?

3. How do layovers impact overall travel time and price?

4.What are the price trends and seasonal changes for both directions?

5.What are the most profitable airlines?

## Project Structure

### 1. Web Scraping

Using Selenium, the airfare data was scraped for different routes and durations across multiple months. Each request resulted in a JSON file containing flight details such as carrier, departure/arrival times, and price.

### 2. Data Cleaning

In the Cleaning and EDA notebook, the scraped data was processed and cleaned:

 • Handling Missing Data: Missing values were removed or filled based on the dataset’s context.
 • Formatting Dates: Departure and return dates were reformatted for consistency.
 • Add new columns: Added new columns like Season,Total Stops and etc.

## 3. Exploratory Data Analysis (EDA)

The EDA focused on uncovering patterns in airfare prices:

 • Price Trends by Month: Visualization of how airfare prices fluctuate month to month.
 • Trip Duration vs Price: Analysis showing how the length of the trip affects the price.
 • Top Destinations by Price: Ranking destinations based on average airfare costs.
 • Airline Comparison: Comparison of average prices across different airlines.

## 4. Data Analysis and Insights

After cleaning the data, key insights were derived from the analysis:

 • Optimal Booking Time: Identified the best time to book flights based on price trends.
 • Price Fluctuations by Trip Duration: Found that longer trips tend to have higher airfare, but specific durations (e.g., 1-week trips) show more stable prices.
 • Airline Performance: Certain airlines consistently offer cheaper flights for specific routes, providing cost-saving insights.

## Conclusion

This project automates the collection of airfare data from Kayak and provides valuable insights into pricing trends.
