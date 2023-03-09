%%% Jako pierwszą klauzulę (nie komentarz!) należy zdefiniować swoje dane     %%%
%%% w postaci faktu: student(imię, nazwisko, numer_indeksu, numer_grupy_lab). %%%
%%% Przykładowo:  student(jan,nowak_jeziorański,150000,2).                    %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
student(krzysztof,ma�czak,155939,9).

kobieta(maria).
kobieta(ewa).
kobieta(joanna).
kobieta(agata).
kobieta(anna).
kobieta(agnieszka).
kobieta(beata).
kobieta(iwona).

m�czyzna(piotr).
m�czyzna(adam).
m�czyzna(marek).
m�czyzna(robert).
m�czyzna(jan).
m�czyzna(krzysztof).
m�czyzna(radek).
m�czyzna(darek).
m�czyzna(tomek).
m�czyzna(jacek).

rodzic(maria,marek).
rodzic(piotr,marek).
rodzic(maria,agata).
rodzic(piotr,agata).
rodzic(piotr,jan).
rodzic(maria,jan).

rodzic(adam,joanna).
rodzic(ewa,joanna).
rodzic(adam,anna).
rodzic(ewa,anna).
rodzic(ewa,krzysztof).
rodzic(adam,krzysztof).

rodzic(robert,radek).
rodzic(agata,radek).
rodzic(robert,beata).
rodzic(agata,beata).

rodzic(jan,darek).
rodzic(jan,tomek).
rodzic(anna,darek).
rodzic(anna,tomek).

rodzic(krzysztof,jacek).
rodzic(agnieszka,jacek).
rodzic(krzysztof,iwona).
rodzic(agnieszka,iwona).

ma��e�stwo(maria,piotr).
ma��e�stwo(adam,ewa).
ma��e�stwo(robert,agata).
ma��e�stwo(jan,anna).
ma��e�stwo(krzysztof,agnieszka).

matka(X,Y):-
	rodzic(X,Y),
	kobieta(X).

ojciec(X,Y):-
	rodzic(X,Y),
	m�czyzna(X).

siostra(X,Y):-
	kobieta(X),
	rodzic(Z,X),
	rodzic(Z,Y),
	X\=Y.

brat(X,Y):-
	m�czyzna(X),
	rodzic(Z,X),
	rodzic(Z,Y),
	X\=Y.

babcia(X,Y):-
	kobieta(X),
	rodzic(Z,Y),
	rodzic(X,Z).

dziadek(X,Y):-
	m�czyzna(X),
	rodzic(Z,Y),
	rodzic(X,Z).

wuj(X,Y):-
	m�czyzna(X),
	siostra(Z,X),
	matka(Z,Y).

stryj(X,Y):-
	m�czyzna(X),
	brat(Z,X),
	ojciec(Z,Y).

rodze�stwo(X,Y):-
	rodzic(Z,X),
	rodzic(Z,Y).

kuzyn(X,Y):-
	m�czyzna(X),
	rodzic(Z,X),
	rodzic(Q,Y),
	rodzic(U,Z),
	rodzic(U,Q),
	Z\=Q,
	X\=Y.

te�ciowa(X,Y):-
	m�czyzna(Y),
	ma��e�stwo(Y,Z),
	matka(X,Z).

te�ciowa(X,Y):-
	m�czyzna(Y),
	ma��e�stwo(Z,Y),
	matka(X,Z).


m��(X,Y):-
	m�czyzna(X),
	ma��e�stwo(X,Y).

m��(X,Y):-
	m�czyzna(X),
	ma��e�stwo(Y,X).

szwagier(X,Y) :-
	m�czyzna(X),
	m��(Y,Z),
	brat(X,Z).

szwagier(X,Y) :-
	m�czyzna(X),
	m��(X,Z),
	siostra(Z,Y).
