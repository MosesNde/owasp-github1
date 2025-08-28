 jupyter_deps = ['jupyterlab', 'jupyterhub', 'notebook', 'nbclassic']
 mlflow_deps = ['mlflow-skinny>=1.2']
 tf_deps = ['tensorflow>2']
dev_deps = ['pytest', 'twine', 'flake8', 'mock', 'behave', 'splinter[selenium]', 'ipdb', 'bumpversion']
 backtracking_deps = [
     'json5>0.9',  # nobody knows
     'google_auth_oauthlib>=1',  # nobody knows
         'marshmallow>=3.17.0',  # required for openapi generation
         'sqlalchemy<2',  # currently no support for sqlalchemy 2
         'minibatch[all]',  # required for streaming
     ],
     extras_require={
         'all': test_deps,