import m2cgen as m2c

from sklearn.ensemble import *
from sklearn.linear_model import *
from sklearn.tree import *
from sklearn.svm import *


CLASSIFICATION_SUPPORTS = [
    LogisticRegression,
    LogisticRegressionCV,
    PassiveAggressiveClassifier,
    Perceptron,
    RidgeClassifier,
    RidgeClassifierCV,
    SGDClassifier,
    LinearSVC,
    NuSVC,
    OneClassSVM,
    SVC,
    DecisionTreeClassifier,
    ExtraTreeClassifier,
    ExtraTreesClassifier,
    RandomForestClassifier
]

REGRESSION_SUPPORTS = [
    ARDRegression,
    BayesianRidge,
    ElasticNet,
    ElasticNetCV,
    GammaRegressor,
    HuberRegressor,
    Lars,
    LarsCV,
    Lasso,
    LassoCV,
    LassoLars,
    LassoLarsCV,
    LassoLarsIC,
    LinearRegression,
    OrthogonalMatchingPursuit,
    OrthogonalMatchingPursuitCV,
    PassiveAggressiveRegressor,
    PoissonRegressor,
    RANSACRegressor,
    Ridge,
    RidgeCV,
    SGDRegressor,
    TheilSenRegressor,
    TweedieRegressor,
    LinearSVR,
    NuSVR,
    SVR,
    DecisionTreeRegressor,
    ExtraTreeRegressor,
    ExtraTreesRegressor,
    RandomForestRegressor
]

LANGUAGE_SUPPORTS = {
    "C": m2c.export_to_c,
    "C#": m2c.export_to_c_sharp,
    "Dart": m2c.export_to_dart,
    "F#": m2c.export_to_f_sharp,
    "Go": m2c.export_to_go,
    "Haskell": m2c.export_to_haskell,
    "Java": m2c.export_to_java,
    "JavaScript": m2c.export_to_javascript,
    "PHP": m2c.export_to_php,
    "PowerShell": m2c.export_to_powershell,
    "Python": m2c.export_to_python,
    "R": m2c.export_to_r,
    "Ruby": m2c.export_to_ruby,
    "Rust": m2c.export_to_rust,
    "VisualBasic": m2c.export_to_visual_basic,
    "Elixir": m2c.export_to_elixir,
}
