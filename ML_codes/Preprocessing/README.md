# what is the point of preprocessing?

when working with data and your data is dirty and not solid enough
it is like cooking a food with dirty and spoiled material the final 
result is not usable or even edible. So data preprocessing is a vital 
step in ML projects that is Done after EDA.

You can put your model in a more balanced, not white noise datasets

## there are Usual Problems in real world data.
- Imbalaced targets
- Missing values and Outliers
- Categorical Features
- Different Feature Scales

### what is Data Leakage?

when you are training a model and your test dataset is on the training dataset.
that cause not real high accuracy measures. with that problem we get high accuracy on our test, and 
poor accuracy on REAL WORLD data.

test data is locked in a Safe box with no way to get access to it and you can have it one time.
and after you used it you put it back into the safe box.

- the solution: 
you should always split your data first.
and it would NEVER learn from the test data.


