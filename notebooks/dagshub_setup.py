import dagshub
import mlflow

mlflow.set_tracking_uri('https://dagshub.com/ShashiDivs/mlops-project-mlflow.mlflow')
dagshub.init(repo_owner='ShashiDivs', repo_name='mlops-project-mlflow', mlflow=True)


with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)