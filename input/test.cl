class Main inherits IO {
    num : Int <- 500;
    a : Int <- 1;
    b : Int <- 1;
    c : Int <- 1;
    main() : SELF_TYPE {
	{
        a <- a + b * c;
	}
    };
};