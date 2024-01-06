# Table of Contents 
1. [Business Process Flow](#business-process-flow)
2. [System Container Diagram](#system-container-diagram)


# Business Process Flow <a name="business-process-flow"></a>
This diagram describes the business process flow of Yeti System.

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


# System Container Diagram <a name="system-container-diagram"></a>
Following are the independent deployable units or containers which are required to create a fully functional system.

```mermaid
C4Container
title Yeti System container diagram

System_Boundary(sources, "Video Feeds") {
	Container_Ext(feed1, "Video Camera", "support RTSP protocol", "A fixed video camera mounted at client's site")
}

System_Boundary(yetiSystem,"Yeti System") {
	Container(videoParsingApp,"Video Parsing App", "python/yolo8/roboflow lib","A python application which <br>uses Yolo8 and Roboflow libraries <br>to get people, count, tracking <br>and detection information from <br>the camera feed")
	ContainerDb(analyticsStore, "Analytics Storage", "PostgreSql", "Store analytics from parsed feed")

	Container(googleSheets, "Google Sheets View", "google sheets", "Google sheet connector and <br>views to fetch and show analytics data")

	Rel(feed1, videoParsingApp, "RTSP/Https")
	Rel(videoParsingApp, analyticsStore, "ODBC??")
	Rel(analyticsStore, googleSheets, "https??")
}

```

