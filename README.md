# LEGO Sets Resale Price Trend
Highlighting trends and identify investment opportunities within the LEGO set market

## Getting Started: 
1. Report and presentation
2. data/: Contains cleaned datasets used for the analysis
3. notebooks/: Jupyter notebooks
4. visualizations/: Tableau visualizations and dashboard
5. scripts/: Python and SQL scripts for data analysis

### Tools:
Excel, Jupyter, Python, SQL, Tableau

### Data Sources:
This dataset uses a combination of data from two API's from Brickset.com and Bricklink.com.

The analysis will be based on the cleaned dataset, which includes the following fields:
* Set_ID
* Name
* Year: year of release
* Theme
* Theme_Group
* Subtheme
* Category
* Packaging: packaging type
* Availability: retail availability
* Pieces: number of pieces
* Minifigures: number of minifigures
* Owned
* Rating: user reviews (out of 5 stars)
* Price: list price in USD
* Resale_Price: latest resale price in USD

## Problem Definition
As LEGO sets increasingly become sought-after collectibles and investments, there is a growing interest in identifying sets or themes that have shown consistent appreciation in resale prices. Moreover, investors seek to understand the underlying patterns and characteristics that contribute to the value appreciation of certain sets, enabling them to make informed decisions when allocating their investment capital.

## Hypothesis
The resale price of a LEGO set can be accurately predicted based on its features such as theme, number of pieces, year of release, and number of minifigures.

## Vision
To provide LEGO investors and collectors with data-driven insights that help identify high-potential sets and make informed investment decisions. By leveraging historical data and predictive modeling, this report aims to demystify the LEGO investment market and highlight opportunities for maximizing returns.

## Objective
* Analyze how resale prices of LEGO sets or pieces change over different periods
* Determine how resale prices are distributed across different themes of LEGO sets or pieces.
* Focus on the top 5 most popular or highest-selling themes and analyze the distribution of resale prices within each.
* Drill down into the top 5 subthemes within each main theme and analyze the distribution of resale prices within those subthemes.
* Investigate if there is any relationship (positive, negative, or none) between the characteristics or attributes of LEGO pieces (such as size, rarity, minifigure inclusion, etc.) and their resale prices.

## Key Insights
* The **Simpsons** theme has the highest median resale price, with sets released between 2014 and 2015.
* The **Advanced Models** theme demonstrates a consistent trend in resale prices from 2003 to 2012.
* The year **1986** stands out with the highest resale prices, showcasing a range of high resale prices from 1985 to 1995.
* The **Star Wars** theme holds the highest maximum resale price and has the most data points, with sets released from 1999 to 2023.
* The main theme groups are **Licensed** and **Model Making**.

### Dashboard
![image](https://github.com/acsoteldo/LEGO-Sets-Resale-Price-Trend/assets/76544489/19f708b0-cd88-4e2d-98ee-0027f3b88b99)

## Next Steps
* Access to additional datasets or APIs that provide up-to-date information on LEGO set sales, trends, and market dynamics.
* Form partnerships with LEGO retailers, online marketplaces, and investment firms to enhance data access and validation.
* Conduct webinars or workshops with LEGO collectors and investors to validate findings and gather qualitative insights.

## Contact
For any inquiries or feedback, please contact acsoteldo01@gmail.com.
