# blockgroupspending
---
## Opportunity
---
US Consumers express their behavior in a number of ways, but critically in their spending decisions. The US Bureau of Labor Statistics is charged with publishing spending activity and provides its Consumer Expenditure Survey (CEX) annually with US totals, with selected states (40) and cities (23). 

Limited to aggregates, the survey only needs 10s of thousands of observations in the original collection. While this is sufficient for macroeconomic use, the volume gives a weak basis for estimating lower levels of geography. In addition, the CEX includes demographic measurements that are similar, but not directly related, to Census variables.  So, the CEX does not integtate well with the American Commuity Survey or other Census publications.

This ***blockgroupspending*** publication by Open Environments attempts to address this problem by using the BLS' Public Microdata (PUMD) sample to allocate CEX spending categories across 220,000 US Census block group geographies. For each block group, the effort applies two models to estimate:
* total consumer spending (regression)
* distribution of spending across spending categories (penetration) including Food, Transportation, Housing and Health costs.

Ultimately, these project spending on block groups that can be joined to US Census publications for additional demographics.

Understanding the results requires awareness of the BLS' CEX data structures. This is available in the markdown file named oe_bls_cex_EDA.md

The publication is made together with the source python code and notebooks used for repeatability. The materials are maintained under version control at https://github.com/OpenEnvironments/blockgroupspending. All feedback and development requests are welcome.

## Model details
--
The CEX publication includes many files reflecting 
* detailed 'diary' surveys capturing spend on thousands of items every two weeks
* family 'interviews' collecting household spending over the previous 3 months

The models are trained upon the latter, 'FMLI' files. The regression model uses extreme gradient boosting, or XGBoost methods that apply many decision trees to iteratively correct prediction error.  The subcategory models also use tree based methods, trained upon a the family interview details. The spending variables are named, following the BLS' CEX convention:
|Variable|Definition|2023|pct| 
|---|---|---|---|
|TOTEXP|Average annual expenditures|77280||
|FOOD|Food|9985|0.129|
|ALCBEV|Alcoholic beverages|637|0.008|
|HOUS|Housing|25436|0.329|
|APPAR|Apparel and services|2041|0.026|
|TRANS|Transportation|13174|0.17|
|HEALTH|Healthcare|6159|0.08|
|ENTERT|Entertainment|3635|0.047|
|PERSCA|Personal care products and services|950|0.012|
|READ|Reading|117|0.002|
|EDUCA|Education|1656|0.021|
|TOBACC|Tobacco products and smoking supplies|370|0.005|
|MISC|Miscellaneous|1184|0.015|
|CASHCO|Cash contributions|2378|0.031|
|RETPEN|Personal insurance and pensions|9556|0.124|

During the exploratory phase of this effort, ensemble modelling was evaluated finding that different groupings of income did not appreciably change model estimates while racial and ethnic categories did.  As a result, the models are case for major races (White, African American, Asian, Other) and Hispanic.

The ACS is collected by API at the block group level.  Block group geographies are the lowest level of Census ACS detail and consolidate into Census tracts which in turn consolidate into counties.

The FMLI responses are recorded in nominal dollars throughout the year, while total expenditure and ACS data represent year end states. As a result, the models' prediction for total expenditure is cast up using monthly inflation, weighted by monthly expenditure.

## Additional Caveats
It is import to note, analytically, that the results are a stretch for credibility.
* CEX Consumer Units (people sharing financial decisions) are not exactly Census households (people in a housing unit)
* CEX demographics are not exactly Census demographics, with the CEX imputing incomes differenly than the Census medians.
* The CEX applies population weightings to the microdata while the Census primarily aggregates from respondents.
* The CEX observations are from 1 household (race is a 0/1 indicator) while Census demographics are many households (races are proportions)
* Models are trained upon repeated measures from a Consumer unit but not revised for ANOVA.
* Several of the CEX subcategories are very small, as spending has changed over the years. Reading, Alcohol and Tobacco use are still top level subcategories, for example as those have declined significantly since the CEX was first designed. So, this model is limited to the major subcategories of food, housing, transportation, health and retirement spending.*
* The model apply machine learning to large datasets so significance is not a consideration. However, in practice, those very small subcategories should be avoided.
* Difference in spending across racial categories also have different magnitudes and varieties. As a result, the R squared metrics on each submodel vary from 25%-45%.
* I find 40% R square results to be significant as they predict human behaviors rather than more deterministic relationships.
  
The resulting dataset is available from the Open Environments at dataverse.harvard.edu. The supporting code is shared on  github.com/OpenEnvironments under MIT open source licensing. The final data files are:
* YYYYblockgroupspending.csv where YYYY is the four digit year
* Get_FMLI.ipynb to collect the files
* Get_ACS.ipynb uses the Census API to download select ACS variables at the block group level
* modelvars.csv configures the requested variables and the Census definition of each.
* blockgroupspending_regression.ipynb trains the regression model.
* blockgroupspending_prediction.ipynb uses the two models to predict total expenditure and it's subcategories in each blockgroup.

Other files are include for posterity, including functions to download and process other CEX PUMD data files.

All questions or feedback is most welcome by email at support@openenvironments.com

## Citations
U.S. Bureau of Labor Statistics. Consumer Expenditure Survey. Summary Tables. https://www.bls.gov/cex/tables/top-line-means.htm. 2023 

U.S. Bureau of Labor Statistics. Consumer Expenditure Survey. Public Use Microdata files. https://www.bls.gov/cex/pumd.htm

U.S. Census Bureau, “American Community Survey 5-Year Estimates: Comparison Profiles 5-Year,” 2022, <http://api.census.gov/data/2022/acs/acs5>

Python Package Index - PyPI. Python Software Foundation. "A simple wrapper for the United States Census Bureau’s API.". Retrieved from https://pypi.org/project/census/

The conda-forge Project: Community-based Software Distribution Built on the conda Package Format and Ecosystem. XGBoost. https://anaconda.org/conda-forge/xgboost

The conda-forge Project: Community-based Software Distribution Built on the conda Package Format and Ecosystem. Tensorflow. https://anaconda.org/conda-forge/tensorflow


## Controls
Pre-COVID estimates use means from 2020.

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-income-before-taxes-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-income-quintiles-before-taxes-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-income-deciles-before-taxes-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-region-1-year-average-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-population-area-size-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-area-type-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-composition-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-education-highest-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-housing-tenure-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-earners-2020.pdf

https://www.bls.gov/cex/tables/calendar-year/mean-item-share-average-standard-error/cu-size-2020.pdf