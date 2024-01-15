# Table of Contents 
1. [Business Process Flow](#business-process-flow)
2. [System Context Diagram](#system-context-diagram)
3. [System Container Diagram](#system-container-diagram)


# Business Process Flow <a name="business-process-flow"></a>
This diagram describes the business process flow of Yeti System. It basically is showing the data flow among the major business processes.

```mermaid
flowchart TD

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
	analyzeData(Simple Analysis)
	analyticalStore[(Analytical <br>Data Store)]
	showAnalytics>Show <br>Analytics]

	analyzeData --> analyticalStore
	rawStore --> analyzeData
	analyticalStore --> showAnalytics
end

sources ---> extraction

``` 

# System Context Diagram <a name="system-context-diagram"></a>

This diagram depicts the major systems both external and internal Yeti system. 

<img src="./diagrams/out/Yeti-System-Context-Diagram.svg"> 



# System Container Diagram <a name="system-container-diagram"></a>
Following are the independent deployable units or containers which are required to create a fully functional system.

<img src="./diagrams/out/Yeti-System-Container-Diagram.svg">

