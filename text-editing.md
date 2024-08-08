#Text Editing with vim

Open file
```sh
vim Dockerfile
```

View the line numbers
```sh
:set number
```

Jump to line 7
```sh
7
```

Enter to visual mode
```sh
Shift +v
```

Copy the current contents of line 7
```sh
y
```

Paste the copied contents
```sh
p
```

Delete the contents
```sh
dw
```

Undo deletion
```sh
u
```

Delete the entire line
```sh
dd or d+shift+w
```

save and exit
```sh
:wq
```

## Add the comment // Dockerfile on the top of the file
Open file
```sh
vim Dockerfile
```

Enter Insert mode and add new line
```sh
Shift+o
```

Type the comment
Open file
```sh
// Dockerfile
```

Save
```sh
:x
```
## Replacing text

add lines numbers
```sh
:set number
```
Change port 8080 to 3000 on line 15
```sh
:15s/8080/3000
```

Update word test to lab in entire file
```sh
:%s/test/lab/gci
```

