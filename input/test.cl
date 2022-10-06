class Main inherits IO {
    num : Int <- 500;
    a : Int <- 1;
    b : Int <- 1;
    c : Int <- 1;
    x : Int <- num - a;

    main() : SELF_TYPE {
	{
        a <- b + c; 
        --c <- ~b;
        if a=2 then b<-2 else c<-55 fi;
	}
    };


};