from darts.utils.utils import SeasonalityMode, TrendMode, ModelMode

arima = {
    'order':[(2,0,0),(0,0,2),(1,0,1)],
    'seasonal_order':[(0,1,1,12),(2,1,0,12),(1,0,1,12)],
    'Xvars':['all',None],
}

elasticnet = {
    'alpha':[i/10 for i in range(1,21)],
    'l1_ratio':[0,0.25,0.5,0.75,1],
    'normalizer':['scale','minmax'],
}

gbt = {
    'max_depth':[2,3],
    'max_features':['sqrt',None],
}

hwes = {
    'trend':['add',None],
    'seasonal':['add'],
}

knn = {
    'n_neighbors':range(2,101),
}

lightgbm = {
    'n_estimators':[150,200,250],
    'boosting_type':['gbdt','dart','goss'],
    'max_depth':[1,2,3],
    'learning_rate':[0.001,0.01,0.1],
}

lasso = {
    'alpha':[i/100 for i in range(1,101)],
}

mlp = {
    'activation':['relu','tanh'],
    'hidden_layer_sizes':[(25,),(25,25,)],
    'solver':['lbfgs','adam'],
    'normalizer':['minmax','scale'],
}

mlr = {
    'normalizer':['scale','minmax',None],
}

prophet = {
    'n_changepoints':range(5),
    'Xvars':['all',None],
}

rf = {
    'max_depth':[2,5],
    'n_estimators':[100,500],
    'max_features':['auto','sqrt'],
    'max_samples':[.75,.9,1],
}

ridge = {
    'alpha':[i/100 for i in range(1,101)],
}

silverkite = {
    'changepoints':range(5),
    'Xvars':['all',None],
}

sgd={
    'penalty':['l2','l1','elasticnet'],
    'l1_ratio':[0,0.15,0.5,0.85,1],
    'learning_rate':['invscaling','constant','optimal','adaptive'],
}

svr={
    'kernel':['linear'],
    'C':[.5,1,2,3],
    'epsilon':[0.01,0.1,0.5],
}

theta = {
    'theta':[0.5,1,1.5,2,2.5,3],
    'model_mode':[
        ModelMode.ADDITIVE,
    ],
    'season_mode':[
        SeasonalityMode.ADDITIVE,
    ],
    'trend_mode':[
        TrendMode.EXPONENTIAL,
        TrendMode.LINEAR
    ],
}

xgboost = {
     'n_estimators':[150,200,250],
     'scale_pos_weight':[5,10],
     'learning_rate':[0.1,0.2],
     'gamma':[0,3,5],
     'subsample':[0.8,0.9],
}
