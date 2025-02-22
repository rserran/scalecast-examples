
elasticnet = {
    'alpha':[i/10 for i in range(1,21)],
    'l1_ratio':[0,0.25,0.5,0.75,1],
    'normalizer':['scale','minmax',None],
    'lags':[1,3,6],
}

gbt = {
    'max_depth':[2,3],
    'max_features':['sqrt',None],
    'lags':[1,3,6],
}

knn = {
    'n_neighbors':range(2,101),
    'lags':[1,3,6],
}

lasso = {
    'alpha':[i/100 for i in range(1,101)],
    'lags':[1,3,6],
}

lightgbm = {
    'n_estimators':[150,200,250],
    'boosting_type':['gbdt','dart'],
    'max_depth':[1,2,3],
    'learning_rate':[0.001,0.01],
    'lags':[1,3,6,12],
}

mlp = {
    'activation':['relu','tanh'],
    'hidden_layer_sizes':[(25,),(25,25,)],
    'solver':['lbfgs','adam'],
    'normalizer':['minmax','scale'],
    'lags':[1,3,6],
}

mlr = {
    'lags':[1,3,6,12],
}

rf = {
    'max_depth':[2,5],
    'n_estimators':[100,500],
    'max_features':['auto','sqrt'],
    'max_samples':[.75,.9,1],
    'lags':[1,3,6],
}

ridge = {
    'alpha':[i/100 for i in range(1,101)],
    'lags':[1,3,6],
}

sgd={
    'penalty':['l2','l1','elasticnet'],
    'l1_ratio':[0,0.15,0.5,0.85,1],
    'learning_rate':['invscaling','constant','optimal','adaptive'],
    'lags':[1,3,6,12],
}

svr={
    'kernel':['linear'],
    'C':[.5,1,2,3],
    'epsilon':[0.01,0.1,0.5],
    'lags':[1,3,6],
}

xgboost = {
    'n_estimators':[150,200,250],
    'scale_pos_weight':[5,10],
    'learning_rate':[0.1,0.2],
    'gamma':[0,3],
    'lags':[1,3,6,12],
}
