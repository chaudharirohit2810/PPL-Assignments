
/* Flights */
/*Source, Airline, Destination, Price, Duration*/
flight(toronto,aircanada,madrid,900,480).
flight(toronto,united,madrid,950,540).
flight(toronto,iberia,madrid,800,480).
flight(toronto,aircanada,london,500,360).
flight(toronto,united,london,650,420).
flight(madrid,aircanada,barcelona,100,60).
flight(madrid,iberia,barcelona,120,65).
flight(madrid,iberia,malaga,50,60).
flight(madrid,iberia,valencia,40,50).
flight(malaga,iberia,valencia,80,120).
flight(barcelona,iberia,valencia,110,75).
flight(paris,united,toulouse,35,120).
flight(barcelona,iberia,london,220,240).

/* Airports */
/* City, Tax, Duration*/
airport(toronto,50,60).
airport(madrid,75,45).
airport(valencia,40,20).
airport(malaga,50,30).
airport(barcelona,40,30).
airport(paris,50,60).
airport(london,75,80).
airport(toulouse,40,30).


/* is there flight from A to B*/
isFlightExist(A, B):-
    flight(A, C, B, D, E),format('There is flight from ~w to ~w via ~w \n', [A, B, C]);
    flight(B, C, A, D, E),format('There is flight from ~w to ~w via ~w \n', [B, A, C]).

/* checking if flight is cheap*/
isFlightCheap(A,C,B):- 
    flight(A,C,B,P,D), P<400, format("Flight from ~w to ~w via ~w is cheap \n", [A, B, C]);
    format("Flight from ~w to ~w via ~w is not cheap \n", [A, B, C]).

/* is it possible to go from A to B in two flights*/
isTwoFlight(A, B):- 
    isFlightExist(A, X), isFlightExist(X,B).

/* Flight is preferred if it is cheap or from aircanada */
isPreferred(A, C, B):- C == aircanada; isFlightCheap(A, C, B) -> write('Flight is preferred \n').

/* checking if there is flight from A to B with airline united*/
isFlightUnited(A, B):- flight(A, C, B, P, D), C == united, format('There is flight from ~w to ~w via ~w \n', [A, B, C]).

/* checking if there is flight from A to B with airline aircanada*/
isFlightAirCanada(A, B):- flight(A, C, B, P, D),C == aircanada, format('There is flight from ~w to ~w via ~w \n', [A, B, C]).

/* Checking it with and*/
isFlight(A, B):- isFlightUnited(A, B), isFlightAirCanada(A, B), format('There is flight from ~w to ~w via both united and air canada \n', [A, B]).



