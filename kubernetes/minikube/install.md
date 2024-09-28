# Minikube installation (ubuntu server)
## Install the container runtime, Docker in this case:
```sh
sudo apt install -y docker.io
```
## Install Minikube
Retrieve and then install the Minikube deb package:
```sh
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_1.4.0.deb
sudo dpkg -i minikube_1.4.0.deb
```
Once this is installed, set the default driver to none:
```sh
sudo minikube config set vm-driver none
```

Now start Minikube
```sh
minikube start --driver=docker
minikube start --driver=docker  --cpus=4 --memory=8192
```
Enable Users to Manage Environments
For the developers to manage their own environments, they need to own certain directories. Let's give them ownership with this:
```sh
sudo chown -R $USER $HOME/.kube $HOME/.minikube
```

## Install kubectl
In order to create a deployment we will need to install kubectl:
```sh
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
```
Now we'll have a kubectl file sitting in our directory (ls will show it) that we have to execute. <br>
Make it executable first, then move it to one of the directories where other executables are stored (/usr/local/bin in this case):
```sh
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```
Now we want to make sure that we can see our Minikube setup and our Kubernetes cluster using kubectl:
```sh
kubectl get po -A
```
## Create and Expose a Deployment
Create a deployment, in this case Nginx:
```sh
kubectl create deployment --image nginx my-nginx
```
To access the deployment we will need to expose it:
```sh
kubectl expose deployment my-nginx --port=80 --type=NodePort
```
Once this is done, we need to determine where to access the Nginx default page:
```sh
minikube service list
```

Once we have the output of this command, we'll aim a curl command at the Nginx service on the service IP and port that the service has mapped to. Look for the row in the output of that last command that has our my-nginx as a NAME. <br>
There's a local IP and port in the TARGET PORT column. <br>
Our next command will look something like this:
```sh
curl http://<LOCAL_IP>:<PORT>
```
Open it in your default browser
```sh
minikube service nginx
```
## (Optional) Expose nginx server as defaut localhost app
Install Nginx
In order to expose our application, we've got to install a proxy first:
```sh
sudo apt install -y nginx
```

Edit the Default Site
```sh
sudo vim /etc/nginx/sites-enabled/default
```

We're going to change the line that reads:
```sh
try_files $uri $uri/ =404;
```
so that it instead reads something like:
```sh
proxy_pass http://<LOCAL_IP>:<PORT>;
```

This is going to be right around line 50 in the file, and note that this http address and port we've added are what we got from the minikube command we ran a little bit ago. Now we can save the file, then make Nginx read the config again with:
```sh
sudo systemctl restart nginx
```
Test in a Browser



