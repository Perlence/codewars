#lang racket/base

#| k-Primes (5 kyu)

https://www.codewars.com/kata/k-primes
|#

(require racket/list
         (only-in math factorize))

(define (count-k-primes k start end)
  (filter (λ (n) (= k (count-prime-factors n))) (range start end)))

(define (count-prime-factors n)
  (for/sum ([prime-exp (factorize n)])
    (second prime-exp)))

(module+ test
  (require rackunit)
  (check-equal? (map count-prime-factors '(2 3 4 5 6 7 8 9 10)) '(1 1 2 1 2 1 3 2 2))
  (check-equal? (count-k-primes 5 500 600) '(500 520 552 567 588 592 594)))
