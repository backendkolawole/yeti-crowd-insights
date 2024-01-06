# Table of Contents 



# Business Process Flow
This diagram describes the business process flow of Yeti System.

``` flowchart TD

%% **************** Data Source definitions ****************
subgraph sources[Data Source Selection]
	video[/Video Feed/]
end 

%% **************** Data Ingestion ****************
subgraph ingest[Data Ingestion]
	extraction(Extract <br>raw data)
	rawStore[(Raw Store)]

	extraction --> rawStore
end

%% **************** Simple Data analytics process ****************
subgraph simpleAnalysis[Basic Analysis]
	analyseData(Simple Analysis)
	analyticalStore[(Analytical <br>Data Store)]
	showAnalytics>Show <br>Analytics]

	analyseData --> analyticalStore
	rawStore --> analyseData
	analyticalStore --> showAnalytics
end

sources ---> extraction

```
