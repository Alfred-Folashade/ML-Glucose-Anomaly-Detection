# ML-Glucose-Anomaly-Detection
Core Idea: A system that reads glucose levels over time and warns if something looks wrong.
To achieve this I will use an an unsupervised Ml technique called Isolation forest

My understanding of Isolation Forest Algorithm:
Anomolous data in a dataset is easier to separate than normal data, so the algorithm isolates the data points with a few random cuts with the expectation that the anomalies will take fewer cuts than the normal ones.

So to do this it first builds a tree (it will actually build a tree many times) it picks a random feature then for that feautre picks a random valid split value (literally just a random value within that column of data). Using this split value it splits the data into less than to left and greater than or equal to on right of tree. 

You typically build 100–300 trees (n_estimators), each on a random subsample of your data.  Each tree gives a path length for every point, you average them, then normalize to get a final score between 0 and 1 where 1 would be anomaly and 0.5 normal. Also path length here corresponds to number of cuts 
https://www.google.com/url?sa=t&source=web&rct=j&url=https%3A%2F%2Ftowardsdatascience.com%2Fhow-to-perform-anomaly-detection-with-the-isolation-forest-algorithm-e8c8372520bc%2F&ved=0CBYQjRxqFwoTCPCb0dXLr5MDFQAAAAAdAAAAABAI&opi=89978449<img width="1516" height="678" alt="image" src="https://github.com/user-attachments/assets/ca9f8cb9-4903-40ed-9cd5-1975d6a62348" />
