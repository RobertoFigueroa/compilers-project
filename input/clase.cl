class Results {

    ress: Int; 

    get_ress() : Int {
        ress
    };

    set_res(i: Int) : SELF_TYPE {
        {
            ress <- i;
            self;
        }
    };
};


class Factorial {
    factorial(n: Int) : Int {
      	 if n=0 then 0 else
         if n=1 then 1 else
        	n*factorial(n-1)
         fi fi
    };
};

class Div inherits Factorial {
    div(n: Int, o: Int) : Int {
        n/o
    };
};

class SumSub inherits Div {

    sum(n: Int, o: Int) : Int {
        n + o
    };

    sub(n: Int, o: Int) : Int {
        n - o
    };

    --malreturn(n: Int, o: Int) : String {
    --    n * o
    --};
    


};

class Calculator inherits SumSub {
    mul(n: Int, o: Int) : Int {
        n*o
    };
};

class Main inherits IO {
    a : Results;
    calc: Calculator;
    s: SumSub;
    t : Int;
    main() : SELF_TYPE {
        {
            --PRUEBAS HERENCIA
            --s@Calculator.mul(2,1);
            
            --PRUEBAS PARAMS
            --a.set_res(calc.mul(5,"compiladores"));
            --a.set_res(calc.mul(5));
            --a.set_res(calc.mul(5,6,7,8,9,10));

            --PRUEBAS INEXISTENCIA
            --x.set_res(1);
            --s.sumnoexiste(1,2);

            --CAST
            t <- true;
            --t <- "prueba";

            --RETORNO
            --s.malreturn(1,2);


            --PROGRAMA NORMAL
            a.set_res(calc.mul(5,4));
            out_int(a.get_ress());
            a.set_res(calc@SumSub.sum(5,6));
            out_int(a.get_ress());
            a.set_res(calc@SumSub.sub(5, calc@SumSub.sum(5,6)));
            out_int(a.get_ress());
            a.set_res(calc@Factorial.factorial(5));
            out_int(a.get_ress());
            self;
        }
    } ;

};