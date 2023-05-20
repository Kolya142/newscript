# newscript
example:
```
  // set var
    set n 0
    set t 3
    set one 1
    set two 2
    set nl \n
    set file open file.txt w
    
    // show text
    show 1
    show 2
    show 3
    show % one

    // file tools
    file write data // write
    set file_read read file
    
    // input
    set inp input /:
    
    // if
    if n == 0 show n==0
    if n != 1 show n!=1
    
    // operators: +=, -=, *=, /=
    n += 1 . int
    n -= % one int
    file_read += % nl str
    n *= 2 . int
    
    // load script.ns
    load main1.ns
    
    // run
    run ls
    run echo 1 2 3
    
    // end
    end
```
