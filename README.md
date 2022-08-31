# newscript
example:
```
    set n 0
    set t 3
    set one 1
    set two 2
    
    // show text
    show 1
    show 2
    show 3
    show % one
    
    // input
    set inp input /:
    
    // if
    if n == 0 show n==0
    if n != 1 show n!=1
    
    // operators: +=, -=, *=, /=
    n += 1
    n -= one
    
    n *= 2
    
    // load script.ns
    // work only on windows
    load main1.ns
    
    // run
    run ls
    run echo 1 2 3
    
    // end
    end
```
