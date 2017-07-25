#lang racket/base

#| Rock Paper Scissors! (8 kyu)

https://www.codewars.com/kata/rock-paper-scissors
|#

(define (rps p1 p2)
  (cond [(equal? p1 p2) "Draw!"]
        [(equal? p1 "rock") (if (equal? p2 "scissors") "Player 1 won!" "Player 2 won!")]
        [(equal? p1 "paper") (if (equal? p2 "rock") "Player 1 won!" "Player 2 won!")]
        [(equal? p1 "scissors") (if (equal? p2 "paper") "Player 1 won!" "Player 2 won!")]))

(module+ test
  (require rackunit)
  (for ([args '(["rock" "scissors"]
                ["scissors" "paper"]
                ["paper" "rock"])])
    (check-equal? (apply rps args) "Player 1 won!"))
  (for ([args '(["scissors" "rock"]
                ["paper" "scissors"]
                ["rock" "paper"])])
    (check-equal? (apply rps args) "Player 2 won!"))
  (for ([args '(["rock" "rock"]
                ["scissors" "scissors"]
                ["paper" "paper"])])
    (check-equal? (apply rps args) "Draw!")))
