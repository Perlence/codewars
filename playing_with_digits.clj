(ns playing-with-digits
  (:require [clojure.test :refer :all]))

(defn digits [n]
  (if (< n 10)
    [n]
    (conj (digits (int (/ n 10))) (mod n 10))))

(defn dig-pow [n p]
  (let [digs (digits n)
        sum (apply + (map #(Math/pow %1 %2)
                          digs
                          (range p (+ p (count digs)))))
        m (mod sum n)]
    (if (= m 0.0) (int (/ sum n)) -1)))

(deftest digits-test
  (is (= (digits 9) [9]))
  (is (= (digits 89) [8 9]))
  (is (= (digits 789) [7 8 9])))

(deftest dig-pow-test
  (is (= (dig-pow 89 1) 1))
  (is (= (dig-pow 92 1) -1))
  (is (= (dig-pow 695 2) 2))
  (is (= (dig-pow 46288 3) 51)))
