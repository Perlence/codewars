#lang racket/base

#| String incrementer (5 kyu)

https://www.codewars.com/kata/string-incrementer
|#

(require racket/match
         racket/list
         racket/string
         racket/format)

(define (increment-string str)
  (match (split-string str)
    [(list base number) (string-append base (increment-number-ending number))]))

(define (split-string str)
  (define mo (regexp-match-positions #rx"[0-9]+$" str))
  (match mo
    [(list (cons start end)) (list (substring str 0 start) (substring str start end))]
    [#f (list str "")]))

(define (increment-number-ending str)
  (~r (add1 (or (string->number str) 0))
      #:min-width (max 1 (string-length str))
      #:pad-string "0"))

(module+ test
  (require rackunit)

  (check-equal? (split-string "foobar") '("foobar" ""))
  (check-equal? (split-string "foobar000") '("foobar" "000"))

  (check-equal? (increment-number-ending "000") "001")
  (check-equal? (increment-number-ending "99") "100")

  (check-equal? (increment-string "foobar000") "foobar001")
  (check-equal? (increment-string "foo") "foo1")
  (check-equal? (increment-string "foobar001") "foobar002")
  (check-equal? (increment-string "foobar99") "foobar100")
  (check-equal? (increment-string "foobar099") "foobar100")
  (check-equal? (increment-string "") "1")
  (check-equal? (increment-string "f00bar099") "f00bar100"))
