#lang racket/base

#| Double Cola (5 kyu)

https://www.codewars.com/kata/double-cola
|#

(define (who-is-next people n)
  (let loop ([n (sub1 n)]
             [q 5])
    (if (< n q)
      (list-ref people (quotient n (quotient q 5)))
      (loop (- n q) (* q 2)))))

(module+ test
  (require rackunit)

  (check-equal? (who-is-next '("Sheldon" "Leonard" "Penny" "Rajesh" "Howard") 1) "Sheldon")
  (check-equal? (who-is-next '("Sheldon" "Leonard" "Penny" "Rajesh" "Howard") 5) "Howard")
  (check-equal? (who-is-next '("Sheldon" "Leonard" "Penny" "Rajesh" "Howard") 52) "Penny")
  (check-equal? (who-is-next '("Sheldon" "Leonard" "Penny" "Rajesh" "Howard") 1000000000) "Penny"))
