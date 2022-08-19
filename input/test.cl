class Main inherits IO {
    num : Int <- 500;
    a : Int <- 1;
    b : Int <- 1;
    c : Int <- 1;
    main() : SELF_TYPE {
	{
        a <- b;
        if a=2 then b<-2 else c<-55 fi;
	}
    };

    fibonacci(n: Int) : Int {
        {( let f : Int in
      	 if n=1 then f<-1 else
         if n=2 then f<-1 else
        	 f<-fibonacci(n-1)+fibonacci(n-2)
         fi fi
       );}
     };
};