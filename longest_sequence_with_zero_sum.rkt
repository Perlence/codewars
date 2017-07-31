#lang racket/base

#| Longest sequence with zero sum (5 kyu)

https://www.codewars.com/kata/longest-sequence-with-zero-sum
longest_sequence_with_zero_sum.rkt
|#

(require racket/list)

(define (max-zero-sequence-length-naive lst)
  (for*/last ([len (in-range 1 (add1 (length lst)))]
              [start (in-range 0 (- (length lst) len))]
              #:when (zero? (apply + (take (drop lst start) len))))
    (take (drop lst start) len)))

(define (max-zero-sequence-length lst)
  (define pyra (pyramid lst))
  (define (column-length column)
    (let ([zero-tail (memq 0 column)])
      (if zero-tail
        (- (length column) (length zero-tail))
        0)))
  (define longest-column (max-key column-length pyra))
  (define initial (takef longest-column (λ (x) (not (zero? x)))))
  (reverse (map (λ (a b) (- b a))
                (cons 0 initial)
                (append initial '(0)))))

(define (pyramid lst)
  (let loop ([lst lst]
             [prev-column empty])
    (if (null? lst)
      empty
      (let* ([head (first lst)]
             [cur-column (cons head (map (λ (a) (+ a head)) prev-column))])
        (cons cur-column (loop (rest lst) cur-column))))))

(define (max-key proc lst)
  (when (null? lst)
    error "max-key arg is an empty list")
  (let loop ([lst (rest lst)]
             [result (first lst)]
             [m (proc (first lst))])
    (if (null? lst)
      result
      (let* ([head (first lst)]
             [proc-head (proc head)]
             [tail (rest lst)])
        (if (> proc-head m)
          (loop tail head proc-head)
          (loop tail result m))))))

(module+ test
  (require rackunit)

  (check-equal? (pyramid '(5 -2 -3 4)) '((5) (-2 3) (-3 -5 0) (4 1 -1 4)))

  (pyramid '(25 -35 12 6 92 -115 17 2 2 2 -7 2 -9 16 2 -11))
  (time (check-equal? (max-zero-sequence-length '(25 -35 12 6 92 -115 17 2 2 2 -7 2 -9 16 2 -11))
                      '(92 -115 17 2 2 2)))
  (time (check-equal? (max-zero-sequence-length (append (range 500) '(92 -115 17 2 2 2) (range 500)))
                      '(92 -115 17 2 2 2))))
