#lang racket/base

#| Rectangle into Squares (6 kyu)

https://www.codewars.com/kata/rectangle-into-squares
|#

(require racket/list)

(define (sq-in-rect len width)
  (let loop ([len len]
             [width width]
             [result empty])
    (cond
      [(= len width) (if (null? result)
                       empty
                       (reverse (cons (first result) result)))]
      [(< len width) (loop len (- width len) (cons len result))]
      [else (loop (- len width) width (cons width result))])))

(module+ test
  (require rackunit)

  (check-equal? (sq-in-rect 5 3) '(3 2 1 1))
  (check-equal? (sq-in-rect 4 3) '(3 1 1 1))
  (check-equal? (sq-in-rect 6 3) '(3 3))
  (check-equal? (sq-in-rect 20 14) '(14 6 6 2 2 2))
  (check-equal? (sq-in-rect 5 5) empty))
