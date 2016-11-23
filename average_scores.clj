(ns average-scores
  (:require [clojure.test :refer :all]))

(defn round [x]
  (Math/round (float x)))

(defn average [data]
  (if (empty? data)
    0
    (round (/ (apply + data) (count data)))))

(deftest basic-test
  (testing "Empty collection"
    (is (= 0 (average []))))
  (testing "One-element collection"
    (is (= 3 (average [3]))))
  (testing "Normal collection"
    (is (= 4 (average [5 3 3 5]))))
  (testing "When mean isn't int"
    (is (= 9 (average [7 8 9 10])))))
