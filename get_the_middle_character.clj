(ns get-the-middle-character
  (:require [clojure.test :refer :all]))

(defn get-middle [s]
  (let [len (count s)
        half (/ len 2)]
    (if (even? len)
      (subs s (dec half) (inc half))
      (subs s half (inc half)))))

(deftest dig-pow-test
  (is (= (get-middle "test") "es"))
  (is (= (get-middle "testing") "t"))
  (is (= (get-middle "middle") "dd"))
  (is (= (get-middle "A") "A")))
