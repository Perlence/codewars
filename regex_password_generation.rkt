#lang racket/base

#| Regex Password Validation (5 kyu)

https://www.codewars.com/kata/regex-password-validation
|#

(require racket/string)

(define (validate password)
  (define password-chars (string->list password))
  (and (>= (string-length password) 6)
       (andmap char-alphanumeric? password-chars)
       (ormap char-lower-case? password-chars)
       (ormap char-upper-case? password-chars)
       (ormap char-numeric? password-chars)))

(define (char-alphanumeric? c)
  (or (char-lower-case? c) (char-upper-case? c) (char-numeric? c)))

(define (char-lower-case? c)
  (and (char<=? #\a c) (char<=? c #\z)))

(define (char-upper-case? c)
  (and (char<=? #\A c) (char<=? c #\Z)))

(define (char-numeric? c)
  (and (char<=? #\0 c) (char<=? c #\9)))

(module+ test
  (require rackunit)
  (check-true (validate "djI38D55"))
  (check-false (validate "a2.d412"))
  (check-false (validate "JHD5FJ53"))
  (check-false (validate "!fdjn345"))
  (check-false (validate "jfkdfj3j"))
  (check-false (validate "123"))
  (check-false (validate "abc"))
  (check-true (validate "Password123")))
