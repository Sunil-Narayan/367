# Analyzing Optimal Economic Structures for Positive Health Outcomes in High GDP-Per-Capita Countries
### Sunil Narayan

### Background:
One of the most contentious topics in the US and around the world is how to provide healthcare to the people who need it. Countries tend to vary in what structure they choose for providing healthcare to their population. In particular, countries very along how much of their GDP they spend on Healthcare, and what percentage of that spending comes from the government versus private individuals. [Previous studies](https://link.springer.com/article/10.1007/s10198-005-0336-8) have found that increasing spending may improve outcomes for infants, but this advantage likely fades overtime. In this analysis, I want to measure the spending habits of countries with a high GDP-per-capita and see if there is a correlation between their Healthcare structures and their reletive probability of death as infants, children, and adults.

Finding the most efficent way to structure healthcare is an important challenge to everyone. All of our lives are contingent on our health, and providing for the health of its people is of critical importance to any modern government. Finding the most efficent way to spend money to increase positive health outcomes can yeild insight as to how each govenment can take on the challenge of maintaining the health of its population with limited resources. 

### Research Questions:
The research questions are the following:

- Question 1: What countries have a GDP-per-capita at or above the median?
- Question 2: How do different countries in this group approach healthcare spending?
- Question 3: How do different countries in this group differ in health outcomes?
- Question 4: Is there an optimal healthcare spending structure among this group to minimize cost and maximize outcomes?

Question 1 is to determine which countries I should include in this study. The reason I want to only study countries with a high GDP is because countries with lower GDPs tend to face catagorically different problems. A country with an annual GDP-per-capita in the hundreds will have to focus on providing more basic forms of care for their people, like running water and electricity. This is a different challenge than a country with an annual GDP-per-capita in the tens of thousands, which will focus more on optimizing and advancing medical technology. A country with a low GDP-per-capita may also be forced to spend a high portion of their GDP on healthcare due to high fixed costs relative to more developed economies. Because these challenges are so different, I believe that low GDP and high GDP countries warrent two different analyses, and in this analysis I have chosen to focus on finding an efficent way for high GDP-per-capita countries to spend their resources. 

Questions 2 and 3 will show how these countries approach healthcare and what the results of their strategies are. The data for question 2 will be be imported from the [WHO Data Tool](https://apps.who.int/nha/database/Select/Indicators/en). This will show which countries spend more or less on healthcare and whether that money tends to come from public or private sources. It also has several other data fields which may be helpful in determining the specifics of how each country approaches healthcare spending. Question 3 will be answered using data from [WHO Adult Mortality](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/adult-mortality-rate-(probability-of-dying-between-15-and-60-years-per-1000-population)), [UNICEF Child Mortality](https://data.unicef.org/resources/dataset/child-mortality/), and [World Bank Infant Mortality](https://data.worldbank.org/indicator/SP.DYN.IMRT.IN?end=1974&most_recent_year_desc=false&start=1974). These show the levels of infant, child, and adult mortality in the countries. 

Question 4 will use the results of questions 2 and 3 to attempt to make a prescriptive statement as to how a country with a developed economy should use its resources to emulate the most efficent healthcare systems. The goal will be to look for trends in spending patterns which corrilate with lower mortality rates. 

### Ethics:
There are several stakeholders in this problem. The people reciving the healthcare are concerned with the quality of the healthcare. This will cause them to gague possible solutions based on the quality of care that they provide. A different stakeholder is companies operating in the fields of biomedical technology, insurance, pharmecuticals, etc. They will likely want to maintain their level of revenue, and may not want solutions which shift spending to the public sector or decrease operating output. Other stakeholders include politicians, some of whom vehemently fight for or against changing the current healthcare systems of their respective countires, and would want to use the results of such an analysis to strengthen their rhetorical positions. 

It should be noted that healthcare outcomes are the products of complex sets of factors and drawing a 1-to-1 corrilation between spending and outcome is inherently oversimplifiying that complexity. Care must be taken not to extrapolate sweeping conclusions from this analysis for the purpose of changing policy without taking these other factors into account. [Policy can have a great impact](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.411.6359&rep=rep1&type=pdf) on health outcomes, and inaccurately assessing the efficency of healthcare systems could lead to countries making sub-optimal plans on how to improve their healthcare infrastructure. Making mistakes in such a field costs people their good health or even their lives, thus care must be taken to ensure that hte results accurately reflect the data.

### Data:

(Note that none of these are links to the files themselves, all of these pages contain links to the files. For the raw CSV/XLSXs themselves, check [the github](https://github.com/Sunil-Narayan/367/tree/main/Assignments/Final))

[World Bank GDP Per Capita](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD?most_recent_value_desc=true) 
This data will be imported as a csv to the project. It shows the current (non-PPP adjusted) GDP per capita for each country.

[WHO Data Tool](https://apps.who.int/nha/database/Select/Indicators/en)
This data will be imported as a XLSX. This shows the public and private spending on healthcare as a proportion of GDP. 

[WHO Adult Mortality](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/adult-mortality-rate-(probability-of-dying-between-15-and-60-years-per-1000-population))
This data will be imported as a csv. It shows the adult mortality rate of each country.

[World Bank Infant Mortality](https://data.worldbank.org/indicator/SP.DYN.IMRT.IN?end=1974&most_recent_year_desc=false&start=1974)
This data will be imported as a csv. It shows the infant mortality rate for each country.

[UNICEF Child Mortality](https://data.unicef.org/resources/dataset/child-mortality/)
This data will be imported as a csv. See the dataset labeled "Probability of dying among children aged 1-4."