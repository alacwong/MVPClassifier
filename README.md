# MVPClassifier
Use a simple perceptron neural network to predict NBA mvps with tournament algorithm

### Classifier performance
<img src="./assets/error%20plot.png"/>

This plot shows classifier performance over 300 epochs. The error value is calculated from the least squares
method between the normalized mvp shares between 2 players. However classifying mvp share is very difficult given player stats
as other factors such as narrative apply. However with the given data and features, this classifier should be able to predict which player is better.
The following plot shows the performance given the task of classifying the better player.