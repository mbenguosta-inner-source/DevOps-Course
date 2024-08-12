# Intall & configure Consul and Vault
## Download, Unpack, and Move Consul to the Bin Directory
  1	Download Consul:
  
  ```sh
  wget https://releases.hashicorp.com/consul/1.7.3/consul_1.7.3_linux_amd64.zip
  ```
  2	Install unzip:
  
  ```sh
  sudo apt install unzip
  ```
  3	Unpack Consul:
  ```sh
  unzip consul_1.7.3_linux_amd64.zip
  ```
  
  4	Move the consul installation executable to the bin directory:
  ```sh
  sudo mv consul /usr/bin
  ```
  5	Verify the installation was successful:
  ```sh
  consul
  ```


The output should list all of the available Consul commands.

## Create and Configure the Consul systemd Service


1	Get and copy the IP address of the server:
 ```sh
 ip addr show
```
 Note: You will use this IP address again when configuring Vault, so you may want to paste it into a file or keep it copied in your clipboard for easier access later on. 
2	Using vim, create a systemd service file:
 ```sh
sudo vim /etc/systemd/system/consul.service
```


3	In the file, paste in the following configuration, replacing IP.ADDRESS.OF.SERVER with the IP address you just obtained:
 ```sh
 [Unit] Description=Consul Documentation=https://www.consul.io/ [Service] ExecStart=/usr/bin/consul agent -server -ui -data-dir=/temp/consul -bootstrap-expect=1 -node=vault -bind=IP.ADDRESS.OF.SERVER -config-dir=/etc/consul.d/ ExecReload=/bin/kill -HUP $MAINPID LimitNOFILE=65536
 [Install] WantedBy=multi-user.target
```

4	Press Esc, type sh:wq, and hit Enter to save and exit the file.
5	Create a directory for the configuration files: 
```sh
sudo mkdir /etc/consul.d
```
Note: Creating a configuration file for the UI is optional. If you choose not to perform the following steps to do so, proceed to reloading the system. 
	6	Using vim, create a JSON configuration file for the UI:


 ```sh
 sudo vim /etc/consul.d/ui.json
```
7	In the file, paste in the following configuration: 
 ```sh
 { "addresses": { "http": "0.0.0.0" } }
```
8	Press Esc, type ```sh:wq```, and hit Enter to save and exit the file.
## Reload, Start, Enable, and Verify the Consul Service

1	Reload the system: 
 ```sh
sudo systemctl daemon-reload
```
2	Start the Consul service: 
  ```sh
 sudo systemctl start consul
```

3	Enable the Consul service: 
  ```sh
 sudo systemctl enable consul
```
4	Verify the status of the Consul service: 
  ```sh
 sudo systemctl status consul
```
 The output should indicate that the Consul service is active and running.

# Install and Configure the Vault Service
## Download, Unpack, and Move Vault to the Bin Directory
1	Download Vault: 
   ```sh
 wget https://releases.hashicorp.com/vault/1.5.0/vault_1.5.0_linux_amd64.zip
```
2	Unpack Vault: 
  ```sh
unzip vault_1.5.0_linux_amd64.zip
```
3	Move the Vault binary to the bin directory: 
  ```sh
sudo mv vault /usr/bin
```
## Create and Configure the Vault systemd Service

1	Create a directory for the configuration file: 
   ```sh
sudo mkdir /etc/vault/
```
2	Get and copy the IP address of the server: 
  ```sh
ip addr show
```
Note: Alternately, if you still have the IP address accessible from when you configured Consul, you could just copy/paste the address from where you saved it. 
3	Using vim, create the configuration file:
  ```sh
sudo vim /etc/vault/config.hcl
```

4	In the file, paste in the following configuration, replacing Consul.IP.ADDRESS with the IP address you just obtained: 
  ```json

storage "consul" {
  address = "Consul.IP.ADDRESS:8500"
  path = "vault/"
}
listener "tcp" {
  address = "0.0.0.0:80"
  tls_disable = 1
}
ui = true
```
5	Press Esc, type   ```sh:wq```, and hit Enter to save and exit the file.
6	Using vim, create a systemd service file: 
  ```sh
sudo vim /etc/systemd/system/vault.service
```
7	In the file, paste in the following configuration: 
  ```sh
[Unit] Description=Vault Documentation=https://www.vault.io/ [Service] ExecStart=/usr/bin/vault server -config=/etc/vault/config.hcl ExecReload=/bin/kill -HUP $MAINPID LimitNOFILE=65536 [Install] WantedBy=multi-user.target
```
 
8	Press Esc, type   ```sh:wq```, and hit Enter to save and exit the file.

## Reload, Start, Enable, and Verify the Vault Service
1	Reload the system: 
  ```sh
sudo systemctl daemon-reload
```
2	Start the Vault service: 
  ```sh
sudo systemctl start vault
```
3	Enable the Vault service: 
  ```sh
sudo systemctl enable vault
```
4	Verify the status of the Vault service: 
  ```sh
sudo systemctl status vault
```

## Connect to the Vault Service
1	Using the dig command and the public IP address of the lab server (found on the lab credentials page), get and copy the fully qualified domain name (FQDN) of the server: 
  ```sh
dig -x <SERVER IP>
```

2	Set the Vault address for the current session, replacing DOMAIN with the FQDN you just obtained: 
  ```sh
export VAULT_ADDR="http://<DOMAIN>"
```
3	Set the Vault address to be persistent upon each system boot, replacing DOMAIN with the same FQDN: 
  ```sh
echo "export VAULT_ADDR=http://<DOMAIN>" >> ~/.bashrc
```
4	Install autocomplete for Vault commands: 
  ```sh
vault -autocomplete-install
```
5	And then enable autocomplete:
  ```sh
complete -C /usr/bin/vault vault
```
## Initialize and Access the Vault
1	Initialize the Vault: 
  ```sh
vault operator init
```
 The output will include five Unseal Keys and an Initial Root Token that you will use to access your Vault. 
 You will need to supply three keys to unseal the Vault. 
 Note: It is important to save the keys and root token. If lost, access to the Vault will be lost. Best practice is to save the keys and token in a secure location. 
2	Run the unseal command with no arguments: 
  ```sh
vault operator unseal
```
3	When prompted with Key (will be hidden):, copy and paste one of the keys provided and hit Enter.
4	Repeat the process using two additional keys to unseal the Vault. 
Note: When the Vault has been successfully unsealed, the Sealed parameter will display as false in the returned output. 
5	Log in to the Vault using the root token that was provided: 
  ```sh
vault login <ROOT_TOKEN>
```
Vault will notify you if you have successfully authenticated and are logged in
