class Main inherits IO {
    a : Int; --0
    b : Int; --4
    c : Int; --8

    main(n : Int) : SELF_TYPE {
	{
        b <- n;
        self;
    };


};