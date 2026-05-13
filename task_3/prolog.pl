
male(james).
male(peter).
male(david).
male(john).
male(michael).

female(mary).
female(susan).
female(linda).
female(grace).
female(ann).

% Parent relationships
parent(james, peter).
parent(mary, peter).

parent(james, susan).
parent(mary, susan).

parent(peter, john).
parent(linda, john).

parent(peter, ann).
parent(linda, ann).

parent(susan, michael).
parent(david, michael).

parent(susan, grace).
parent(david, grace).


% RULES


father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

child(X, Y) :-
    parent(Y, X).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

grandchild(X, Y) :-
    grandparent(Y, X).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

cousin(X, Y) :-
    parent(A, X),
    parent(B, Y),
    sibling(A, B).

uncle(X, Y) :-
    sibling(X, Z),
    parent(Z, Y),
    male(X).

aunt(X, Y) :-
    sibling(X, Z),
    parent(Z, Y),
    female(X).