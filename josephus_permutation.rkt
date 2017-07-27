#lang racket/base

#| Josephus Permutation (5 kyu)

https://www.codewars.com/kata/josephus_permutation
|#

(require racket/list)

(define (josephus items k)
  (let loop ([items items]
             [n 0])
    (if (null? items)
      empty
      (let ([n (modulo (+ (sub1 n) k) (length items))])
        (cons (list-ref items n)
              (loop (append (take items n) (drop items (add1 n)))
                    n))))))

(module+ test
  (require rackunit)

  (check-equal? (josephus '(1 2 3 4 5 6 7 8 9 10) 1) '(1 2 3 4 5 6 7 8 9 10))
  (check-equal? (josephus '(1 2 3 4 5 6 7 8 9 10) 2) '(2 4 6 8 10 3 7 1 9 5))
  (check-equal? (josephus '("C" "o" "d" "e" "W" "a" "r" "s") 4) '("e" "s" "W" "o" "C" "d" "r" "a"))
  (check-equal? (josephus '(1 2 3 4 5 6 7) 3) '(3 6 2 7 5 1 4))
  (check-equal? (josephus '() 3) '()))
