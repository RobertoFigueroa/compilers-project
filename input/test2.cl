class Factorial {
  	var: Int <- 0;
  	
  	factorial(n: Int) : Int {
      {( let f : Int in
      	 if n=0 then f<-0 else
         if n=1 then f<-1 else
        	 f<-n*factorial(n-1)
         fi fi
       );}
    };
  
  };


class Otro {
  	variable: Int <- 0;
  	
  	my_otro(n: Int) : Int {
      {( let f : Int in
      	 if n=0 then f<-0 else
         if n=1 then f<-1 else
        	 f<-n*factorial(n-1)
         fi fi
       );}
    };
  
  };
