## Experiments log
- 01/06 [Giacomo] HashingVectorizer tried instead of TF-IDF, not better
- 04/06 [Giacomo] Random Forest classifiers investigated, bad performances that might be explained by the sparsity of the data
- 05/06 [Giacomo] t-NSE + PCA to plot feature space
- 06/06 [Giacomo] Experimented with standard machine learning approaches on character n-grams TF-IDF, ensemble of character and word level classifiers, none of which outperformed logistic regression over word-level TF-IDF
- 06/06 [Giacomo] Tried to reduce the dimensionality of the feature vectors with PCA (to 500 and 1000 dimensions), achieved very bad results
- 20/06 [Giacomo] In the last few days, many experiments were performed. Tried to add IT Wikipedia dumps to TF-IDF to reduce the weights of Italian words, not very effective in practice. Added explainability section for logistic regressor. Tried to drop confounding features from the training set but performances dropped. 
- 26/06 [Giacomo] Tried to group all sentences of the same dialect in a single file, no differences in the performance of the model. Added class weights to logistic regression, good increase in the performance of the model. There is still a trade-off between two pairs of dialects (VEC-LMO and SC-SCN) but seems to asymmetric. Class weights were obtained using k-fold cross validation. 


## Models log
| Model                 | Parameters                       | Validation F1 micro |
|:---------------------:|:--------------------------------:|:-------------------:|
| Logistic Regression   | `default`                        |0.8957               |
| Logistic Regression   | `sag_solver`                     |0.9295               |
| Logistic Regression   | `sag_solver`, `class_weights`    |0.9445               |