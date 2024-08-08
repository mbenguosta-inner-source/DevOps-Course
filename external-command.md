## Run external commands in vim editor

Sort text file by line
```sh
:% ! sort
```

Write data to file
```sh
:1,10 w >> subfile.txt
```

Search for S
```sh
:/^S
```

Write subfile (from 10 to the end line) to another file
```sh
:10,$ >> 10-end.txt
```

Copy another file content to current file
```sh
:r source-file.txt
```
