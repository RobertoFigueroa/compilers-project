class Main inherits IO {
    num : Int <- 500;
    a : Int <- 7;
    b : Int <- 8;
    c : Int <- 11;
    main() : SELF_TYPE {
	{
        a <- a + b * c;
	}
    };
};