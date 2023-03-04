kobieta(ela).
kobieta(ala).
kobieta(ola).
kobieta(iza).
menzczyzna(tomek).
menzczyzna(robert).
menzczyzna(jacek).
menzczyzna(krzysztof).

rodzic(ela,robert).
rodzic(tomek,robert).
rodzic(tomek,iza).
rodzic(robert,ala).
rodzic(robert,ola).
rodzic(ola,jacek).

dziecko(Y,X):-
	rodzic(X,Y).

brat(X,Y):-
	rodzic(Z,X),
	rodzic(Z,Y),
	menzczyzna(X),
	X\=Y.

siostra(X,Y):-
	rodzic(Z,X),
	rodzic(Z,Y),
	kobieta(X),
	X\=Y.

rodzenstwo(X,Y):-
	brat(X,Y);
	siostra(X,Y),
	X\=Y.

przodek(X,Z):-
	rodzic(X,Z).

przodek(X,Z):-
	rodzic(X,Y),
	przodek(Y,Z).

potomek(X,Z):-
	przodek(Z,X).

spokrewnieni(X,Y):-
	przodek(Z,X),
	przodek(Z,Y),
	X\=Y.

