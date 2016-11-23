(ns convert-a-string-to-a-number
  (:require [clojure.test :refer :all]))

(defn string-to-number [str]
  (Integer/parseInt str))

(deftest examples
  (is (= (string-to-number "1234") 1234))
  (is (= (string-to-number "605") 605))
  (is (= (string-to-number "1405") 1405))
  (is (= (string-to-number "-7") -7)))
