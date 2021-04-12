# additional feature which will be used
for data in [train_df, test_df]:
    data["CREDIT_ANNUITY_RATIO"] = data["AMT_CREDIT"] / (
        data["AMT_ANNUITY"] + 0.00001
    )

# KNN classifier result as a feature (which has high correlation with target)
knn = KNeighborsClassifier(500, n_jobs=-1)
train_data_for_neighbors = train_df[
    ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3", "CREDIT_ANNUITY_RATIO"]
]
train_target = train_df.TARGET
test_data_for_neighbors = test_df[
    ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3", "CREDIT_ANNUITY_RATIO"]
]

knn.fit(train_data_for_neighbors, train_target)

train_500_neighbors = knn.kneighbors(train_data_for_neighbors)[1]
test_500_neighbors = knn.kneighbors(test_data_for_neighbors)[1]

train_df["TARGET_NEIGHBORS_500_MEAN"] = [
    train_df["TARGET"].iloc[ele].mean() for ele in train_500_neighbors
]
test_df["TARGET_NEIGHBORS_500_MEAN"] = [
    train_df["TARGET"].iloc[ele].mean() for ele in test_500_neighbors
]
