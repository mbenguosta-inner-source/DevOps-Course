Choose one of the following projects:

# PROJECT 1 : 

## Use gitlab CI or github action to build and deploy  a nodejs or python app in a cloud PAAS service

### Options 1: (when you have cloud access) <br>
1-  Build the container image<br>
2-  Host it to dockerHub<br>
3- deploy in a cloud serverless container service ( Azure Container App or ECS or Google Cloud Run)<br>

Note: Do it in 2 or 3 separated jobs.<br><br><br><br>


### Option 2:<br><br>
1- Scan your app with trivy and save artifacts <br>
2- Build your app (without docker)<br>
3- Deploy it to Heroku<br>

Note: Do it in 2 or 3 separated jobs.<br><br><br><br>


# PROJECT 2 : 

### Options 1: (when you have cloud access) <br>

Use terraform to deploy cloud infrastructure

1- create vpc network and  subnet<br>
2- Deploy an ubuntu vm instance with nginx pre-installed<br>
3- Create a gitlab-ci or github action cicd pipeline to build and deploy <br>


### Option 2:<br><br>

Create a terraform module ``` kub-module ``` to deploy kubernetes cluster in azure or GCP or AWS <br>

The module should contains ``` variables.tf ```, ``` main.tf ``` and ``` output.tf ``` <br>

In the ``` output.tf ``` retrieve cluster name and id <br>

Add a ``` clusters.tf ``` file in the root directory and add  two ``` kub-module ``` implementations to create ``` cluster1 ``` and ``` cluster2 ```<br><br><br>

You can use terratest to test your modules


## Submit your job with the following gForm <br>
https://forms.gle/o11NQe99WTajXZoj9
