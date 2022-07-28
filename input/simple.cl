class Main inherits IO {
    num : Int <- 500;
    main() : SELF_TYPE {
	{
	    out_string((num).type_name());
	    out_string((new Object).type_name()).
	    out_string((isvoid self).type_name());
	}
    };
};