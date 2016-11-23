(ns transportation-on-vacation
  (:require [clojure.test :refer :all]))

(defn rental-car-cost [d]
  (let [mul (* d 40)]
    (cond (>= d 7) (- mul 50)
          (>= d 3) (- mul 20)
          :else mul)))

(defn test-assert [act exp]
  (is (= act exp)))

(deftest a-test1
  (is (= (rental-car-cost 1) 40))
  (is (= (rental-car-cost 3) 100))
  (is (= (rental-car-cost 8) 270)))
