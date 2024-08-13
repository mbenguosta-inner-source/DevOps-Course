# Configure Authentication with HashiCorp Vault

## Unseal the Vault and Log in with the Root Token
1	In the Vault Server, retrieve the vault keys:
 ```sh
 cat Keys
 ```
2	Unseal the vault:
 ```sh
vault operator unseal <UNSEAL_KEY_1>
vault operator unseal <UNSEAL_KEY_2>
vault operator unseal <UNSEAL_KEY_3>
```
3	Log in with the Initial Root Token:
 ```sh
vault login <INITIAL_ROOT_TOKEN>
```
## Enable KV Secrets Engine and Write a Generic Test Secret
1	Enable a kv secrets engine at the secrets-kv path: 
 ```sh
vault secrets enable -path=secrets-kv kv
```

2	Write a secret to the secrets-kv path: 
 ```sh
vault kv put secrets-kv/tokenTestSecret tokenTestKey=tokenTestValue
```

## Create a Policy That Gives Read Permissions to the KV Secrets Engine

1	Create a policy file named my_token_policy.hcl:
 ```sh
vim /home/cloud_user/my_token_policy.hcl
```
2	Populate the policy file:
```hcl
path "secrets-kv/tokenTestSecret"{ capabilities = ["read"] }
```
3	Save the file:ESC :wq ENTER  
4	Write the policy:
 ```sh
vault policy write my_token_policy my_token_policy.hcl
```
## Create a Token, Test It Out, and Then Revoke It
1	Create a token: 
 ```sh
vault token create -policy="my_token_policy" -format=json | jq
```
2	Copy the client_token.
3	Log in with the newly created token: 
 ```sh
vault login <CLIENT_TOKEN>
```
4	Attempt to read the secret: 
 ```sh
vault kv get secrets-kv/tokenTestSecret
```
5	Attempt to write a new secret: 
 ```sh
vault kv put secrets-kv/tokenTestSecret tokenTestValue02=tokenTestKey02
```
6	Log in with the Initial Root Token: 
 ```sh
vault login <INITIAL_ROOT_TOKEN>
```
7	Revoke the client_token: 
 ```sh
vault token revoke <CLIENT_TOKEN>
```
